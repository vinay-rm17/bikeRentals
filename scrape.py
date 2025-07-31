import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# --- Provider Name (set it once) ---
provider_name = "Royal Brothers"

# --- ChromeDriver path ---
chrome_driver_path = r"C:\\Users\\rmvin\\OneDrive\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run browser in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Target URL ---
url="https://www.royalbrothers.com/search?utf8=%E2%9C%93&city=coorg&web_link=coorg&current_service_type=bike-rentals&only_electric=false&pickup=28+Jul%2C+2025&pickup_submit=28-07-2025&pickup_time=8%3A00+AM&dropoff=28+Jul%2C+2025&dropoff_submit=28-07-2025&dropoff_time=8%3A00+PM&bike_model%5B%5D=272&bike_model%5B%5D=4&bike_model%5B%5D=20&bike_model%5B%5D=7&bike_model%5B%5D=18&bike_model%5B%5D=308&bike_model%5B%5D=376&bike_model%5B%5D=341&bike_model%5B%5D=330&bike_model%5B%5D=29&bike_model%5B%5D=345&bike_model%5B%5D=344&bike_model%5B%5D=353&bike_model%5B%5D=296&bike_model%5B%5D=35&bike_model%5B%5D=314&bike_model%5B%5D=320&bike_model%5B%5D=321&bike_model%5B%5D=233"
driver.get(url)
time.sleep(5)  # Wait for page to load

# --- Parse HTML ---
soup = BeautifulSoup(driver.page_source, "html.parser")
bikes = soup.find_all("div", class_="tarif-desc-body")

# --- CSV File Path ---
csv_file = "bikes_data.csv"

# --- Create CSV with headers if not exists ---
if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Bike Name", "Price (₹)", "Provider"])

# --- Append data to CSV ---
with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for bike in bikes:
        name_tag = bike.find("h6", class_="valign-wrapper center-align bike_name")
        name = name_tag.get_text(strip=True) if name_tag else "N/A"

        price_tag = bike.find("span", id="rental_amount")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        writer.writerow([name, price, provider_name])
        print(f"Saved -> Bike: {name}, Price: ₹{price}, Provider: {provider_name}")

driver.quit()
print(f"\n✅ Data appended to {csv_file}")
