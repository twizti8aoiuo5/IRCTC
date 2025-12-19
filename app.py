from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

app = Flask(__name__)

@app.route('/')
def check_irctc():
    chrome_options = Options()
    
    # Critical flags to reduce Memory Usage
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false") # Saves huge RAM
    
    # Fake User-Agent to look like a real browser
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = None
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # Set a timeout so it doesn't hang
        driver.set_page_load_timeout(30)
        
        driver.get("https://www.irctc.co.in/nget/train-search")
        title = driver.title
        return f"<h1>Service Online</h1><p>Successfully opened: {title}</p>"
    except Exception as e:
        return f"<h1>Error</h1><p>Could not load page. Error: {str(e)}</p>"
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    # Use Render's default port
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
