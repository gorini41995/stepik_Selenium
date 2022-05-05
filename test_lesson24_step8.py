import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

try:
    browser = webdriver.Chrome(desired_capabilities=caps)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    time.sleep(1)

    price = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
