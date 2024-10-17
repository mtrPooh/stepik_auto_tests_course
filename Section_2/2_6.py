from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value')
    y = calc(x.text)

    el = browser.find_element(By.CSS_SELECTOR, '#answer')
    el.send_keys(y)

    el = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    el.click()

    el = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", el)
    el.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()