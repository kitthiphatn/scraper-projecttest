# E-Commerce Price Scraper 🛒

โปรแกรมสำหรับดึงข้อมูลราคาสินค้าจากเว็บไซต์ e-commerce อย่างอัตโนมัติ พร้อมระบบป้องกันการตรวจจับ bot

## ✨ Features

- 🔄 **Auto-scraping หลายหน้า** - ดึงข้อมูลจากหลายหน้าได้อัตโนมัติ
- 🛡️ **Anti-detection** - มีระบบป้องกันการตรวจจับ bot
- ☁️ **Cloudflare bypass** - รองรับการข้าม Cloudflare challenge
- 💾 **Auto-save CSV** - บันทึกข้อมูลเป็น CSV อัตโนมัติ
- 🔄 **Auto-restart driver** - รีสตาร์ท driver ทุก 50 หน้าเพื่อประหยัด memory
- ⏱️ **Random delays** - ใช้ delay แบบสุ่มเพื่อหลีกเลี่ยงการตรวจจับ

## 📋 Requirements

- Python 3.7+
- Google Chrome browser
- Internet connection

## 📦 Installation

### 1. Clone repository

```bash
git clone <your-repository-url>
cd "Sacraper project"
```

### 2. ติดตั้ง dependencies

```bash
pip install selenium webdriver-manager
```

หรือใช้ requirements.txt (ถ้ามี):

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### การใช้งานพื้นฐาน

```bash
python MISS.py
```

### การปรับแต่ง Configuration

แก้ไขค่าต่างๆ ในไฟล์ `MISS.py`:

```python
# URL ของเว็บไซต์ที่ต้องการ scrape
BASE_URL = "https://example-ecommerce.com/products"

# หน้าเริ่มต้นและหน้าสุดท้าย
START_PAGE = 1
END_PAGE = 100

# ชื่อไฟล์ CSV ที่จะบันทึก
FILENAME = "product_prices.csv"
```

### การปรับแต่ง CSS Selectors

ปรับ CSS selectors ให้ตรงกับเว็บไซต์เป้าหมาย:

```python
# หา product cards
products = driver.find_elements(By.CSS_SELECTOR, ".product-item, .product-card")

# ดึงชื่อสินค้า
name = product.find_element(By.CSS_SELECTOR, ".product-name, h3").text

# ดึงราคา
price = product.find_element(By.CSS_SELECTOR, ".price, .product-price").text
```

## 📊 Output Format

โปรแกรมจะสร้างไฟล์ CSV ที่มีโครงสร้างดังนี้:

| Product Name | Price | Availability |
|--------------|-------|--------------|
| สินค้า A     | ฿299  | In Stock     |
| สินค้า B     | ฿599  | In Stock     |

## ⚙️ Configuration Options

### Chrome Options

- `--incognito` - เปิดโหมดไม่ระบุตัวตน
- `--disable-blink-features=AutomationControlled` - ปิดการแสดงว่าเป็น automation
- Custom User-Agent - ปลอมเป็น browser ปกติ

### Anti-Detection Features

- ปิดการแสดง webdriver property
- ใช้ random delays (2-4 วินาที)
- รีสตาร์ท driver ทุก 50 หน้า
- รองรับ Cloudflare challenge (รอ 30 วินาที)

## 🔧 Troubleshooting

### ปัญหา: ChromeDriver ไม่ทำงาน

**วิธีแก้:**
- ตรวจสอบว่าติดตั้ง Chrome browser แล้ว
- ลบ cache ของ webdriver-manager: `rm -rf ~/.wdm`

### ปัญหา: ไม่พบ elements

**วิธีแก้:**
- ตรวจสอบ CSS selectors ว่าตรงกับเว็บไซต์เป้าหมาย
- เพิ่ม delay time ให้มากขึ้น
- ใช้ browser developer tools เพื่อหา selectors ที่ถูกต้อง

### ปัญหา: ถูก Cloudflare block

**วิธีแก้:**
- เพิ่ม delay time
- ลดจำนวนหน้าที่ scrape ต่อครั้ง
- ใช้ proxy หรือ VPN

## 📝 Notes

- ⚠️ **Legal Notice**: ตรวจสอบ Terms of Service ของเว็บไซต์เป้าหมายก่อนใช้งาน
- ⚠️ **Rate Limiting**: ใช้ delay ที่เหมาะสมเพื่อไม่ให้เซิร์ฟเวอร์เป้าหมายโดนโหลดมากเกินไป
- 💡 **Tip**: ทดสอบกับหน้าเดียวก่อน (END_PAGE = 1) เพื่อตรวจสอบว่า selectors ทำงานถูกต้อง

## 🤝 Contributing

Pull requests are welcome! สำหรับการเปลี่ยนแปลงใหญ่ๆ กรุณาเปิด issue เพื่อหารือก่อน

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Created with ❤️ by [Your Name]

## 🔗 Links

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

**Happy Scraping! 🎉**
