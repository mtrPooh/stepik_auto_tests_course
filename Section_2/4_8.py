from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    book_btn = browser.find_element(By.CSS_SELECTOR, '#book')

    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    book_btn.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')

    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)

    x = x_element.text
    y = calc(x)

    el = browser.find_element(By.CSS_SELECTOR, '#answer')
    el.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()