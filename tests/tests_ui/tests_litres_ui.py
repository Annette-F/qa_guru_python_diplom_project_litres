from allure_commons.types import Severity
import allure
from pages.authorization_page import authorization
from pages.book_page import book_page


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Успешная авторизация')
@allure.story('Авторизация')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_valid_authorization():
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email()
    authorization.fill_password()
    authorization.submit_authorization()
    authorization.check_successfull_authorization()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Авторизация с неверно указанным паролем')
@allure.story('Авторизация')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_authorization_with_wrong_password():
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email()
    authorization.fill_wrong_password()
    authorization.submit_authorization()
    authorization.check_unsuccessfull_authorization('Неверное сочетание логина и пароля')


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Разлогин')
@allure.story('Авторизация')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_logout():
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email()
    authorization.fill_password()
    authorization.submit_authorization()
    authorization.open_prolife_page()
    authorization.logout_user()
    authorization.check_logout()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Поиск книги через строку поиска по автору')
@allure.story('Поиск книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_search_book_by_author():
    authorization.open()
    book_page.search_book_by_author('Михаил Булгаков')
    book_page.check_search_book_by_author()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Поиск книги через каталог по жанру')
@allure.story('Поиск книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_search_book_through_catalog_by_genre():
    authorization.open()
    book_page.open_catalog()
    book_page.check_search_books_by_genre()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Annette-F')
@allure.feature('Добавление книги в "Отложенные"')
@allure.story('Мои книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_add_book_to_favorite():
    authorization.open()
    book_page.search_book_by_title('Маленький принц')
    book_page.check_search_book_by_title()
    book_page.open_book_page()
    book_page.add_book_to_favorite()
    book_page.check_added_book_to_favorite()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Создание списка книг')
@allure.story('Мои книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_create_list_of_books():
    authorization.open()
    authorization.open_authorization_page()
    authorization.fill_email()
    authorization.fill_password()
    authorization.submit_authorization()
    authorization.open_prolife_page()
    book_page.open_page_list_of_book()
    book_page.create_list_of_books('Любимые книги')


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Добавление книги в корзину')
@allure.story('Корзина')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_add_book_to_cart():
    authorization.open()
    book_page.search_book_by_title('Маленький принц')
    book_page.check_search_book_by_title()
    book_page.open_book_page()
    book_page.add_book_to_cart()
    book_page.check_added_book_to_cart()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Удаление книги из корзины')
@allure.story('Корзина')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_delete_book_from_cart():
    authorization.open()
    book_page.search_book_by_title('Маленький принц')
    book_page.check_search_book_by_title()
    book_page.open_book_page()
    book_page.add_book_to_cart()
    book_page.check_added_book_to_cart()
    book_page.delete_book_from_cart()
