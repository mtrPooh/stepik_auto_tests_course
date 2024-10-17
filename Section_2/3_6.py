from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    el = browser.find_element(By.CSS_SELECTOR, '#answer')
    el.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()