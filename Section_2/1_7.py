from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()