from selenium.webdriver.common.by import By

class MainPageLocators(object):

    Loc_search_line = (By.XPATH, '//*[@id="edtSearch"]')
    Loc_search_button = (By.XPATH, '//*[@id="btnSearch"]')
    Loc_login = (By.XPATH, '//*[@id="lblLogin"]')
    Loc_login_iframe = (By.ID, 'loginIframe')
    Loc_login_name = (By.ID, 'userName')
    Loc_login_password = (By.ID, 'password')
    Loc_login_button = (By.XPATH, '//*[@id="btnLogin"]')
    Loc_first_item = (By.CSS_SELECTOR, 'span#lblNumberItem')
    Loc_sidebar = (By.ID, 'left')
    Loc_sidebar_categorie = (By.ID, 'litp18890188')
    Loc_sidebar_sub_categorie = (By.CLASS_NAME, 'item fullList')
    Loc_apple = (By.CLASS_NAME, 'alzaico-apple')
    Loc_googleplay = (By.CLASS_NAME, 'alzaico-android')
    Loc_facebook = (By.CLASS_NAME, 'alzaico-facebook')
    Loc_instagram = (By.CLASS_NAME, 'alzaico-instagram')
    Loc_youtube = (By.CLASS_NAME, 'alzaico-youtube')
    Loc_twitter = (By.CLASS_NAME, 'alzaico-twitter')
    Loc_chat = (By.CSS_SELECTOR, 'div#chat-open-button')
    Loc_how_to_by = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul > li > a')
    Loc_orders = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(2) > li > a')
    Loc_about = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(3) > li > a')
    Loc_firms = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(4) > li > a')
    Loc_affiliate = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(4) > li:nth-of-type(2) > a')
    Loc_students = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(4) > li:nth-of-type(3) > a')
    Loc_vip = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(4) > li:nth-of-type(4) > a')
    Loc_marketplace = (By.CSS_SELECTOR, 'div#footerContent > div:nth-of-type(2) > ul:nth-of-type(4) > li:nth-of-type(5) > a')
    Loc_myalza = (By.CSS_SELECTOR, 'a#lblMujUcet')
    Loc_register = (By.ID, 'registerLink')

class SearchResultsPageLocators(object):

    Loc_buy = (By.CLASS_NAME, 'btnk1')
    Loc_count = (By.CSS_SELECTOR, 'span#lblNumberItem')
    Loc_search_name = (By.CSS_SELECTOR, 'div#h1c > h1')
    Loc_item_cards = (By.CSS_SELECTOR, 'div#boxes > div')
    Loc_first_item = (By.CSS_SELECTOR, 'div#boxes > div > div > div:nth-of-type(2) > a')
    Loc_max_price = (By.CSS_SELECTOR, 'a#ui-id-3')
    Loc_min_price = (By.CSS_SELECTOR, 'a#ui-id-4')
    Loc_score = (By.CSS_SELECTOR, 'a#ui-id-5')
    Loc_score_stars = (By.CSS_SELECTOR, 'a#ui-id-5')
    Loc_top = (By.CSS_SELECTOR, 'a#ui-id-2')
    Loc_price = (By.CSS_SELECTOR, 'div#boxes > div > div:nth-of-type(2) > div > div > span:nth-of-type(2)')
    Loc_sidebar_filter_price = (By.CSS_SELECTOR, 'div#parametrization > div > div')
    Loc_sidebar_filter_available = (By.CSS_SELECTOR, 'div#parametrization > div > div:nth-of-type(2) > div > div')
    Loc_sidebar_filter_lable = (By.CSS_SELECTOR, 'div#producers > div')
    Loc_sidebar_filter_stav = (By.CSS_SELECTOR, 'div#parametrization > div > div:nth-of-type(2) > div:nth-of-type(2)')
    Loc_sidebar_filter_type = (By.CSS_SELECTOR, 'div#topped-parameter-1 > div')


class CartPageLocators(object):
    Cart_btn = (By.ID, 'basketLink')
    Cart_item_text = (By.CSS_SELECTOR, 'td#order-item-381761391 > div > div > a')
    Cart_price = (By.CSS_SELECTOR, 'div#o1basket > table > tbody > tr > td:nth-of-type(6)')
    Cart_sumprice = (By.CSS_SELECTOR, 'td#order-item-382154264 > div > div > a')
    Cart_item_name = (By.CSS_SELECTOR, 'div#sum > div > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2) > span')
    Cart_item_count = (By.CSS_SELECTOR, 'div#r382154264 > div')
    Cart_item_countup = (By.CSS_SELECTOR, 'div#r382154264 > div:nth-of-type(2)')
    Cart_item_countdown = (By.CSS_SELECTOR, 'div#r382154264 > div:nth-of-type(3)')
    Cart_exit = (By.CSS_SELECTOR, 'div#orderpage > div:nth-of-type(3) > div:nth-of-type(10) > a > span')
    Cart_next = (By.CSS_SELECTOR, 'div#blockBtnRight > a')
    Cart_del = (By.CSS_SELECTOR, 'div#d382154264 > div > ul > li > span')
    Cart_del_btn = (By.CSS_SELECTOR, 'div#d382154264 > div > ul > li > span')

class UserPageLocators(object):
    Loc_unlogin = (By.CSS_SELECTOR, '#lblSignOut')

class Item_card(object):
    Loc_name = (By.CSS_SELECTOR, 'div#h1c > h1')
    Loc_parametrs = (By.CSS_SELECTOR, 'a#hlTabParameters')
    Loc_foto = (By.CSS_SELECTOR, 'a#tabFoto')
    Loc_fotos = (By.CSS_SELECTOR, 'a#tabFoto')
    Loc_score = (By.CSS_SELECTOR, 'div#popis > div > div > div:nth-of-type(2) > div > div > div')
    Loc_recence = (By.CSS_SELECTOR, 'a#reviews-tab')#!!!!
    Loc_poradna = (By.CSS_SELECTOR, 'a#hlTabDiscussionPosts')#!!!!
    Loc_price = (By.CSS_SELECTOR, 'table#prices > tbody > tr:nth-of-type(2) > td > div > div > div > div:nth-of-type(2) > span')
    Loc_main_foto = (By.CSS_SELECTOR, 'img#imgMain')
    Loc_home = (By.CSS_SELECTOR, 'a#popisx')
    Loc_main_info = (By.CSS_SELECTOR, 'div#popis')
    Loc_parametrs_info = (By.CSS_SELECTOR, 'div#parametry')
    Loc_recence_info = (By.CSS_SELECTOR, 'div#recenze > div > div > div:nth-of-type(2)')
    Loc_poradna_info = (By.CSS_SELECTOR, 'div#discussionPosts')
