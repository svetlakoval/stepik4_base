# test_product_page.py

import pytest
from selenium import webdriver
from pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link =" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket():
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_product_name_in_success_message()
    page.should_be_basket_total_equal_product_price()
    browser.quit()