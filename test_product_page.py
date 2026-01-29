# test_product_page.py

import pytest
from selenium import webdriver
from pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link =" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket():
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)
    page.open()  # открываем страницу 
    page.should_not_be_success_message()
    page.add_product_to_basket()  # добавляем в корзину
    page.should_be_product_name_in_success_message() #Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
    page.should_be_basket_total_equal_product_price()
    #page.success_message_should_disappear() #элемент присутствует на странице и должен исчезнуть
    browser.quit()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()