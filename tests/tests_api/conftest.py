from selene import browser
import pytest
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def base_url(request):
    browser.config.base_url = os.getenv('URL_API')

    yield

    browser.quit()