import time
import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete

try:
    browser = webdriver.Chrome(desired_capabilities=caps)
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, 'button[type=submit]')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
