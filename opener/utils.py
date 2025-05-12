import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .models import Website

def open_website(website_id):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            website = Website.objects.get(id=website_id)
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            
            while True:
                try:
                    driver.get(website.url)
                    time.sleep(15)
                    time.sleep(240 - 15)
                except Exception as e:
                    print(f"Error opening {website.url}: {e}")
                    time.sleep(10)  # صبر قبل از تلاش دوباره
                    continue
            driver.quit()
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries - 1:
                print(f"Failed to process website {website_id} after {max_retries} attempts")
            time.sleep(10)

def start_website_opener_thread(website_id):
    thread = threading.Thread(target=open_website, args=(website_id,))
    thread.daemon = True
    thread.start()