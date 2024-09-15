import requests
import json
from jsonschema import validate
from path import path

url = 'https://api.litres.ru/foundation/api'
endpoint = '/cart/arts/add'
headers = {'Content-Type': 'application/json'}


def test_add_book_to_cart():
    endpoint = '/cart/arts/add'
    art_ids = [9815607]

    response = requests.put(url + endpoint, json={"art_ids": art_ids}, headers=headers)
    body = response.json()

    assert response.status_code == 200
    with open(path('add_book_to_cart.json')) as file:
        validate(body, schema=json.loads(file.read()))
    assert body['payload']['data']['added_art_ids'] == art_ids
    assert body['payload']['data']['failed_art_ids'] == []


def test_search_book_by_title_and_author():
    endpoint = '/search'
    types = 'text_book'
    title = 'Маленький принц'
    full_name = 'Антуан де Сент-Экзюпери'

    response = requests.get(url + endpoint, params={'q': title, 'types': types, 'full_name': full_name})
    body = response.json()

    assert response.status_code == 200
    with open(path('successfull_search_book.json')) as file:
        validate(body, schema=json.loads(file.read()))
    assert body['payload']['data'][0]['type'] == types
    assert body['payload']['data'][0]['instance']['title'] == title
    assert body['payload']['data'][0]['instance']['persons'][0]['full_name'] == full_name


def test_unsuccessfull_search_book():
    endpoint = '/search'
    types = 'text_book'
    title = 'zxcvbnm'

    response = requests.get(url + endpoint, params={'q': title, 'types': types})
    body = response.json()

    assert response.status_code == 200
    with open(path('unsuccessfull_search_book.json')) as file:
        validate(body, schema=json.loads(file.read()))
    assert body['payload']['data'] == []
    assert body['payload']['extra']['counters']['all'] == 0


def test_add_book_to_wishlist():
    endpoint = '/wishlist/arts/'
    id_book = '9815607'
    response = requests.put(url + endpoint + id_book)
    assert response.status_code == 204
    assert response.text == ''


def test_delete_book_from_wishlist():
    endpoint = '/wishlist/arts/'
    id_book = '9815607'
    response = requests.delete(url + endpoint + id_book)
    assert response.status_code == 204
    assert response.text == ''


def test_authorization_with_invalid_password():
    endpoint = '/auth/login'
    login = "marivtest@mail.ru"
    password = "zxcv1234"

    response = requests.post(url + endpoint, headers=headers, json={'login': login, 'password': password})
    body = response.json()

    assert response.status_code == 401
    with open(path('unsuccessfull_authorization.json')) as file:
        validate(body, schema=json.loads(file.read()))
    assert body['error']['title'] == 'Incorrect user data'
    assert body['error']['type'] == 'Unauthorized'
