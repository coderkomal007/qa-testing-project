from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/login")

driver.find_element(By.NAME, "email").send_keys("test@example.com")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.ID, "submitLogin").click()

time.sleep(3)
assert "Welcome" in driver.page_source

driver.quit()
