from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('dsfsdfs')

    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('dsfsdfs')

    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('dsfsdfs')

    infile = browser.find_element_by_id('file')
    infile.send_keys(file_path)

    button = browser.find_element_by_class_name("btn")
    button.click()
    time.sleep(3)
finally:
    browser.quit()
