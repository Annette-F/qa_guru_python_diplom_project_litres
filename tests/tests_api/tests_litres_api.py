import json
import os
from jsonschema import validate
from path import path
import allure
from allure_commons.types import Severity
from utils.api_requests import api_get, api_post, api_put_to_cart, api_put_to_wishlist, api_delete


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Добавление книги в корзину')
@allure.story('Корзина')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_add_book_to_cart():
    endpoint = '/cart/arts/add'
    headers = {'Content-Type': 'application/json'}
    art_ids = [9815607]

    with allure.step('Добавление книги в корзину'):
        result = api_put_to_cart(endpoint, json={'art_ids': art_ids}, headers=headers)

    assert result.status_code == 200

    with open(path('add_book_to_cart.json')) as file:
        validate(result.json(), schema=json.loads(file.read()))
    assert result.json()['payload']['data']['added_art_ids'] == art_ids
    assert result.json()['payload']['data']['failed_art_ids'] == []


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Поиск печатной книги по названию и автору')
@allure.story('Поиск')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_search_book_by_title_and_author():
    endpoint = '/search'
    types = 'text_book'
    title = 'Маленький принц'
    full_name = 'Антуан де Сент-Экзюпери'

    with allure.step('Поиск печатной книги по названию и автору'):
        result = api_get(endpoint, params={'q': title, 'types': types, 'full_name': full_name})

    assert result.status_code == 200

    with open(path('successfull_search_book.json')) as file:
        validate(result.json(), schema=json.loads(file.read()))
    assert result.json()['payload']['data'][0]['type'] == types
    assert result.json()['payload']['data'][0]['instance']['title'] == title
    assert result.json()['payload']['data'][0]['instance']['persons'][0]['full_name'] == full_name


@allure.tag('API')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Неуспешный поиск печатной книги по названию')
@allure.story('Поиск')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_unsuccessfull_search_book():
    endpoint = '/search'
    types = 'text_book'
    title = 'zxcvbnm'

    with allure.step('Неуспешный поиск печатной книги по названию'):
        result = api_get(endpoint, params={'q': title, 'types': types})

    assert result.status_code == 200

    with open(path('unsuccessfull_search_book.json')) as file:
        validate(result.json(), schema=json.loads(file.read()))
    assert result.json()['payload']['data'] == []
    assert result.json()['payload']['extra']['counters']['all'] == 0


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Добавление книги в "Отложенные"')
@allure.story('Мои книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_add_book_to_wishlist():
    endpoint = '/wishlist/arts/'
    id_book = '9815607'

    with allure.step('Добавление книги в "Отложенные"'):
        result = api_put_to_wishlist(endpoint + id_book)

    assert result.status_code == 204
    assert result.text == ''


@allure.tag('API')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Удаление книги из "Отложенных"')
@allure.story('Мои книги')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_delete_book_from_wishlist():
    endpoint = '/wishlist/arts/'
    id_book = '9815607'

    with allure.step('Удаление книги из "Отложенных"'):
        result = api_delete(endpoint + id_book)

    assert result.status_code == 204
    assert result.text == ''


@allure.tag('API')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Авторизация с неверно указанным паролем')
@allure.story('Авторизация')
@allure.link('https://www.litres.ru', name='LitRes.ru')
def test_authorization_with_invalid_password():
    endpoint = '/auth/login'
    headers = {'Content-Type': 'application/json'}
    login = os.getenv('EMAIL')
    password = os.getenv('WRONG_PASS')

    with allure.step('Авторизация с неверно указанным паролем'):
        result = api_post(endpoint, headers=headers, json={'login': login, 'password': password})

    assert result.status_code == 401

    with open(path('unsuccessfull_authorization.json')) as file:
        validate(result.json(), schema=json.loads(file.read()))
    assert result.json()['error']['title'] == 'Incorrect user data'
    assert result.json()['error']['type'] == 'Unauthorized'
