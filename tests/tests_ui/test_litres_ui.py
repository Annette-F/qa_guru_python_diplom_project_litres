from allure_commons.types import Severity
import allure
from pages.web_page.authorization_page import authorization
from pages.web_page.book_page import book_page


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Successfull authorizaton')
@allure.story('Authorization')
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
@allure.feature('Authorization with invalid data')
@allure.story('Authorization')
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
@allure.feature('Logout')
@allure.story('Authorization')
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
@allure.feature('Search a book by the author search field')
@allure.story('Search book')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_search_book_by_author():
    authorization.open()
    book_page.search_book_by_author('Михаил Булгаков')
    book_page.check_search_book_by_author()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search for a book through the catalog by genre')
@allure.story('Search book')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_search_book_through_catalog_by_genre():
    authorization.open()
    book_page.open_catalog()
    book_page.check_search_books_by_genre()


@allure.tag('Web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Annette-F')
@allure.feature('Add the book to the "Wishlist"')
@allure.story('My books')
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
@allure.feature('Create a list of books')
@allure.story('My books')
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
@allure.feature('Add the book to the cart')
@allure.story('Cart')
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
@allure.feature('Remove book from the cart')
@allure.story('Cart')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_delete_book_from_cart():
    authorization.open()
    book_page.search_book_by_title('Маленький принц')
    book_page.check_search_book_by_title()
    book_page.open_book_page()
    book_page.add_book_to_cart()
    book_page.check_added_book_to_cart()
    book_page.delete_book_from_cart()
