# test_product_page.py

import pytest
from selenium import webdriver
from pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_product_to_basket():
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)
    page.open()  # открываем страницу 
    page.should_not_be_success_message()
    browser.quit()