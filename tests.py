import pytest
import page
from conftest import browser





# test 1
def test_login_sucsess(browser):
   site = page.MainPage(browser)
   site.login_fill_and_click('putinov.tb@gmail.com', 'skillfactory')
   assert pytest.driver.find_element_by_id('lblUser').text == "Moje Alza - Timofey Bystrov"


# test 2
def test_search_item():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   assert site.is_search_results_found('usb')


# test 3
def test_search_item_count():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   assert site.is_search_results_count() > 0


# test 4
def test_add_item_to_cart():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   sucsess_atention = pytest.driver.find_element_by_class_name('productInfo__texts__message').text
   assert sucsess_atention == 'Zboží bylo přidáno do košíku'

# test 5
def test_unlogin():
   site = page.MainPage(browser)
   site.login_fill_and_click('putinov.tb@gmail.com', 'skillfactory')
   site.unlogin()
   unlogin = pytest.driver.find_element_by_xpath('//*[@id="lblLogin"]').text
   assert unlogin == 'Přihlásit'

# test 6
def test_item_card_name():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   name = site.get_card_name()
   assert name != ''


# test 7
def test_item_card_foto():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   foto = site.get_main_foto()
   assert foto.get_attribute('src') != ''


# test 8
def item_card_fotos():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   fotos = site.get_fotos()
   for i in range(len(fotos)):
      assert fotos[i].get_attribute('src') != ''


# test 9
def test_item_card_description():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   desc = site.get_main_info()
   assert desc != ''


# test 10
def test_item_card_params():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   param = site.get_params()
   assert param != ''


# test 11
def test_item_card_cena():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   cena = site.get_price()
   assert cena != ''


# test 12
def test_item_card_recenze():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   recenz = site.get_recence()
   assert recenz != ''


# test 13
def test_item_card_poradna():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   porad = site.get_poradna()
   assert porad != ''


# test 14
def item_card_score():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   score = site.get_score_card().text
   assert score != ''


# test 15
def test_item_card_home():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   info1 = site.get_main_info()
   site.get_poradna()
   site.go_home_card()
   info2 = site.get_main_info()
   assert info1 == info2


# test 16
def test_cart_items_price():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   prices = site.get_single_prices_cart()
   for i in range(len(prices)):
      assert prices[i] != ''


# test 17
def test_enter_cart():
   site = page.MainPage(browser)
   site.enter_cart()
   text = pytest.driver.find_element_by_css_selector('div#blocke > div > span').text
   assert text == 'Jsem tak prázdný...'




# test 18
def test_cart_items_names():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   names = site.get_single_prices_cart()
   for i in range(len(names)):
      assert names[i] != ''


# test 19
def test_cart_sum_price_correct():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   summ = site.get_sum_price_cart().text
   summ = summ[:-3]
   summ = summ.split(' ')
   summ = summ[0] + summ[1]
   summ =int(summ)
   summ_check = site.get_single_prices_cart()
   for i in range(len(summ_check)):
      summ_check[i] = summ_check[:-3]
      summ_check_m = summ_check[i].split(' ')
      summ_check_m[i] = int(summ_check_m[0] + summ_check_m[1])
   while i in range(len(summ_check_m)):
      summ_check = summ_check_m[i] + summ_check_m[i+1]
   assert summ == summ_check


# test 20
def test_cart_exit():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.enter_item_card()
   before = site.get_card_name().text
   site.enter_cart()
   site.exit_cart()
   after = site.get_card_name().text
   assert before == after



# test 21
def test_cart_delete_item():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   site.cart_delete_item()
   text = pytest.driver.find_element_by_css_selector('div#blocke > div > span').text
   assert text == 'Jsem tak prázdný...'


# test 22
def test_cart_item_countup():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   before = site.get_cart_item_count()
   site.cart_item_count_up().click()
   after = site.get_cart_item_count()
   assert before < after


# test 23
def test_cart_item_countdown():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.add_item_to_cart()
   site.enter_cart()
   before = site.get_cart_item_count()
   site.cart_item_count_up().click()
   after = site.get_cart_item_count()
   assert before > after


# test 24
def test_result_filter_max_price():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.go_to_serch_max_price().click()
   price1 = site.get_serch_prices()[1].text
   price2 = site.get_serch_prices()[2].text
   price1 = int(price1[:-2])
   price2 = int(price2[:-2])
   assert price1 >= price2




# test 25
def test_result_filter_min_price():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   site.go_to_serch_min_price().click()
   price1 = site.get_serch_prices()[1].text
   price2 = site.get_serch_prices()[2].text
   price1 = int(price1[:-2])
   price2 = int(price2[:-2])
   assert price1 <= price2



# test 26
def test_result_filterside_price():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   price = site.get_search_sidebar_price()
   assert price != ''


# test 27
def test_result_filterside_available():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   available = site.get_search_sidebar_available()
   assert available != ''



# test 28
def test_result_filterside_lable():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   lable = site.get_search_sidebar_lable()
   assert lable != ''



# test 29
def test_result_filterside_stav():
   site = page.MainPage(browser)
   site.enter_search_line('usb')
   site.click_search_button()
   stav = site.get_search_sidebar_stav()
   assert stav != ''



# test 30
def test_leftside_menu():
   site = page.MainPage(browser)
   menu = site.get_leftside_menu()
   assert menu != ''



# test 31
def test_leftside_menu_categories():
   site = page.MainPage(browser)
   categories = site.get_leftside_menu()
   assert categories != ''


# test 32
def test_leftside_menu_sub_categories():
   site = page.MainPage(browser)
   subcategories = site.get_leftside_menu()
   assert subcategories != ''

# test 33
def test_aple_store_link():
   site = page.MainPage(browser)
   link = site.get_apple().get_attribute('href')
   assert link == 'https://apps.apple.com/cz/app/alza/id582287621?l=cs'

# test 34
def test_googleplay_link():
   site = page.MainPage(browser)
   link = site.get_googleplay().get_attribute('href')
   assert link == 'https://play.google.com/store/apps/details?id=cz.alza.eshop&feature=search_result#?t=W251bGwsMSwyLDEsImN6LmFsemEuZXNob3AiXQ..'

# test 35
def test_facebook_link():
   site = page.MainPage(browser)
   link = site.get_facebook().get_attribute('href')
   assert link == 'https://www.facebook.com/alza.cz/'

# test 36
def test_instagram_link():
   site = page.MainPage(browser)
   link = site.get_instagram().get_attribute('href')
   assert link == 'https://www.instagram.com/alza_czsk/'

# test 37
def test_youtube_link():
   site = page.MainPage(browser)
   link = site.get_youtube().get_attribute('href')
   assert link == 'https://www.youtube.com/channel/UC0wtqzWrBA5gL4Jr_QIQTgg'

# test 38
def test_twiter_link():
   site = page.MainPage(browser)
   link = site.get_twitter().get_attribute('href')
   assert link == 'https://twitter.com/Alzacz'

# test 39
def test_chat():
   site = page.MainPage(browser)
   site.get_chat()


# test 40
def test_how_to_by():
   site = page.MainPage(browser)
   site.get_how_to_by()
   text = pytest.driver.find_element_by_css_selector('div#articleContainer > article > header > div > h1').text
   assert text == 'Jak nakupovat na Alza.cz?'


# test 41
def test_your_order():
   site = page.MainPage(browser)
   site.get_orders()
   text = pytest.driver.find_element_by_css_selector('div#placeholderMain > div > span').text
   assert text == 'Zadejte číslo objednávky a zjistěte její stav'


# test 42
def test_about():
   site = page.MainPage(browser)
   site.get_about()
   text = pytest.driver.find_element_by_css_selector('div#h1c > h1').text
   assert text == 'O nás'


# test 43
def test_for_firms():
   site = page.MainPage(browser)
   site.get_firms()
   text = pytest.driver.find_element_by_css_selector('div#lp > header > div > h1').text
   assert text == 'Efektivní řešení firemních nákupů pro živnostníky, velké firmy i veřejný sektor'


# test 44
def test_affiliate():
   site = page.MainPage(browser)
   site.get_affiliate()
   text = pytest.driver.find_element_by_css_selector('html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > div > h1 > em').text
   assert text == 'Vydělávejte na internetu'


# test 45
def test_students():
   site = page.MainPage(browser)
   site.get_students()
   text = pytest.driver.find_element_by_css_selector('div#articleContainer > article > header > div > h1').text
   assert text == 'Alza pro studenty'


# test 46
def test_vip():
   site = page.MainPage(browser)
   site.get_vip()
   text = pytest.driver.find_element_by_css_selector('div#articlePage > article > header > div > h2').text
   assert text == 'Staňte se VIP zákazníkem'


# test 47
def test_marketplace():
   site = page.MainPage(browser)
   site.get_marketplace()
   text = pytest.driver.find_element_by_css_selector('html > body > nav > div > a > img').get_attribute('src')
   assert text != ''


# test 48
def test_myalza():
   site = page.MainPage(browser)
   site.get_myalza()
   text = pytest.driver.find_element_by_css_selector('div#h1c > h1').text
   assert text == 'Můj Účet'

# test 49
def test_myalza_login():
   site = page.MainPage(browser)
   site.login_fill_and_click('putinov.tb@gmail.com', 'skillfactory')
   site.get_myalza()
   text = pytest.driver.find_element_by_css_selector('div#alza-bo-orders > app-backoffice > app-order-list > div > div > div').text
   assert text == 'Nemáte žádné aktivní objednávky'


# test 50
#def test_new_user():