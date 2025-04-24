from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(override=True)

# Access environment variables
SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
print(f"SELENIUM_URL at {SELENIUM_URL}")


# Connect to the Selenium standalone container
driver = webdriver.Remote(
    command_executor=SELENIUM_URL,  # Or replace 'localhost' with the container host
    options=options
)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(20)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

driver.quit()