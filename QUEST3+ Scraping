from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# --- CONFIG ---
SEARCH_TERM = "Panadol Extra Caplet"
CSV_FILENAME = "quest3plus_pmo2_data.csv"

# --- SETUP SELENIUM ---
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Enable for background scraping
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://quest3plus.bpfk.gov.my/pmo2/index.php")

# --- WAIT AND SELECT SEARCH MODE ---
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchBy")))
select = Select(driver.find_element(By.ID, "searchBy"))
select.select_by_value("1")  # 1 = Product Name

# --- ENTER SEARCH TERM SAFELY ---
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "searchTxt"))
)
search_box.click()
search_box.clear()
search_box.send_keys(SEARCH_TERM)

# --- SUBMIT SEARCH ---
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
)
time.sleep(2)

# Find all rows in the table body
rows = driver.find_elements(By.XPATH, "//tbody/tr")

# Loop through each row and extract data
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 4:
        mal_code = cells[1].text.strip()
        a_tag = driver.find_element(By.XPATH, f"//a[contains(text(), '{mal_code}')]")
        a_tag.click()

        # Extract all ingredient names
        rows = driver.find_elements(By.XPATH, "//tbody/tr")
        ingredients = [row.find_elements(By.TAG_NAME, "td")[1].text.strip() for row in rows if len(row.find_elements(By.TAG_NAME, "td")) >= 2]
        
        # Print in a single line, comma-separated
        print(", ".join(ingredients))
        #print(f"MAL Code: {mal_code}")
        #print("-" * 40)

# driver.quit()

