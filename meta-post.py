from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL
url = "https://business.facebook.com/latest/composer?asset_id=109067838907447&business_id=1838981816516765&nav_ref=media_manager_redirect_home&ref=biz_web_home_create_post&context_ref=HOME"
driver.get(url)

try:
    # Wait for the "Accept" button with the specified data-testid attribute to become clickable
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='cookie-policy-manage-dialog-accept-button']"))
    )

    # Click on the "Accept" button
    accept_button.click()

except Exception as e:
    print("An error occurred:", e)

# Close the browser when done
driver.quit()
