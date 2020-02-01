from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_1 = browser.find_element_by_id("num1")
    x_2 = browser.find_element_by_id("num2")
    num1 = x_1.text
    num2 = x_2.text

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(num1) + int(num2)))
    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(5)
finally:
    browser.quit()
