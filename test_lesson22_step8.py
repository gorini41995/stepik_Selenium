import time
import os
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"  #  complete

try:
    browser = webdriver.Chrome(desired_capabilities=caps)
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    time.sleep(1)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("1")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("1")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("1")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')   # добавляем к этому пути имя файла

    file_upload = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    file_upload.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
