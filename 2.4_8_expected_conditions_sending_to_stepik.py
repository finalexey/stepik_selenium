import math
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SeleniumAnswer:
    def __init__(self, remote: Remote, step_link: str,
                 timeout: int = 3) -> None:
        self.link = step_link
        self.remote = remote
        self.timeout = timeout

    def send_answer(self, answer: str):
        def wait_textarea(remote: Remote):
            return remote.find_element_by_css_selector("textarea.textarea")

        def wait_textarea_enabled(remote: Remote):
            return remote.find_element_by_tag_name("textarea").is_enabled()

        def wait_correct(remote: Remote):
            return remote.find_element_by_class_name("correct")

        self.remote.get(self.link)
        WebDriverWait(self.remote, self.timeout).until(wait_textarea)

        try:
            self.remote.find_element_by_class_name("again-btn").click()
            WebDriverWait(self.remote, self.timeout).until(wait_textarea_enabled)
        except NoSuchElementException:
            pass

        self.remote.find_element_by_css_selector("textarea.textarea").send_keys(answer)
        self.remote.find_element_by_class_name("submit-submission").click()

        try:
            WebDriverWait(self.remote, self.timeout).until(wait_correct)
        except NoSuchElementException:
            return False


class SeleniumAuth:
    AUTH_LINK = "https://stepik.org/catalog?auth=login"

    def __init__(self,
                 username: str,
                 password: str,
                 remote: Remote,
                 timeout: int = 3) -> None:
        self.timeout = timeout
        self.username = username
        self.password = password
        self.remote = remote

    def auth(self):
        self.remote.get(self.AUTH_LINK)
        WebDriverWait(
            self.remote,
            self.timeout).until(lambda x: x.find_element_by_name("login"))
        auth_elems = "login", "password"
        self.remote.find_element_by_name(auth_elems[0]).send_keys(
            self.username)
        self.remote.find_element_by_name(auth_elems[1]).send_keys(
            self.password)
        self.remote.find_element_by_class_name("sign-form__btn").click()
        WebDriverWait(self.remote, self.timeout).until(
            lambda x: x.find_element_by_class_name("navbar__profile-img"))


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    ans = alert.text.split()[-1]
    print(ans)
    alert.accept()

    return ans


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    WebDriverWait(browser, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"),
                                                          "10000"))
    browser.find_element_by_id("book").click()
    WebDriverWait(browser,
                  3).until(lambda x: x.find_element_by_id("input_value"))
    browser.find_element_by_id("answer").send_keys(
        calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    answer = print_answer(browser)

    SeleniumAuth(os.getenv("login"), os.getenv("password"),
                        browser).auth()
    SeleniumAnswer(
        browser,
        "https://stepik.org/lesson/181384/step/8?unit=156009").send_answer(
            answer)
finally:
    browser.quit()
