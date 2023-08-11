from math import log, sin
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec


class Solution:
    def __init__(self, link):
        self.__link = link

    def __send_form(self):
        with Chrome(service=Service(executable_path='C:\chromedriver\chromedriver.exe')) as browser:
            browser.get(self.__link)

            def __check_price():
                book_button = browser.find_element(By.ID, 'book')
                wdw(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '100'))
                book_button.click()

            def __get_x():
                x_element = int(browser.find_element(By.ID, 'input_value').text)
                return str(log(abs(12 * sin(x_element))))

            def __send_answer(value):
                browser.find_element(By.ID, 'answer').send_keys(value)

            def __button_click():
                wdw(browser, 2).until(ec.element_to_be_clickable(By.ID, 'submit'))

            try:
                __check_price()
                __send_answer(__get_x())
                __button_click()

            except: print('Ой-ой! Какая-то ошибка возникла...')

            finally:
                sleep(10)
                browser.quit()

    def start(self):
        self.__send_form()


if __name__ == '__main__':
    Solution('http://suninjuly.github.io/explicit_wait2.html').start()
