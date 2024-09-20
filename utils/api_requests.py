import json
import os
import requests
import logging
import allure
from allure_commons.types import AttachmentType


def api_get(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.get(url=os.getenv('URL') + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name='Response', attachment_type=AttachmentType.JSON, extension='.json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
    return result


def api_post(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.post(url=os.getenv('URL') + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name='Response', attachment_type=AttachmentType.JSON, extension='.json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
    return result


def api_put_to_cart(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.put(url=os.getenv('URL') + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name='Response', attachment_type=AttachmentType.JSON, extension='.json')
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
    return result


def api_put_to_wishlist(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.put(url=os.getenv('URL') + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result


def api_delete(endpoint, **kwargs):
    with allure.step('API Request'):
        result = requests.delete(url=os.getenv('URL') + endpoint, **kwargs)
        allure.attach(body=result.request.method + ' ' + result.url, name='Request',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        allure.attach(body=str(result.status_code), name='Status Code',
                      attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(result.request.url)
        logging.info(result.status_code)
    return result
