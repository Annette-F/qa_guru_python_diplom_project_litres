import os
from selene import browser, be, have
import allure


class AuthorizationUserPage:
    def open(self):
        with allure.step('Open main page https://www.litres.ru'):
            browser.open('/')

    def open_authorization_page(self):
        with allure.step('Open authorization form'):
            browser.element('[data-testid="tab-login"]').click()

    def fill_email(self):
        with allure.step('Fill Email'):
            email = os.getenv('EMAIL')
            browser.element('#auth__input--enterEmailOrLogin').should(be.blank).type(email)
            browser.element('[data-testid="auth__button--continue"]').click()

    def fill_password(self):
        with allure.step('Fill Password'):
            password = os.getenv('USER_PASS')
            browser.element('[data-testid="auth__input--enterPassword"]').should(be.blank).type(password)

    def fill_wrong_password(self):
        with allure.step('Fill Password invalid data'):
            passw = os.getenv('WRONG_PASS')
            browser.element('[data-testid="auth__input--enterPassword"]').should(be.blank).type(passw)

    def submit_authorization(self):
        with allure.step('Submit authorization'):
            browser.element('[data-testid="auth__button--enter"]').click()
            browser.element('.Button_buttonContent__mWLSp').click()

    def check_successfull_authorization(self):
        with allure.step('Check successfull authorization'):
            browser.element('[data-testid="header__profile-button"]').should(be.visible)

    def check_unsuccessfull_authorization(self, text):
        with allure.step('Check unsuccessfull authrization'):
            browser.element('.ControlInput_input__error__0DtKl').should(have.text(text))

    def open_prolife_page(self):
        with allure.step('Open profile'):
            browser.element('[data-testid="authorization-popup__close-button"]').click()
            browser.element('[data-testid="header__profile-button"]').click()

    def logout_user(self):
        with allure.step('Logout'):
            browser.element('.Menu__exit_hEk0E').click()

    def check_logout(self):
        with allure.step('Check successfull logout'):
            browser.element('[data-testid="tab-login"]').should(be.visible)


authorization = AuthorizationUserPage()
