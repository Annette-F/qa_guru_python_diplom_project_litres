# Проект по автоматизации тестирования онлайн-сервиса электронных и аудиокниг <img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/litres.svg" width="150" heigth="150"/>


## :world_map: Содержание

- [Технологии и инструменты](#octocat-технологии-и-инструменты)
- [Список реализованных проверок в автотестах](#white_check_mark-список-реализованных-проверок-в-автотестах)
- [Запуск тестов в Jenkins с параметрами](#rocketl-Запуск-тестов-в-Jenkins-с-параметрами)
- [Отчет о результатах тестирования в Allure-reports](#bookmark_tabs-Отчет-о-результатах-тестрования-в-Allure-reports)
- Статистика запуска тест-планов и отчеты в Allure TestOps
- [Уведомление в Telegram о результатах прогона тестов с использованием бота](#loudspeaker-Уведомление-в-Telegram-о-результатах-проверки-с-использованием-бота)
- [Видео-отчет прохождения UI-автотеста на Selenoid](#movie_camera-Видео-отчет-прохождения-теста-на-Selenoid)
- [Видео-отчет прохождения Mobile-автотеста](#movie_camera-Видео-отчет-прохождения-Mobile-автотеста)


#### <img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/litres.svg" width="70" heigth="70"/> [Сайт онлайн-сервиса Litres](https://www.litres.ru/)


## :dart: Цель проекта

Тестирование основных функций онлайн-сервиса, позволяющих пользователям пройти успешную авторизацию, найти интересующую книгу, добавить книгу в корзину, 
добавить книгу в список отложенных книг. А также отсутствиии авторизации при неверно указанном пароле.


## :gear: Технологии и инструменты

<p align="left">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/python.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/jenkins.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/pycharm.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/pytest.svg" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/github.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/AllureReport%20(1).png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/AllureTestOps.png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/Selenoid%20(1).png" height="50" width="50">
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/selene%20(1).png" height="50" width="50">
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/browserstack.svg" width="50" heigth="50"/>
<img src="https://github.com/Annette-F/qa_guru_python_diplom_project_litres/blob/main/resources/images/appium.png" width="50" heigth="50"/>
<img src="https://raw.githubusercontent.com/Annette-F/qa_guru_python_diplom_project_litres/refs/heads/main/resources/images/Telegram.svg" width="50" heigth="50"/>
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



## :rocket: Запуск тестов в Jenkins с параметрами

Сборка, параметризация и запуск проекта производятся с помощью Jenkins. При каждом запросе на тестирование браузера Selenoid запускает новый Docker-контейнер и останавливает его после закрытия браузера. Перед запуском можно указать версию браузера (в данном случае запуск тестов проводился на браузере Chrome версии 126.0). Также в параметрах добавлена возможность выбора окружения, на котором будут запущены тесты. 


## :bar_chart: Отчет о результатах тестирования в Allure-reports

После прохождения тестов автоматически формируется отчет в Allure Report. Allure формирует подробный отчет о результатах прогона тестов. Кастомные фильтры и листенеры делают отчет максимально понятным. Например, в отчет пишутся все селекторы и методы Selene, отчеты формируются по категориям.
После окончания выполнения автотестов по каждому из них в отчете доступны скриншоты, лог консоли браузера и видеозапись выполнения теста.


## :bar_chart: Статистика запуска тест-планов и отчеты в Allure TestOps


## :email: Уведомление в Telegram о результатах прогона тестов с использованием бота

Настроено автоматическое оповещение о результатах прохождения тестов в Telegram-бот с полной информацией о прогоне и ссылкой на Allure


## :movie_camera: Видео-отчет прохождения UI-автотеста на Selenoid

Пример видеозаписи выполнения теста.


## :movie_camera: Видео-отчет прохождения Mobile-автотеста
