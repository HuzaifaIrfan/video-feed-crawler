from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(override=True)

# Access environment variables
SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
print(f"SELENIUM_URL at '{SELENIUM_URL}'")


class Crawler:
    def __init__(self):
        pass