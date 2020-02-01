import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    if WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")):
        button1 = browser.find_element(By.ID, "book")
        button1.click()

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    alert2 = browser.switch_to.alert
    alert2_text = alert2.text
    print(alert2_text.split(": ")[-1])


finally:
    browser.quit()
