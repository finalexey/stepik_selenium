from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    current_window = browser.current_window_handle
    button1 = browser.find_element_by_class_name("btn")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_class_name("btn")
    button2.click()
    time.sleep(2)

    alert2 = browser.switch_to.alert
    alert2_text = alert2.text
    print(alert2_text.split(": ")[-1])


finally:
    browser.quit()
