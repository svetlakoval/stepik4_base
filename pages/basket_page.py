# pages/basket_page.py

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        """Проверяет, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_empty_basket_message(self):
        """Проверяет, что есть сообщение о пустой корзине"""
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"
        
        # Дополнительно можно проверить текст сообщения
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in message or "Ваша корзина пуста" in message, \
            f"Expected empty basket message, but got: {message}"