from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    el.send_keys('Ivan')

    el = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    el.send_keys('Petrov')

    el = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    el.send_keys('Petrov@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    el = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    el.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()