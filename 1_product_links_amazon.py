from pyppeteer import launch
import asyncio
from bs4 import BeautifulSoup
import csv

# URL to start scraping from Amazon
url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225011011&rh=n%3A%2116225011011%2Cn%3A1063306&ref=nav_em__nav_desktop_sa_intl_furniture_0_2_17_6'

"""
Function to scrape product URLs from Amazon pages. It navigates through multiple pages
until the desired number of product URLs (max_links) is collected. Results are written to 
a CSV file in real-time, so progress can be tracked as the script runs.
"""
async def scrape_with_pagination(max_links):
    # Launch a headless browser (this runs without opening a visible browser window)
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()

    # Set a Firefox user agent to mimic real browser behavior and avoid bot detection
    firefox_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    await page.setUserAgent(firefox_user_agent)

    # List to store collected product URLs
    product_urls = []
    
    # Start scraping from the initial URL
    current_url = url

    # Open a CSV file to store the product URLs
    with open('product_urls.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row in the CSV file
        writer.writerow(['Product URL'])

        # Continue scraping pages until the desired number of product links is collected
        while len(product_urls) < max_links:
            # Navigate to the current page URL
            await page.goto(current_url)

            try:
                # Wait for the product list to load (selector for each product)
                await page.waitForSelector('.s-result-item', options={'timeout': 60000})

                # Extract the page content and parse it with BeautifulSoup
                content = await page.content()
                soup = BeautifulSoup(content, 'html.parser')

                # Find all product links on the page
                product_links = soup.select('.s-result-item a.a-link-normal.a-text-normal')
                # Construct full URLs from the links
                urls = ['https://www.amazon.com' + link['href'] for link in product_links if link['href']]

                # Add the URLs to the list and write them to the CSV file in real-time
                for product_url in urls:
                    # Stop if we have collected enough URLs
                    if len(product_urls) >= max_links:
                        break
                    product_urls.append(product_url)

                    # Write each URL to the CSV file
                    writer.writerow([product_url])
                    # Flush the buffer so the file is updated immediately
                    csvfile.flush()

                print(f"Scraped {len(product_urls)} product URLs so far...")

                # If enough URLs are collected, stop the scraping process
                if len(product_urls) >= max_links:
                    break

                # Find the "Next" button to navigate to the next page
                next_page_button = soup.find('a', {'class': 's-pagination-next'})
                if next_page_button and 'href' in next_page_button.attrs:
                    # Update the current URL to the next page's URL
                    current_url = 'https://www.amazon.com' + next_page_button['href']
                else:
                    # Stop if no more pages are found
                    print("No more pages found.")
                    break

            except Exception as e:
                # Handle any errors that occur during scraping
                print(f"Error occurred: {e}")
                break  # Exit the loop on error

    # Close the browser after scraping is complete
    await browser.close()

    print(f"Scraping finished. Total products collected: {len(product_urls)}")
    return product_urls

# Ask the user how many product links they want to scrape
max_links = int(input("How many product links do you want to scrape? "))

# Run the async scraping function and wait for it to complete
urls = asyncio.get_event_loop().run_until_complete(scrape_with_pagination(max_links))
print(f"Scraping finished, check 'product_urls.csv' for results.")
