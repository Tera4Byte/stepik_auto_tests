import time, math
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/math.html'

try:
    service = Service(executable_path='C:\chromedriver\chromedriver.exe')
    browser = wd.Chrome(service=service)
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.form-check.form-radio-custom > label').click()
    browser.find_element(By.CSS_SELECTOR, "button[type='Submit']").click()

except Exception as ex: print(ex)
finally: time.sleep(8); browser.quit()