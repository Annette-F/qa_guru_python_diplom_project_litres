# Проект по автоматизации тестирования онлайн-сервиса электронных и аудиокниг [Litres](https://www.litres.ru/)


## Содержание

- [Технологии и инструменты](#octocat-технологии-и-инструменты)
- [Список реализованных проверок в автотестах](#white_check_mark-список-реализованных-проверок-в-автотестах)
- [Запуск тестов в Jenkins с параметрами](#rocketl-Запуск-тестов-в-Jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#bookmark_tabs-Отчет-о-результатах-тестрования-в-Allure-reports)
- Статистика запуска тест-планов и отчеты в Allure TestOps
- [Уведомление в Telegram о результатах прогона тестов с использованием бота](#loudspeaker-Уведомление-в-Telegram-о-результатах-проверки-с-использованием-бота)
- [Видео-отчет прохождения UI-автотеста на Selenoid](#movie_camera-Видео-отчет-прохождения-теста-на-Selenoid)
- Видео-отчет прохождения Mobile-автотеста


#### [Сайт онлайн-сервиса Litres](https://www.litres.ru/)


## Цель проекта

Тестирование основных функций онлайн-сервиса, позволяющих пользователям пройти успешную авторизацию, найти интересующую книгу, добавить книгу в корзину, 
добавить книгу в список отложенных книг. А также отсутствиии авторизации при неверно указанном пароле.


## :octocat: Технологии и инструменты

<p align="left">
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/python.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/jenkins.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/pycharm.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/pytest.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/github.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/AllureReport.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/Selenoid.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_hw_14_tutu/blob/main/resources/images/selene.png" height="50" width="50">
<img src="https://raw.githubusercontent.com/Annette-F/Annette-F/main/icons/Telegram.svg" width="50" heigth="50"/>
</p>


## :white_check_mark: Список реализованных проверок в автотестах 

## UI-тесты

- Проверка успешной авторизации пользователя
- Проверка отсутствия авторизации при вводе неверного пароля
- Разлогин пользователя
- Поиск книги через строку поиска по автору
- Поиск книги через каталог по жанру
- Добавление книги в "Отложенные"
- Создание списка книг
- Добавление книги в корзину
- Удаление книги из корзины

## API-тесты

- Добавление книги в корзину
- Поиск печатной книги по названию и автору
- Неуспешный поиск печатной книги по названию
- Добавление книги в "Отложенные"
- Удаление книги из "Отложенных"
- Авторизация с неверно указанным паролем

## Mobile-тесты


