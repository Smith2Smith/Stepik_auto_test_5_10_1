#test_MANUALtestRegUser1.py
#5_10_1_2

import pytest
from selenium import webdriver

def test_MANUALtestRegUser1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ru/")
        browser.find_element_by_css_selector("#login_link").click()
        browser.find_element_by_css_selector("#id_registration-email").send_keys("rr25700112222ryhg67ff4432@sdfgh.dfgh")
        browser.find_element_by_css_selector("#id_registration-password1").send_keys("qqqaaazzzQQQAAAZZZ")
        browser.find_element_by_css_selector("#id_registration-password2").send_keys("qqqaaazzzQQQAAAZZZ")
        browser.find_element_by_css_selector("[name ='registration_submit']").click()
        browser.find_element_by_css_selector("#logout_link").click()
    finally:
        browser.quit()

#