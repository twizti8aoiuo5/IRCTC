from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

app = Flask(__name__)

@app.route('/')
def open_irctc():
    # Setup Chrome options for a server environment
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Adding a realistic User-Agent to avoid immediate bot detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # In the Docker container, chromium-driver is located at /usr/bin/chromedriver
    service = Service(executable_path="/usr/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Attempt to open IRCTC
        driver.get("https://www.irctc.co.in/nget/train-search")
        page_title = driver.title
        driver.quit()
        return f"Status: Success! Page Title: {page_title}"
    except Exception as e:
        if driver:
            driver.quit()
        return f"Status: Failed. Error: {str(e)}"

if __name__ == "__main__":
    # Render provides a PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)