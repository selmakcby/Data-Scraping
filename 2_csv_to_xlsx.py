import csv
import xlsxwriter

"""
Converts a CSV file to an XLSX file, keeping only unique product URLs.
The script reads the 'product_urls.csv' file, extracts unique URLs, 
and writes them as hyperlinks in an Excel file ('unique_product_urls.xlsx').
"""

# Create a set to store unique URLs (sets automatically handle duplicates)
unique_urls = set()

# Open and read the CSV file containing product URLs
with open('product_urls.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        unique_urls.add(row[0])  # Add each URL to the set (duplicates will be ignored)

# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook('unique_product_urls.xlsx')
worksheet = workbook.add_worksheet()

# Write each unique URL as a hyperlink in the Excel file
row = 0
col = 0
for url in unique_urls:
    worksheet.write_url(row, col, url, string=url)  # Write URL as a clickable hyperlink
    row += 1

# Close the workbook to save the file
workbook.close()

