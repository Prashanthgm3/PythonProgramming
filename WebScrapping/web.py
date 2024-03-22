from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to chromedriver executable
chromedriver_path = "/path/to/chromedriver"

# URL of the webpage to scrape
url = "https://www.screener.in/company/GRAVITA/consolidated/"

# Configure Selenium webdriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the URL
driver.get(url)

# Wait for the Market Cap element to be visible
market_cap_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "data-bse"))
)

# Extract the Market Cap value
market_cap = market_cap_element.text.strip()

# Wait for the Current Price element to be visible
current_price_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "data-nse"))
)

# Extract the Current Price value
current_price = current_price_element.text.strip()

# Wait for the High / Low element to be visible
high_low_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), '52 Week High / Low')]/following-sibling::td"))
)

# Extract the High / Low value
high_low = high_low_element.text.strip()

# Print the extracted values
print("Market Cap:", market_cap)
print("Current Price:", current_price)
print("High / Low:", high_low)

# Close the webdriver
driver.quit()
