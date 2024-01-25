# qa_python_sprint_4

### Содержание проекта:

- `conftest.py` - фикстуры
- `main.py` - приложение BooksCollector
- `tests.py` - юнит-тесты

### Описание:
В файле `tests.py` содержатся юнит-тесты, покрывающие приложение `BooksCollector`, которое находится в `main.py`.
Большая часть тестов покрывают основной функционал. Часть тестов являются негативными. Ниже перечислены тесты, их 
описание и методы которые они проверяют.

### Тесты в фале tests.py:

- `test_add_new_book_add_two_books` - Добавление двух сущностей. 
Проверяет методы `add_new_book` и `get_books_genre`. 


- `test_add_new_book_validation_name_book_negative` - Негативный тест на валидацию. 
Проверяет методы `add_new_book` и `get_books_genre`. 



- `test_get_books_with_specific_genre` - Вывод списка книг с 
опредленным жанром. Проверяет метод `get_books_with_specific_genre`. 


- `test_set_book_genre_set_new_book_genre` - Установка и получение жанра книги по ее имени.
Проверяет методы `add_new_book`, `set_book_genre` и `get_books_genre`. 



- `test_get_books_for_children_check_age_rating` - Вывод книг без 
возрастного ограничения. Проверяет метод `get_books_for_children`. 


- `test_add_book_in_favorites_add_one_book` - Добавление сущности в список избранных книг. 
Проверяет методы `add_new_book`, `add_book_in_favorites` и `get_list_of_favorites_books` . 


- `test_add_book_in_favorites_double_add_book` - Повторное добавление в избранное одной и тоей же книги. 
Проверяет метод `add_new_book`, `add_book_in_favorites` и `get_list_of_favorites_books`. 


- `test_delete_book_from_favorites_delete_book` - Удаление сущности из списка избранных книг. 
Проверяет методы `add_new_book`, `add_book_in_favorites`,`delete_book_from_favorites` и `get_list_of_favorites_books`. 



### Запуск тестов: 
`pytest -v tests.py` 