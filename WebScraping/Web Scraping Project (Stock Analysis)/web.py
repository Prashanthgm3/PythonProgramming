import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://www.screener.in/company/AFFLE/consolidated/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', class_='data-table')

    # Check if the table is found
    if table:
        # Initialize a dictionary to store the extracted ratios
        ratios = {
            "Stock P/E": None,
            "Book Value": None,
            "Dividend Yield": None,
            "ROCE": None,
            "ROE": None,
            "Face Value": None
        }

        # Find all rows in the table
        rows = table.find_all('tr')

        # Loop through each row in the table
        for row in rows:
            # Extract header and value from each row
            header = row.find('td', class_='row-label')
            value = row.find('td', class_='row-value')

            # Check if both header and value exist
            if header and value:
                # Get text content of header and value
                header_text = header.get_text().strip()
                value_text = value.get_text().strip()

                # Check if header corresponds to a ratio we're interested in
                if header_text in ratios:
                    ratios[header_text] = value_text

        # Print the extracted ratios
        for ratio, value in ratios.items():
            print(f"{ratio}: {value}")
    else:
        print("Table not found on the webpage.")
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
