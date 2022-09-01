#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    search = WebElement(id='search-field')

    search_run_button = WebElement(xpath='//span[@class="b-header-b-search-e-btntxt"]')

    products_titles = ManyWebElements(xpath='//a[@class="product-title-link"]')
    products_titles_sale = ManyWebElements(xpath='//a[@class="card-label card-label_profit card-label_color-mid"]')

    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

    basket_button = WebElement(xpath='//a[@id="buy799777"]')

    basket_full = ManyWebElements(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

    massage_run_button = WebElement(xpath='(//a[@href="/cabinet/"])[1]')
    massage_pop_up_window = WebElement(xpath='//div[@class="b-menu-list-title font_regular"]')
    forma = ManyWebElements(xpath='//div[@class="js-auth__title new-auth__title"]')

    myLab_run_button = WebElement(xpath='(// a[@ data-sendto="authorize"])[2]')
    myLab_discount_button = WebElement(xpath=' (//span[@class="b-sub-menu-sub-title-m-small pointer-imp"])[3]')
    favorites_button = WebElement(xpath='//span[@class="header-sprite"]')
    favorites_pop_up_window = WebElement(xpath='//img[@class="book-img-cover b-suggests-b-sly-e-img"]')
    favorites_button_clean = WebElement(xpath='//span[@class="b-list-item-hover pointer"]')
    favorites_full = ManyWebElements(xpath='//span[@class="b-header-b-personal-e-icon-count-m-putorder basket-in-dreambox-a"]')
    favorites_button_run = WebElement(xpath='//span[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-putorder b-header-e-sprite-background"]')
    favorites_products_titles = ManyWebElements(xpath='//span[@class="product-title"]')

    basket_button_run = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]')
    basket_products_titles = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')
    basket_button_clean = WebElement(css_selector='.b-link-popup')
    basket_title = WebElement(xpath='//span[@class="g-alttext-small g-alttext-grey g-alttext-head"]')
    basket_button_return = WebElement(xpath='//a[@class="b-link-popup g-alttext-deepblue"]')

    delivery_button_run = WebElement(xpath='//a[@class="b-header-b-sec-menu-e-link"]')
    delivery_title = WebElement(xpath='//span[@id="jslikeurl14"]')

    certificate_button_run = WebElement(xpath='//a[@href="/top/certificates/"]')
    certificate_title = ManyWebElements(xpath='//span[@class="product-title"]')

    rating_button_run = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    rating_title = WebElement(xpath='//span[@class="navisort-head-text"]')

    new_button_run = WebElement(xpath='//a[@href="/novelty/"]')
    new_title = WebElement(xpath='//h1')

    sale_button_run = WebElement(xpath='//a[@href="/sale/"]')
    sale_title = WebElement(xpath='//a[@href="/actions/"]')

    button_8_800_600_95_25 = WebElement(xpath='(//a[@href="/contact/"])[3]')
    button_conect = WebElement(xpath='(//a[@class="btn btn-small btn-clear font_regular-btn"])[1]')

    button_contacts = WebElement(xpath='(//a[@class="b-header-b-sec-menu-e-link"])[6]')

    button_support = WebElement(xpath='(//a[@class="b-header-b-sec-menu-e-link"])[7]')
    support_title = WebElement(xpath='// a[ @class ="support-all active"]')

    button_pickup = WebElement(xpath='(//a[@class="b-header-b-sec-menu-e-link"])[8]')
    pickup_title = WebElement(xpath='//span[@class="delivery-map-wrapper__header-text-inline"]')
    field_pickup = WebElement(xpath='// input[@class ="delivery-serach-panel__input js-delivery-point-search-input"]')
    pickup_item = WebElement(xpath='//div[@data-address = "ул. Думская, д. 4 Невский Проспект Санкт-Петербург"]')
    ymaps = WebElement(xpath='//ymaps[@class="ymaps-2-1-79-balloon ymaps-2-1-79-balloon_layout_normal ymaps-2-1-79-balloon_to_top ymaps-2-1-79-i-custom-scroll"]//div[@class="delivery-point__address"]')

    button_book = WebElement(xpath='//a[@href="/books/"]')
    bil_book = WebElement(xpath='//span[@class="b-menu-list-title b-menu-list-title-first"]')
    bil_book_menu1 = WebElement(xpath='(//a[@href="/genres/965"])[2]')
    bil_book_menu2 = WebElement(xpath='//li[@class="b-menu-second-item"]//a[@href="/genres/2827"]')
    bil_book_menu3 = WebElement(xpath='//li[@class="b-menu-second-item"]//a[@href="/genres/2828"]')
    bil_book_menu4 = WebElement(xpath='//li[@class="b-menu-second-item active"]//a[@href="/genres/972"]')
    all_books = WebElement(xpath=' //a[text()="Все книги"]')
    periodicals = WebElement(xpath='//a[text()="Периодические издания"]')

    button_main = WebElement(xpath='(//span[@class="b-header-b-menu-e-link"])[1]')

    button_school = WebElement(xpath='//span[@class="b-header-b-menu-e-link "]')
    school_menu = WebElement(xpath='//span[text()="Основные предметы"]')

    button_toys = WebElement(xpath='//span[@class="b-header-b-menu-e-link"]//a[@href="/games/"]')
    toys_items_3 = WebElement(xpath='//span[text()="Игры и Игрушки"]')
    toys_items_1 = WebElement(xpath='//a[text()="Все игрушки"]')

    toys_items_3_puzzle = WebElement(xpath='//a[@href="/genres/1690"]')
    toys_items_3_child_souv = WebElement(xpath='//a[@href="/genres/2922"]')

    button_stationery = WebElement(xpath='(//span[@class="b-header-b-menu-e-link"])[3]')
    stationery_items_3_globes = WebElement(xpath='//a[text()="Глобусы"]')
    stationery_items_1 = WebElement(xpath='//a[text()="Все канцтовары"]')

    button_more = WebElement(xpath='(//span[@class="b-header-b-menu-e-text"])[1]')
    more_items_2_souvenirs = WebElement(xpath='(//a[@href="/souvenir/"])[3]')
    more_items_1_cd_dvd = WebElement(xpath='(//a[@href="/multimedia/"])[3]')
    more_items_3 = WebElement(xpath='(//a[@href="/journals/"])[5]')
    more_items_4 = WebElement(xpath='(//a[@href="/household/"])[3]')

    button_club = WebElement(xpath='(//a[@class="b-header-b-menu-e-text"])[10]')
    littest = WebElement(xpath='(//a[@href="/littest/"])[2]')

    logo = WebElement(xpath='//span[@class="b-header-b-logo-e-logo"]')

    button_social_network = WebElement(xpath='//div[@class ="fleft have-dropdown relative"]')
    button_social_network_vk = WebElement(xpath='//span[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk"]')
    button_social_network_yt = WebElement(xpath='//a[@ href = "https://www.youtube.com/user/labirintruTV"]')


    page_num_3 = WebElement(xpath='//a[@class="pagination-number__text" and @href="?stype=0&page=3"]')

    title_search_error = WebElement(css_selector='input[value = "Русский язык"]')
    button_change_city = WebElement(xpath='//span[@class="region-location-icon-txt "]')
    city_name = WebElement(xpath='//input[@id="region-post"]')
    new_city_name = WebElement(xpath='//a[text()="г. Москва"]')

    button_sort = WebElement(xpath='//span[@class="sorting-value menu-open l-spacing12 navisort-item"]')
    button_sort_preice = WebElement(css_selector='a[data-event-content="дешевые"]')
    products_price1 = WebElement(xpath='(//*[@class="price"])[1]//span//span')
    products_price2 = WebElement(xpath='(//*[@class="price"])[2]//span//span')
    products_price3 = WebElement(xpath='(//*[@class="price"])[3]//span//span')

    button_more_action = WebElement(xpath='(//a[@class="icon-compare track-tooltip js-open-actions-block"])[1]')
    button_add_to_compare = WebElement(xpath='(// a[@class ="b-list-item-hover js-card-block-actions-compare"])[1]')

    field_email = WebElement(xpath='//input[@class="getemail-form-input js-getemail"]')
    massage_under_the_field_email = WebElement(xpath='//label[@class="getemail-form-label getemail-form-e-text"]')
    button_coupon = WebElement(xpath='//span[@class="getemail-btn btn btn-small btn-clear-blue btn-disabled"]')

    block_icons = WebElement(css_selector=' .b-header-b-personal')

    pagination_number_two = WebElement(xpath='//a[@class="pagination-number__text"and@href="?stype=0&page=2"]')
    pagination_number_two_selected = WebElement(xpath='// span[@class ="pagination-number__text selected"]')
    pagination_next = WebElement(xpath=' //div[@class="pagination-next"]//a[@class="pagination-next__text"]')

    button_filter_price = WebElement(xpath='(//span[text()="ЦЕНА"])[1]')
    field_price_min = WebElement(xpath='(// input[@ name="price_min"])[2]')
    field_price_max = WebElement(xpath='(// input[@ name="price_max"])[2]')
    button_show1 = WebElement(xpath='(// input[@value="Показать"])[5]')
    filter_price_100 = WebElement(css_selector='input[id="section-search-form-price_min"]')
    filter_price_150 = WebElement(css_selector='input[id="section-search-form-price_max"]')

    button_all_filters = WebElement(xpath='(//span[@class="navisort-item__content"])[5]')
    cover_color = WebElement(xpath='//div[text()="ЦВЕТ ОБЛОЖКИ"]')
    cover_color_checkbox_red = WebElement(xpath='//div[@class="row"]//ul//li//label')
    button_show2 = WebElement(xpath='(// input[@value="Показать"])[2]')
    filtel_cover_color = WebElement(xpath=' (//span[@class="filter-reset-group__title"])[1]')
    paper_book_check_box = WebElement(xpath='//span[text()="Бумажные книги"]')
    filter_book_check_box = WebElement(xpath='(//div[@class="filter-reset__content"])[1]')
    other_goods_check_box = WebElement(xpath='//span[text()="Прочие товары"]')
    filter_other_goods = WebElement(xpath='(//div[@class="filter-reset__content"])[2]')

    filtel_Availability = WebElement(xpath='// div[text() ="НАЛИЧИЕ"]')
    Availability_check_box = WebElement(xpath='// span[text() ="В наличии"]')
    wait_check_box = WebElement(xpath='// span[text() = "Ожидаются"]')
    no_sale_check_box = WebElement(xpath='// span[text() = "Нет в продаже"]')
    button_pre_order = WebElement(xpath='//a[@data-idtov="875610"]')






