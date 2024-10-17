from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1 = num1.text

    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2 = num2.text

    summ = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(summ)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()