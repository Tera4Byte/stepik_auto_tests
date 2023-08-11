import time, math
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/execute_script.html'

try:
    service = Service(executable_path='C:\chromedriver\chromedriver.exe')
    browser = wd.Chrome()
    browser.get(link)

    x = browser.find_element(By.XPATH, "//span[contains(@id, 'input_value')]").text

    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    robotsRule = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    button = browser.find_element(By.XPATH, "//button[contains(@type, 'submit')]")
    browser.execute_script("return arguments[0].scrollIntoView(true)", robotsRule)
    robotsRule.click(); time.sleep(1); button.click()

except Exception as ex: print(ex)
finally: time.sleep(15); browser.quit()