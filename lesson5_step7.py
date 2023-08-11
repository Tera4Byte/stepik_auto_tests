import time, operator
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

try:
    service = Service(executable_path='C:\chromedriver\chromedriver.exe')
    browser = wd.Chrome()
    browser.get(link)

    ops = {"+": operator.add}
    button = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]")

    numbers = [int(num.text) for num in browser.find_elements(By.XPATH, "//span[contains(@id, 'num')]")]
    symbol = browser.find_element(By.XPATH, '*//div/form/h2//span[3]').text

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(ops[symbol](numbers[0], numbers[1])))

    button.click()

except Exception as ex: print(ex)
finally: time.sleep(15); browser.quit()