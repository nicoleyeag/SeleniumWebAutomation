from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"  # Adjust this if the path differs
chrome_options.add_argument("--headless")  # Optional, for headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Specify the path to ChromeDriver
service = Service("/home/nicole/.cache/selenium/chromedriver/linux64/130.0.6723.91/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test by navigating to a page
driver.get("https://www.example.com")
print(driver.title)

# Close the browser
driver.quit()
