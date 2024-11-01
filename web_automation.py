from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Adjust path if ChromeDriver is not in your PATH

# Step 2: Open the target website
driver.get("https://the-internet.herokuapp.com/login")

# Step 3: Locate the username and password fields
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# Step 4: Input login credentials
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Step 5: Submit the form
password_input.send_keys(Keys.RETURN)

# Step 6: Wait to observe the result
time.sleep(3)  # Wait 3 seconds to see the logged-in screen

# Step 7: Verify login success
success_message = driver.find_element(By.ID, "flash")
if "You logged into a secure area!" in success_message.text:
    print("Login successful!")
else:
    print("Login failed!")

# Step 8: Close the browser
driver.quit()
