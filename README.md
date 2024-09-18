# Amazon and Alibaba Product Scraper

This repository contains a set of scripts that perform web scraping on Amazon and Alibaba websites. The main objective is to collect product information, filter the results, and store them in Excel files. Additionally, the scripts can compare products across both platforms based on various attributes such as price and keywords.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Scripts](#scripts)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Dependencies](#dependencies)
7. [License](#license)

## Project Overview

This project scrapes product information from **Amazon** and searches for corresponding products on **Alibaba**. The data collected is stored in Excel files, and additional functionality includes filtering, comparison, and processing of the collected data.

The repository consists of the following functionalities:
- Scraping product URLs from Amazon and storing them in CSV and Excel files.
- Scraping product details from Alibaba for products that match the Amazon data.
- Filtering and cleaning the data before final output.
- Storing and combining the results into Excel files.

## Features

- **Amazon Product URL Scraper**: Scrapes product URLs from Amazon and saves them to CSV/Excel files.
- **Alibaba Product Finder**: Finds relevant products on Alibaba based on keywords from Amazon and compares prices.
- **Unique URL Filtering**: Ensures only unique product URLs are stored in the Excel files.
- **Excel Integration**: Automates the process of writing and manipulating data in Excel sheets, including combining and cleaning data.
- **Headless Browsing**: Uses `pyppeteer` and `Selenium` in headless mode for efficiency.

## Scripts

### 1. **Amazon Scraper**

- **File**: `amazon_scraper.py`
- **Description**: Scrapes product URLs from Amazon and stores them in a CSV file (`product_urls.csv`). The script allows the user to define the number of URLs they want to scrape. It also handles pagination.
- **Output**: `product_urls.csv`

### 2. **CSV to Excel Converter**

- **File**: `csv_to_excel.py`
- **Description**: Converts the CSV file of Amazon product URLs (`product_urls.csv`) to an Excel file (`unique_product_urls.xlsx`), ensuring that only unique URLs are saved.
- **Output**: `unique_product_urls.xlsx`

### 3. **Product Info Scraper (Amazon)**

- **File**: `product_info_scraper.py`
- **Description**: Extracts product details (title, price, and image) from the URLs stored in the Excel file (`unique_product_urls.xlsx`) and saves the details in another Excel file (`product_info.xlsx`).
- **Output**: `product_info.xlsx`

### 4. **Alibaba Scraper and Comparison**

- **File**: `alibaba_scraper.py`
- **Description**: Reads product information and keywords from Amazon and searches for similar products on Alibaba. It stores 5 matching results for each Amazon product in a new Excel file (`alibaba.xlsx`), including details like product title, image, rating, and price.
- **Output**: `alibaba.xlsx`

### 5. **Excel Cleanup**

- **File**: `excel_cleanup.py`
- **Description**: Cleans the Alibaba Excel file (`alibaba.xlsx`) by shifting columns and removing unnecessary rows. Ensures that the data is properly formatted.
- **Output**: `alibaba.xlsx`

### 6. **Excel Merger**

- **File**: `excel_merger.py`
- **Description**: Combines data from multiple Excel files, specifically merging the Alibaba product data (`alibaba.xlsx`) into an existing Excel file (`xxxx.xlsx`), grouping products into sets of 5 for each Amazon product.
- **Output**: `name_of_your_file.xlsx`

## Usage

1. Amazon Scraping
bash
Copy code
python amazon_scraper.py
This script will scrape Amazon product URLs and store them in product_urls.csv. You will be prompted to enter the number of URLs you want to scrape.

2. Convert CSV to Excel
bash
Copy code
python csv_to_excel.py
This script converts the product_urls.csv into an Excel file unique_product_urls.xlsx, filtering out duplicate URLs.

3. Extract Product Information
bash
Copy code
python product_info_scraper.py
This script extracts product details (title, price, image) from Amazon using the URLs in unique_product_urls.xlsx and stores them in product_info.xlsx.

4. Alibaba Scraping
bash
Copy code
python alibaba_scraper.py
This script searches Alibaba for products matching the Amazon data and stores the results in alibaba.xlsx.

5. Clean Excel File
bash
Copy code
python excel_cleanup.py
This script cleans up and adjusts the alibaba.xlsx file.

6. Merge Excel Files
bash
Copy code
python excel_merger.py
This script merges the alibaba.xlsx data into an existing file xxxx.xlsx.

## Dependencies

- beautifulsoup4
- pandas
- openpyxl
- xlsxwriter
- requests-html
- pyppeteer
- selenium
- geckodriver (for Selenium with Firefox)
- You can install the dependencies using:

## License

This project is licensed under the MIT License - see the LICENSE file for details.
