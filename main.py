from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import random
import time


class Form:
    __instance__ = None

    def __init__(self):
        self.url = 'https://docs.google.com/forms/d/*********'
        # radio button
        # self.question_holder_css_selector = '(//span[@role="presentation"])'
        self.question_holder_css_selector = '//span[@role="presentation"]'
        self.radio_button_class_name = '//div[@role=\'radio\']'
        # submit button
        self.submit_button_class_name = '//span[text()=\'提交\' or text()=\'Submit\']'

        if Form.__instance__ == None:
            Form.__instance__ = self

    def get_instance():
        if Form.__instance__ == None:
            Form()
        return Form.__instance__


def initialize():
    target_form = Form.get_instance()
    service = Service(executable_path=".\\driver\\chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get(target_form.url)
    return driver


def assert_correct_page(driver):  # check the form title
    assert "" in driver.title


def fill_username(driver, name):  # fill username
    name_input = driver.find_element(By.TAG_NAME, 'input')
    name_input.send_keys(name)


def fill_options(driver):  # randomly fill radio button
    target_form = Form.get_instance()
    css_selector_holder = target_form.question_holder_css_selector
    button_class_name = target_form.radio_button_class_name
    counter = []

    content_holders = driver.find_elements(By.XPATH, css_selector_holder)
    i = 0
    for holder in content_holders:
        if i == 0:
            print(holder)
            # time.sleep(0.2)
            buttons = holder.find_elements(By.XPATH, '.' + button_class_name)
            # this"." is use for query element in holder
            # time.sleep(0.2)
            random.choice(buttons).click()
            i += 1
        if i < 4:
            i += 1
        else:
            print(holder)
            # time.sleep(0.2)
            buttons = holder.find_elements(By.XPATH, '.' + button_class_name)
            # time.sleep(0.2)
            random.choice(buttons).click()


def click_submit(driver):  # click the submit button
    # class_name = 'quantumWizButtonPaperbuttonLabel'
    class_name = Form.get_instance().submit_button_class_name

    button = driver.find_element(By.XPATH, class_name)
    button.click()


def read_names_from_file():  # read names from csv
    names = []
    with open('names.csv') as f:
        names = [row.split(',')[0] for row in f]
    return names


def fill_form(driver):  # select action what will run
    # fill_username(driver, name)
    fill_options(driver)
    # click_submit(driver)


def open_new_form(driver):  # open a new form
    target_form = Form.get_instance()
    driver.get(target_form.url)


def main():
    driver = initialize()
    # names = read_names_from_file()

    # assert_correct_page(driver)

    for i in range(1):  # fill form ? times
        try:
            # name = random.choice(names)
            # time.sleep(1)
            fill_form(driver)
            print(f'execute {i + 1} successful')
            # time.sleep(2)
            input()
            open_new_form(driver)
        except Exception as e:
            print(f'execute {i + 1} failure')
            print(e)


if __name__ == '__main__':
    main()
