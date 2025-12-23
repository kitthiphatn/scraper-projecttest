# E-Commerce Price Scraper 🛒

Automated web scraper for extracting product pricing data from e-commerce websites with built-in anti-detection measures.

## ✨ Features

- 🔄 **Multi-page Auto-scraping** - Automatically scrape data from multiple pages
- 🛡️ **Anti-detection System** - Built-in bot detection prevention
- ☁️ **Cloudflare Bypass** - Handles Cloudflare challenge pages
- 💾 **Auto-save to CSV** - Automatically saves data to CSV format
- 🔄 **Auto-restart Driver** - Restarts driver every 50 pages to save memory
- ⏱️ **Random Delays** - Uses random delays to avoid detection

## 📋 Requirements

- Python 3.7+
- Google Chrome browser
- Internet connection

## 📦 Installation

### 1. Clone repository

```bash
git clone https://github.com/kitthiphatn/scraper-projecttest.git
cd scraper-projecttest
```

### 2. Install dependencies

```bash
pip install selenium webdriver-manager
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage

```bash
python MISS.py
```

### Configuration

Edit the configuration variables in `MISS.py`:

```python
# Target website URL
BASE_URL = "https://example-ecommerce.com/products"

# Start and end page numbers
START_PAGE = 1
END_PAGE = 100

# Output CSV filename
FILENAME = "product_prices.csv"
```

### Customizing CSS Selectors

Adjust CSS selectors to match your target website:

```python
# Find product cards
products = driver.find_elements(By.CSS_SELECTOR, ".product-item, .product-card")

# Extract product name
name = product.find_element(By.CSS_SELECTOR, ".product-name, h3").text

# Extract price
price = product.find_element(By.CSS_SELECTOR, ".price, .product-price").text
```

## 📊 Output Format

The program generates a CSV file with the following structure:

| Product Name | Price | Availability |
|--------------|-------|--------------|
| Product A    | $299  | In Stock     |
| Product B    | $599  | In Stock     |

## ⚙️ Configuration Options

### Chrome Options

- `--incognito` - Opens browser in incognito mode
- `--disable-blink-features=AutomationControlled` - Hides automation indicators
- Custom User-Agent - Mimics regular browser behavior

### Anti-Detection Features

- Removes webdriver property from navigator
- Random delays (2-4 seconds between requests)
- Driver restart every 50 pages
- Cloudflare challenge handling (30-second wait)

## 🔧 Troubleshooting

### Issue: ChromeDriver not working

**Solution:**
- Verify Chrome browser is installed
- Clear webdriver-manager cache: `rm -rf ~/.wdm`

### Issue: Elements not found

**Solution:**
- Verify CSS selectors match the target website
- Increase delay time
- Use browser developer tools to find correct selectors

### Issue: Blocked by Cloudflare

**Solution:**
- Increase delay time between requests
- Reduce number of pages scraped per session
- Use proxy or VPN

## 📝 Notes

- ⚠️ **Legal Notice**: Always check the target website's Terms of Service before scraping
- ⚠️ **Rate Limiting**: Use appropriate delays to avoid overloading target servers
- 💡 **Tip**: Test with a single page first (END_PAGE = 1) to verify selectors work correctly

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Created with ❤️ by [kitthiphatn](https://github.com/kitthiphatn)

## 🔗 Links

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

**Happy Scraping! 🎉**
