#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import keyboard


def newBrowser(headless=True):
    service = Service('/usr/local/bin/geckodriver')
    options = Options()
    options.page_load_strategy = 'normal'
    if headless == True:
        options.add_argument("--headless")

    return webdriver.Firefox(
        service=service,
        options=options
    )


def main():
    browser = newBrowser(headless=False)
    print('Starting..')

    browser.get('https://www.livechat.com/typing-speed-test/#/')
    browser.implicitly_wait(10)

    text_field = WebDriverWait(browser, 5, poll_frequency=1).until(
        ec.visibility_of_element_located(
            (By.CLASS_NAME, 'tst-input-wrapper')
        )
    )

    previous_input = ""
    while True:

        if previous_input != text_field.get_attribute('innerText'):
            previous_input = text_field.get_attribute('innerText')
            print("text field", previous_input)

            current_word = browser.find_element(
                By.CSS_SELECTOR, 'div.tst-input > div:nth-child(2) > span.u-pl-0.u-pr-2xs'
            ).get_attribute('innerText')

            for i in range(len(current_word)):
                print(current_word[i])
                keyboard.press_and_release(current_word[i])

            keyboard.press_and_release("space")


if __name__ == '__main__':
    main()
