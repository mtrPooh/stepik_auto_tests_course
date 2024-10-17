from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "button")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()