#Для запуска
#python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_smoke_labirint.py
import pytest
import time
import pyautogui
from pages.labirint import MainPage


def test_check_main_search(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()

    assert page.products_titles.count() == 60


def test_check_massage_button(web_browser):

    page = MainPage(web_browser)

    page.massage_run_button.click()

    title = page.forma.get_text()
    title = ''.join(title)

    assert title == 'Полный доступ к Лабиринту'


def test_check_massage_button_pop_up(web_browser):

    page = MainPage(web_browser)

    page.massage_run_button.hover()

    assert page.massage_pop_up_window.get_text() == 'У вас пока нет сообщений!'


def test_check_myLab_button(web_browser):

    page = MainPage(web_browser)

    page.myLab_run_button.click()

    title = page.forma.get_text()
    title = ''.join(title)

    assert title == 'Полный доступ к Лабиринту'


def test_check_myLab_button_discount(web_browser):

    page = MainPage(web_browser)

    page.myLab_run_button.hover()
    page.myLab_discount_button.click()

    assert page.new_title.get_text() == 'Накопительная скидка от 5% до 15%'


def test_check_favorites_button_full(web_browser):

        page = MainPage(web_browser)

        page.search = 'Русский язык'
        page.search_run_button.click()
        page.favorites_button.click()

        title = page.favorites_full.get_text()
        title = ''.join(title)
        assert title == '1'


def test_check_favorites_button_full_img(web_browser):

        page = MainPage(web_browser)

        page.search = 'Русский язык'
        page.search_run_button.click()
        page.favorites_button.click()
        page.refresh()
        page.favorites_button.hover()

        assert page.favorites_pop_up_window.get_attribute('src') != ''


def test_check_favorites_button_run(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.favorites_button.click()
    page.favorites_button_run.click()

    assert page.favorites_products_titles.count() == 1

def test_check_basket_full(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.basket_button.click()

    title = page.basket_full.get_text()
    title = ''.join(title)
    assert title == '1'


def test_check_favorites_button_clean(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.favorites_button.click()
    page.favorites_button.click()
    page.favorites_button_clean.click()

    title = page.favorites_full.get_text()
    title = ''.join(title)
    assert title == '0'


def test_check_basket_run(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.basket_button.click()
    page.basket_button_run.click()

    assert page.basket_products_titles.get_text() == '1'


def test_check_basket_button_clean(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.basket_button.click()
    page.basket_button_run.click()
    page.basket_button_clean.click()

    title = page.basket_title.get_text()
    title = ''.join(title)
    assert title == 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?'


def test_check_basket_button_return(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.basket_button.click()
    page.basket_button_run.click()
    page.basket_button_clean.click()
    page.basket_button_return.click()

    assert page.basket_products_titles.get_text() == '1'


def test_check_delivery_button_run(web_browser):

    page = MainPage(web_browser)

    page.delivery_button_run.click()

    assert page.delivery_title.get_text() == 'Курьерская доставка Л-Пост, г. Санкт-Петербург'


def test_check_certificate_button_run15(web_browser):

    page = MainPage(web_browser)

    page.certificate_button_run.click()

    assert page.certificate_title.count() == 8


def test_check_rating_button_run(web_browser):

    page = MainPage(web_browser)

    page.rating_button_run.click()

    assert page.rating_title.get_text() == '1 000 книг'


def test_check_new_button_run(web_browser):

    page = MainPage(web_browser)

    page.new_button_run.click()

    assert page.new_title.get_text() == 'Новые книги'


def test_check_sale_button_run(web_browser):

    page = MainPage(web_browser)

    page.sale_button_run.click()

    assert page.sale_title.get_text() == 'Все акции сегодня'


def test_check_button_8_800_600_95_25(web_browser):

    page = MainPage(web_browser)

    page.button_8_800_600_95_25.click()

    assert page.button_conect.get_text() == 'Соединить с оператором'


def test_check_button_contacts(web_browser):

    page = MainPage(web_browser)

    page.button_contacts.click()

    assert page.new_title.get_text() == 'Контакты'


def test_check_button_support(web_browser):

    page = MainPage(web_browser)

    page.button_support.click()

    assert page.support_title.get_text() == 'Публичные вопросы'


def test_check_button_pickup(web_browser):

    page = MainPage(web_browser)

    page.button_pickup.click()

    assert page.pickup_title.get_text() == 'Доставка'


def test_check_button_pickup_item_selection(web_browser):

    page = MainPage(web_browser)

    page.button_pickup.click()
    page.field_pickup = 'Невский проспект'
    page.pickup_item.click()

    assert page.ymaps.get_text() == 'Санкт-Петербург, ул. Думская, д. 4'


def test_check_button_social_network_vk(web_browser):

    page = MainPage(web_browser)

    page.button_social_network.hover()

    assert page.button_social_network_vk.is_clickable()


def test_check_button_social_network_yt(web_browser):

    page = MainPage(web_browser)

    page.button_social_network.hover()

    assert page.button_social_network_yt.is_clickable()


def test_check_button_book1(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.bil_book.hover()

    assert page.bil_book_menu1.get_text() == 'Все книги жанра'
    assert page.bil_book_menu2.get_text() == 'Билингвы'
    assert page.bil_book_menu3.get_text() == 'Литература на иностранном языке'
    assert page.bil_book_menu4.get_text() == 'Литература на иностранном языке для детей'


def test_check_button_book2(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.bil_book.hover()
    page.bil_book_menu1.click()

    assert page.new_title.get_text() == 'Билингвы и книги на иностранных языках'


def test_check_button_book3(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.bil_book.hover()
    page.bil_book_menu2.click()

    assert page.new_title.get_text() == 'Билингвы'


def test_check_button_book4(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.bil_book.hover()
    page.bil_book_menu3.click()

    assert page.new_title.get_text() == 'Литература на иностранном языке'


def test_check_button_book5(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.bil_book.hover()
    page.bil_book_menu4.click()

    assert page.new_title.get_text() == 'Литература на иностранном языке для детей'


def test_check_button_book6(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.all_books.click()

    assert page.new_title.get_text() == 'Книги'


def test_check_button_book7(web_browser):

    page = MainPage(web_browser)

    page.button_book.hover()
    page.periodicals.click()

    assert page.new_title.get_text() == 'Периодические издания'


def test_check_button_main(web_browser):

    page = MainPage(web_browser)

    page.button_main.click()

    assert page.new_title.get_text() == 'Главные книги 2022'


def test_check_menu_button_school(web_browser):

    page = MainPage(web_browser)

    page.button_school.hover()

    assert page.school_menu.get_text() == 'Основные предметы'


def test_check_menu_button_toys1(web_browser):

    page = MainPage(web_browser)

    page.button_toys.hover()
    page.toys_items_1.click()

    assert page.new_title.get_text() == 'Игры и игрушки'


def test_check_menu_button_toys2(web_browser):

    page = MainPage(web_browser)

    page.button_toys.hover()
    page.toys_items_3.hover()
    page.toys_items_3_puzzle.click()

    assert page.new_title.get_text() == 'Головоломки'


def test_check_menu_button_toys3(web_browser):

    page = MainPage(web_browser)

    page.button_toys.hover()
    page.toys_items_3.hover()
    page.toys_items_3_child_souv.click()

    assert page.new_title.get_text() == 'Детские сувениры'


def test_check_menu_button_stationery1(web_browser):

    page = MainPage(web_browser)

    page.button_stationery.hover()
    page.stationery_items_1.click()

    assert page.new_title.get_text() == 'Канцелярские товары'


def test_check_menu_button_stationery2(web_browser):

    page = MainPage(web_browser)

    page.button_stationery.hover()
    page.stationery_items_3_globes.click()

    assert page.new_title.get_text() == 'Глобусы'


def test_check_menu_button_more1(web_browser):

    page = MainPage(web_browser)

    page.button_more.hover()
    page.more_items_1_cd_dvd.click()

    assert page.new_title.get_text() == 'Мультимедиа'


def test_check_menu_button_more2(web_browser):

    page = MainPage(web_browser)

    page.button_more.hover()
    page.more_items_2_souvenirs.click()

    assert page.new_title.get_text() == 'Сувениры'


def test_check_menu_button_more3(web_browser):

    page = MainPage(web_browser)

    page.button_more.hover()
    page.more_items_3.click()

    assert page.new_title.get_text() == 'Журнальный лабиринт'


def test_check_menu_button_more4(web_browser):

    page = MainPage(web_browser)

    page.button_more.hover()
    page.more_items_4.click()

    assert page.new_title.get_text() == 'Товары для дома'


def test_check_menu_button_club(web_browser):

    page = MainPage(web_browser)

    page.button_club.hover()
    page.littest.click()

    assert page.new_title.get_text() == 'Литературные тесты'


def test_check_change_city(web_browser):

    page = MainPage(web_browser)

    page.button_change_city.click()
    page.city_name = 'Москв'
    page.new_city_name.click()

    assert page.button_change_city.get_text() == 'Москва'


def test_check_logo33(web_browser):

    page = MainPage(web_browser)

    page.delivery_button_run.click()
    page.logo.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


def test_scroll_page34(web_browser):

    page = MainPage(web_browser)
    page.search = 'Русский язык'
    page.search_run_button.click()
    page.page_num_3.scroll_to_element()
    assert page.page_num_3.is_clickable()
    page.page_num_3.highlight_and_make_screenshot('scrolling.png')


def test_search_product_adventure_error(web_browser):

    page = MainPage(web_browser)

    page.search = 'Heccrbq zpsr'
    page.search_run_button.click()

    for title in page.title_search_error.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Русский язык' or 'русккий язык' in title(), msg


def test_check_sort_by_price(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.button_sort.click()
    page.button_sort_preice.click()
    page.wait_page_loaded()
    price1 = page.products_price1.get_text()
    price2 = page.products_price2.get_text()
    price3 = page.products_price3.get_text()

    assert (price1 <= price2)and(price2 <= price3)


def test_check_button_more_action(web_browser):

    page = MainPage(web_browser)

    page.button_more_action.click()
    page.button_add_to_compare .click()
    page.button_add_to_compare.click()

    assert page.new_title.get_text() == 'Сравнение товаров'


def test_check_field_email_error(web_browser):

    page = MainPage(web_browser)

    page.field_email = '1111'
    page.button_coupon.click()

    assert page.massage_under_the_field_email.get_text() == 'Укажите почту'


def test_visible_block_icons(web_browser):

    page = MainPage(web_browser)
    assert page.block_icons.is_visible()


def test_visible_logo(web_browser):

    page = MainPage(web_browser)
    assert page.logo.is_visible()


def test_check_pagination_number_two(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.pagination_number_two.click()

    assert page.pagination_number_two_selected.is_visible()


def test_check_pagination_next(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.pagination_next.click()

    assert page.pagination_number_two_selected.is_visible()


def test_check_filter_price(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.button_filter_price.click()
    page.field_price_min = '100'
    page.field_price_max = '150'
    page.button_show1.hover()
    assert page.button_show1.is_clickable()


def test_check_filter_paper_book_check_box(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.button_all_filters.click()
    page.paper_book_check_box.click()
    page.button_show2.click()

    assert page.filter_book_check_box.get_text() != 'Бумажные книги'


def test_check_filter_other_goods(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.button_all_filters.click()
    page.other_goods_check_box.click()
    page.button_show2.click()

    assert page.filter_other_goods.get_text() != 'Прочите товары'


def test_photo_product(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()

    assert page.products_titles .get_attribute('src') != ''


def test_check_pre_order(web_browser):

    page = MainPage(web_browser)

    page.search = 'Русский язык'
    page.search_run_button.click()
    page.button_all_filters.click()
    page.filtel_Availability.click()
    page.filtel_Availability.click()
    page.Availability_check_box.click()
    page.wait_check_box.click()
    page.no_sale_check_box.click()
    page.button_show2.click()

    assert page.button_pre_order.get_text() == 'ПРЕДЗАКАЗ'

