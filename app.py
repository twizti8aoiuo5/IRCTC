from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

app = Flask(__name__)

@app.route('/')
def check_irctc():
    chrome_options = Options()
    
    # Critical flags to save RAM
    chrome_options.add_argument("--headless=new") # New headless mode is more efficient
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu") # Saves memory on servers without GPUs
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false") # Don't load images
    chrome_options.add_argument("--memory-pressure-off") 
    
    # Use a real user agent to appear less like a bot
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = None
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(30) # Prevent hanging
        
        driver.get("https://www.irctc.co.in/nget/train-search")
        title = driver.title
        return f"<h1>Success!</h1><p>Accessed: {title}</p>"
    except Exception as e:
        return f"<h1>Failed</h1><p>Error: {str(e)}</p>"
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
