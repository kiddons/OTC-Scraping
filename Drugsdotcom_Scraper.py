from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup browser
options = Options()
options.add_argument("--headless")  # Uncomment for headless mode
driver = webdriver.Chrome(options=options)

# Target page
drug_url = "https://www.drugs.com/aspirin.html"
driver.get(drug_url)
time.sleep(2)  # Wait for full page load

# Extract drug name
try:
    drug_div = driver.find_element(By.CLASS_NAME, "ddc-pronounce-title")
    drug_name = drug_div.find_element(By.TAG_NAME, "h1").text
    print("Drug Name:", drug_name)
except Exception as e:
    print("Error extracting drug name:", e)

# Extract Warnings section (full text under #warnings)
try:
    warnings_section = driver.find_element(By.ID, "warnings")
    # Some pages use <p> tags, others might use <div> or plain text, so get all text
    warning_text = warnings_section.text
    print("\nWarnings:\n", warning_text)
except Exception as e:
    print("\nError extracting warnings section:", e)

driver.quit()
