# e-commerce-price-scraper.py
import time
import csv
import os
import random
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuration ---
BASE_URL = "https://example-ecommerce.com/products"
START_PAGE = 1
END_PAGE = 100
FILENAME = "product_prices.csv"

# --- Disable verbose logging ---
os.environ['WDM_LOG_LEVEL'] = '0'
logging.getLogger('selenium').setLevel(logging.CRITICAL)

def setup_driver():
    """Setup Chrome driver with anti-detection measures"""
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    chrome_options.add_argument("--log-level=3")
    
    log_path = "NUL" if os.name == 'nt' else "/dev/null"
    service = Service(ChromeDriverManager().install(), log_path=log_path)
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def scrape_products():
    """Scrape product data from multiple pages"""
    driver = setup_driver()
    
    # Initialize CSV file
    if not os.path.isfile(FILENAME):
        with open(FILENAME, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'Availability'])

    print(f"🚀 Starting scraper for {END_PAGE - START_PAGE + 1} pages...")
    print(f"📂 Saving to: {FILENAME}")

    try:
        for page in range(START_PAGE, END_PAGE + 1):
            target_url = f"{BASE_URL}?page={page}" if page > 1 else BASE_URL
            
            print(f"🔄 Loading page {page}/{END_PAGE}...")
            
            try:
                driver.get(target_url)
                time.sleep(random.uniform(2, 4))  # Random delay to avoid detection

                # Check for Cloudflare challenge
                if "Just a moment" in driver.title:
                    print(f"⚠️ Cloudflare detected on page {page}. Waiting...")
                    time.sleep(30)
                    driver.get(target_url)
                    time.sleep(10)

                # Find product elements (adjust selectors based on target site)
                products = driver.find_elements(By.CSS_SELECTOR, ".product-item, .product-card")
                
                data_buffer = []
                
                for product in products:
                    try:
                        # Extract product information
                        name = product.find_element(By.CSS_SELECTOR, ".product-name, h3").text
                        price = product.find_element(By.CSS_SELECTOR, ".price, .product-price").text
                        availability = "In Stock"  # Can be extracted from page
                        
                        if name and name.strip():
                            data_buffer.append([name.strip(), price.strip(), availability])
                            
                    except Exception:
                        continue

                # Save to CSV after each page
                if data_buffer:
                    with open(FILENAME, mode='a', newline='', encoding='utf-8-sig') as file:
                        writer = csv.writer(file)
                        writer.writerows(data_buffer)
                    print(f"   ✅ Page {page}: Saved {len(data_buffer)} items")
                else:
                    print(f"   ⚠️ Page {page}: No products found")

            except Exception as e:
                print(f"   ❌ Error on page {page}: {e}")
            
            # Restart driver every 50 pages to free memory
            if page % 50 == 0:
                print("🧹 Restarting driver...")
                driver.quit()
                time.sleep(3)
                driver = setup_driver()

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
    finally:
        driver.quit()
        print("🎉 Scraping completed")

if __name__ == "__main__":
    scrape_products()