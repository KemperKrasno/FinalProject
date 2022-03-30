import pytest

from locators import MainPageLocators
from locators import SearchResultsPageLocators
from locators import CartPageLocators
from locators import UserPageLocators
from locators import Item_card

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def click_search_button(self):

        element = pytest.driver.find_element(*MainPageLocators.Loc_search_button)
        element.click()

    def enter_search_line(self, value):

        element = pytest.driver.find_element(*MainPageLocators.Loc_search_line)
        element.send_keys(value)


    def new_reg(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_login)
        element.click()
        pytest.driver.switch_to.frame(pytest.driver.find_element(*MainPageLocators.Loc_login_iframe))
        element = pytest.driver.find_element(*MainPageLocators.Loc_register)
        element.click()



    def login_fill_and_click(self, name, password):

        element = pytest.driver.find_element(*MainPageLocators.Loc_login)
        element.click()
        pytest.driver.switch_to.frame(pytest.driver.find_element(*MainPageLocators.Loc_login_iframe))
        element = pytest.driver.find_element(*MainPageLocators.Loc_login_name)
        element.send_keys(name)
        element = pytest.driver.find_element(*MainPageLocators.Loc_login_password)
        element.send_keys(password)
        element = pytest.driver.find_element(*MainPageLocators.Loc_login_button)
        element.click()


    def is_search_results_found(self, name):

        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_search_name)
        nameText = element.text
        itemText = nameText.split(' ')
        name in itemText

    def is_search_results_count(self):

        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_count)
        countText = element.text
        countParts = countText.split(' ')
        count = countParts[0] + countParts[1]
        countInt = int(count)
        return countInt

    def add_item_to_cart(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_buy)
        pytest.driver.execute_script("arguments[0].click();", element)


    def get_item_in_cart_text(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_item_text)
        return element.text


    def enter_cart(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_btn)
        pytest.driver.execute_script("arguments[0].click();", element)


    def enter_item_card(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_first_item)
        element.click()

    def get_card_name(self):
        element = pytest.driver.find_element(*Item_card.Loc_name)
        return element.text

    def get_main_info(self):
        element = pytest.driver.find_element(*Item_card.Loc_main_info)
        return element.text

    def get_main_foto(self):
        element = pytest.driver.find_element(*Item_card.Loc_main_foto)
        return element

    def get_fotos(self):
        element = pytest.driver.find_element(*Item_card.Loc_foto)
        pytest.driver.execute_script("arguments[0].click();", element)
        elements = pytest.driver.find_elements(*Item_card.Loc_fotos)
        return elements

    def get_recence(self):
        element = pytest.driver.find_element(*Item_card.Loc_recence)
        pytest.driver.execute_script("arguments[0].click();", element)
        element = pytest.driver.find_element(*Item_card.Loc_recence_info)
        return element.text

    def get_price(self):
        element = pytest.driver.find_element(*Item_card.Loc_price)
        return element

    def get_poradna(self):
        element = pytest.driver.find_element(*Item_card.Loc_poradna)
        pytest.driver.execute_script("arguments[0].click();", element)
        element = pytest.driver.find_element(*Item_card.Loc_poradna_info)
        return element.text

    def go_home_card(self):
        element = pytest.driver.find_element(*Item_card.Loc_home)
        pytest.driver.execute_script("arguments[0].click();", element)


    def get_params(self):
        element = pytest.driver.find_element(*Item_card.Loc_parametrs)
        pytest.driver.execute_script("arguments[0].click();", element)
        element = pytest.driver.find_element(*Item_card.Loc_parametrs_info)
        return element.text

    def get_score_card(self):
        element = pytest.driver.find_element(*Item_card.Loc_score)
        return element

    def get_serch_prices(self):
        elements = pytest.driver.find_elements(*SearchResultsPageLocators.Loc_price)
        return elements

    def go_to_serch_score(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_score)
        return element

    def go_to_serch_max_price(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_max_price)
        return element

    def go_to_serch_min_price(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_min_price)
        return element

    def get_sum_price_cart(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_price)
        price = element.text
        IntPrice = int(price)
        return IntPrice

    def get_single_prices_cart(self):
        elements = pytest.driver.find_elements(*CartPageLocators.Cart_price)
        return elements



    def cart_item_count_up(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_item_countup)
        pytest.driver.execute_script("arguments[0].click();", element)


    def cart_item_count_down(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_item_countdown)
        pytest.driver.execute_script("arguments[0].click();", element)


    def get_cart_item_count(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_item_count)
        return int(element.text)

    def cart_delete_item(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_del)
        element.click()
        element = pytest.driver.find_element(*CartPageLocators.Cart_del_btn)
        element.click()


    def exit_cart(self):
        element = pytest.driver.find_element(*CartPageLocators.Cart_exit)
        element.click()

    def get_search_sidebar_price(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_sidebar_filter_price)
        return element.text

    def get_search_sidebar_available(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_sidebar_filter_price)
        return element.text

    def get_search_sidebar_lable(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_sidebar_filter_price)
        return element.text

    def get_search_sidebar_stav(self):
        element = pytest.driver.find_element(*SearchResultsPageLocators.Loc_sidebar_filter_price)
        return element.text

    def get_leftside_menu(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_sidebar)
        return element.text

    def get_leftside_menu_categories(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_sidebar_categorie)
        return element.text

    def get_leftside_menu_subcategories(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_sidebar_sub_categorie)
        return element.text


    def unlogin(self):
        element = pytest.driver.find_element(*UserPageLocators.Loc_unlogin)
        element.click()

    def get_apple(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_apple)
        return element

    def get_googleplay(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_googleplay)
        return element

    def get_facebook(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_facebook)
        return element

    def get_instagram(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_instagram)
        return element

    def get_youtube(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_youtube)
        return element

    def get_twitter(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_twitter)
        return element

    def get_chat(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_chat)
        element.click()

    def get_how_to_by(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_how_to_by)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_orders(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_orders)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_about(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_about)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_firms(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_firms)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_affiliate(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_affiliate)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_students(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_students)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_vip(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_vip)
        pytest.driver.execute_script("arguments[0].click();", element)

    def get_marketplace(self):
        pytest.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = pytest.driver.find_element(*MainPageLocators.Loc_marketplace)
        pytest.driver.execute_script("arguments[0].click();", element)


    def get_myalza(self):
        element = pytest.driver.find_element(*MainPageLocators.Loc_myalza)
        element.click()

