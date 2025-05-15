from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Configure Chrome to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")  # Required for Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents crashes

# Auto-download ChromeDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Example: Scrape a webpage
driver.get("https://example.com")
print("Page Title:", driver.title)
driver.quit()