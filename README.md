[![Python CI](https://github.com/Alexanderkona/pythontest/actions/workflows/python-app.yml/badge.svg)](https://github.com/Alexanderkona/pythontest/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/github/Alexanderkona/pythontest/badge.svg?branch=main)](https://coveralls.io/github/Alexanderkona/pythontest?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Alexanderkona_pythontest&metric=alert_status)](https://sonarcloud.io/dashboard?id=Alexanderkona_pythontest)

# pythontest

 


Блочные тесты
Тест №1: Проверка добавления книги (позитивный)
Цель: Проверить, что книга добавляется в библиотеку.
Входные данные: (title = "1984", author = "George Orwell")
Ожидаемый результат: В библиотеке одна книга с информацией "1984 by George Orwell".
Описание процесса: Вызов метода add_book с корректными данными должен увеличить количество книг в библиотеке на 1.

Тест №2: Проверка добавления книги с пустым заголовком (негативный)
Цель: Проверить, что при пустом заголовке книга не добавляется.
Входные данные: (title = "", author = "George Orwell")
Ожидаемый результат: В библиотеке 0 книг и вызывается предупреждение о пустом заголовке.
Описание процесса: Вызов метода add_book с пустым заголовком должен оставить количество книг равным 0.

Тест №3: Проверка добавления книги с пустым автором (негативный)
Цель: Проверить, что при пустом имени автора книга не добавляется.
Входные данные: (title = "1984", author = "")
Ожидаемый результат: В библиотеке 0 книг и вызывается предупреждение о пустом имени автора.
Описание процесса: Вызов метода add_book с пустым именем автора должен оставить количество книг равным 0.

Тест №4: Проверка добавления книги с слишком длинным заголовком (негативный)
Цель: Проверить, что книга не добавляется, если заголовок превышает 100 символов.
Входные данные: (title = "A" * 101, author = "George Orwell")
Ожидаемый результат: В библиотеке 0 книг и вызывается предупреждение о длинном заголовке.
Описание процесса: Вызов метода add_book с заголовком длиной более 100 символов должен оставить количество книг равным 0.

Тест №5: Проверка добавления книги с слишком длинным именем автора (негативный)
Цель: Проверить, что книга не добавляется, если имя автора превышает 100 символов.
Входные данные: (title = "1984", author = "A" * 101)
Ожидаемый результат: В библиотеке 0 книг и вызывается предупреждение о длинном имени автора.
Описание процесса: Вызов метода add_book с именем автора длиной более 100 символов должен оставить количество книг равным 0.

Тест №6: Проверка расстояния Левенштейна (позитивный)
Цель: Проверить правильность вычисления расстояния Левенштейна.
Входные данные: (str1 = "kitten", str2 = "sitting")
Ожидаемый результат: Расстояние Левенштейна равно 3.
Описание процесса: Вызов метода levenshtein_distance с "kitten" и "sitting" должен вернуть 3.

Тест №7: Проверка расстояния Левенштейна (негативный)
Цель: Проверить, что расстояние Левенштейна не меньше 3 для двух разных строк.
Входные данные: (str1 = "cat", str2 = "dog")
Ожидаемый результат: Расстояние Левенштейна больше или равно 3.
Описание процесса: Вызов метода levenshtein_distance с "cat" и "dog" должен вернуть значение, большее или равное 3.

Интеграционные тесты
Тест №8: Проверка поиска книги по существующему заголовку (позитивный)
Цель: Проверить, что функция поиска находит книгу по заголовку.
Входные данные: (title = "1984")
Ожидаемый результат: Найденная книга содержит "1984".
Описание процесса: Вызов метода find_books с заголовком "1984" должен вернуть список, содержащий "1984".

Тест №9: Проверка поиска книги по несуществующему заголовку (негативный)
Цель: Проверить, что функция поиска не находит книгу по несуществующему заголовку.
Входные данные: (title = "Animal Farm")
Ожидаемый результат: Не найдено книг с заголовком "Animal Farm".
Описание процесса: Вызов метода find_books с заголовком "Animal Farm" должен вернуть пустой список.

Тест №10: Проверка добавления книги с корректными данными (позитивный)
Цель: Проверить, что при вводе корректных данных книга успешно добавляется в библиотеку.
Входные данные: (title = "1984", author = "George Orwell")
Ожидаемый результат: В библиотеке 1 книга, и вызывается уведомление об успешном добавлении книги.
Описание процесса: Вызов метода add_book с корректными данными (название книги "1984" и имя автора "George Orwell") должен увеличить количество книг в библиотеке до 1 и выдать уведомление о том, что книга успешно добавлена.

Тест №11: Проверка добавления книги с пустым заголовком и пустым автором (негативный)
Цель: Проверить, что при пустом заголовке и пустом имени автора книга не добавляется.
Входные данные: (title = "", author = "")
Ожидаемый результат: В библиотеке 0 книг и вызывается предупреждение о пустом заголовке и имени автора.
Описание процесса: Вызов метода add_book с пустым заголовком и пустым именем автора должен оставить количество книг равным 0, и должно быть выдано предупреждение о том, что название книги и имя автора не могут быть пустыми.



