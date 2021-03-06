from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = int(x_element.get_attribute("valuex"))
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_class_name("btn")
    time.sleep(2)
    button.click()
    time.sleep(5)

finally:
    browser.quit()
