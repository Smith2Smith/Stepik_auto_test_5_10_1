#5_10_1
#test_items.py
import time

def test_is_button_basket_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)

    n = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert n > 0, "button add to basket not exists"
#