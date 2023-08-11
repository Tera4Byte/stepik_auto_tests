import math
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Solution:
    def __init__(self, link):
        self.__link = link

    def __send_form(self):
        with Chrome(service=Service(executable_path='C:\chromedriver\chromedriver.exe')) as browser:
            browser.get(self.__link)

            def __buttonClick():
                browser.find_element(By.XPATH, '//button[contains(@type, "submit")]').click()

            def __confirm(variant):
                confirm = browser.switch_to.alert

                var = [confirm.accept() if variant == 'yes' else confirm.dismiss()]

            def __get_x():
                x_element = int(browser.find_element(By.ID, 'input_value').text)
                return str(math.log(abs(12*math.sin(x_element))))

            def __send_answer(value):
                browser.find_element(By.ID, 'answer').send_keys(value)

            try:
                __buttonClick()
                __confirm('yes')
                __send_answer(__get_x())
                __buttonClick()

            except Exception as ex: print(ex)

            finally:
                sleep(10)
                browser.quit()

    def start(self):
        self.__send_form()


if __name__ == '__main__':
    Solution('http://suninjuly.github.io/alert_accept.html').start()
