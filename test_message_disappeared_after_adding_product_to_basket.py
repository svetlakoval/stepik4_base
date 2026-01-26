# test_product_page.py

import pytest
from selenium import webdriver
from pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket():
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)
    page.open()  # открываем страницу 
    page.add_product_to_basket()  # добавляем в корзину
    page.success_message_should_disappear() #элемент присутствует на странице и должен исчезнуть
    browser.quit()