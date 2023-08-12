import os
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
            data = ['Иванов', 'Иван', 'example@host.domain']

            try:
                elements = browser.find_elements(By.TAG_NAME, 'input')
                for element in elements:
                    var = [element.send_keys(data[1]) if 'first' in element.accessible_name else
                           element.send_keys(data[0]) if 'last' in element.accessible_name else
                           element.send_keys(data[2]) if 'email' in element.accessible_name else
                           element.send_keys(os.path.join('C:\\Users\\artem\\OneDrive\\Desktop',
                                                          'text.txt')) if 'file to' in element.accessible_name else
                           print('>>> Произошла ошибка!')]

                browser.find_element(By.CSS_SELECTOR, 'body > div > form > button').click()

            except Exception as ex:
                print(ex)

            finally:
                sleep(10)
                browser.quit()
    def start(self):
        self.__send_form()


if __name__ == '__main__':
    s = Solution('http://suninjuly.github.io/file_input.html')
    s.start()