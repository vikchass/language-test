import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMainPage:
        def test_should_find_button(self, browser):
                browser.get(link)
                time.sleep(30)
                button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
                assert button.is_displayed(), \
                        'Кнопка добавления товара в корзину отсутсвует'




