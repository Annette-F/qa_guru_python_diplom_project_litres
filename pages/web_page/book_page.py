from selene import browser, have, be
import allure


class BookPage:
    def search_book_by_author(self, book_author):
        with allure.step('Enter the author of the book in the search field'):
            browser.element('.SearchForm_input__qDTKP').should(be.visible).type(book_author)
            browser.element('.SearchForm_btn__imsGi').click()

    def check_search_book_by_author(self):
        with allure.step('Check the book search result by author'):
            browser.element('[data-testid="art__authorName"]').should(have.text('Михаил Булгаков'))

    def open_catalog(self):
        with allure.step('Open the book catalog'):
            browser.element('.CatalogButton_wrapper__nZ5n8').click()
            browser.open('/genre/klassicheskaya-literatura-5028/')

    def check_search_books_by_genre(self):
        with allure.step('Check the search result through the catalog by genre'):
            browser.element('.PageHeader_title__text__rrWrd').should(have.text('классическая литература'))

    def search_book_by_title(self, book_title):
        with allure.step('Enter the title of the book in the search field'):
            browser.element('.SearchForm_input__qDTKP').should(be.visible).type(book_title)
            browser.element('.SearchForm_btn__imsGi').click()

    def check_search_book_by_title(self):
        with allure.step('Check the book search result by title'):
            browser.element('.ArtInfo_title__h_5Ay').should(have.text('Маленький принц'))

    def add_book_to_favorite(self):
        with allure.step('Add the book to the "Wishlist"'):
            browser.element('[data-testid="wishlist__button"]').click()

    def check_added_book_to_favorite(self):
        with allure.step('Check adding the book to the "Wishlist"'):
            browser.open('/my-books/liked/')
            browser.element('.ArtInfo_title__h_5Ay').should(have.text('Маленький принц'))

    def open_book_page(self):
        with allure.step('Open page with the book'):
            browser.open('/book/antuan-de-sent-ekzuperi/malenkiy-princ-9815607/')

    def add_book_to_cart(self):
        with allure.step('Add the book to the cart'):
            browser.element('[data-testid="book__addToCartButton"]').click()

    def check_added_book_to_cart(self):
        with allure.step('Check adding the book to the cart'):
            browser.open('/my-books/cart/')
            browser.element('.Cart_bookCard___l8R6').should(be.visible)

    def delete_book_from_cart(self):
        with allure.step('Remove the book from the cart'):
            browser.element('[data-testid="cart__listDeleteButton"]').click()
            browser.element('.Button_button_primary__k65Je.Button_button_medium__m3Snt').click()

    def check_deleted_book_from_cart(self):
        with allure.step('Check removing the book from the cart'):
            browser.element('[data-testid="cart__emptyState--wrapper"]').should(have.text('Корзина пуста'))

    def open_page_list_of_book(self):
        with allure.step('Open page "Lists"'):
            browser.open('/my-books/shelfs/')

    def create_list_of_books(self, list_name):
        with allure.step('Create list of books'):
            browser.element('[data-testid="myBook__myFoldersCreate--button"]').click()
            browser.element('[data-testid="myBooks__myFoldersModal--input"]').should(be.blank).type(list_name)
            browser.element('[data-testid="myBooks__myFoldersModalSave--button"]').click()


book_page = BookPage()
