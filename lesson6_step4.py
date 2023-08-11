import time

from selenium import webdriver
import datetime

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def fill_required():
    elements = []
    elements.append(browser.find_element(By.CSS_SELECTOR,
        "div.first_block input.first"))
    elements.append(browser.find_element(By.CSS_SELECTOR,
        "div.first_block input.second"))
    elements.append(browser.find_element(By.CSS_SELECTOR,
        "div.first_block input.third"))
    for element in elements:
        element.send_keys("required")


def fill_non_required():
    elements = browser.find_element(By.CSS_SELECTOR, "div.second_block input.first")
    for element in elements:
        element.send_keys("non required")


def test1():
    fill_required()


def test2():
    fill_required()
    fill_non_required()


def test3():
    fill_non_required()


functions = [test1, test2, test3]
try:
    browser = webdriver.Chrome(service=Service(executable_path='C:\chromedriver\chromedriver.exe'))
    for i in range(len(functions)):
        print("[test][", i, "][", datetime.datetime.now(), "]")
        browser.get("http://suninjuly.github.io/registration2.html")
        functions[i]()

        button = browser.find_element(By.CSS_SELECTOR,"button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        print(welcome_text)
        if i == 2:
            assert "Поздравляем! Вы успешно зарегистрировались!" != welcome_text
        if i != 2:
            assert "Поздравляем! Вы успешно зарегистрировались!" == welcome_text
        print("[success][", i, "]")

except Exception as ex:
    print(ex)

finally:
    time.sleep(4)
    browser.quit()