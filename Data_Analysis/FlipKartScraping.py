from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver (Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Flipkart's webpage
url = 'https://www.flipkart.com/search?q=laptops'
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')

# Extract product information as before
# product_containers = soup.find_all('div', class_='_1AtVbE')
# for container in product_containers:
#     title = container.find('div', class_='_4rR01T')
#     price = container.find('div', class_='_30jeq3')
#     if title and price:
#         print(f"Product: {title.text.strip()} - Price: {price.text.strip()}")
#
product_containers = soup.find_all('div')
for container in product_containers:
    title = container.find('div', class_='KzDlHZ')
    price = container.find('div', class_='Nx9bqj _4b5DiR')
    if title:
        print(f"Product: {title.text.strip()} ----Price: {price.text.strip()}")

# Close the browser
driver.quit()
