"""Run a complete SauceDemo purchase as a standalone Selenium script."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main() -> None:
    driver = webdriver.Chrome()
    try:
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
            "standard_user"
        )
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(
            "Test"
        )
        driver.find_element(By.ID, "last-name").send_keys("User")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        confirmation = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        print(confirmation.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
