# qa_python

## Тесты в фале test.py:

- `test_add_new_book_add_two_books` - проверяет методы `add_new_book` и `get_books_genre`. Добавление двух сущностей.


- `test_add_new_book_validation_name_book_negative` - проверяет методы `add_new_book` и `get_books_genre`. 
Негативный тест на валидацию.


- `test_get_books_with_specific_genre` - проверяет метод `get_books_with_specific_genre`. Вывод списка книг с 
опредленным жанром


- `test_set_book_genre_set_new_book_genre` - проверяет методы `add_new_book`, `set_book_genre` и `get_books_genre`. 
Установка и получение жанра книги по ее имени.


- `test_get_books_for_children_check_age_rating` - проверяет метод `get_books_for_children`. Вывод книг без 
возрастного ограничения.


- `test_add_book_in_favorites_add_one_book` - проверяет методы `add_new_book`, `add_book_in_favorites` и 
`get_list_of_favorites_books` . Добавление сущности в список избранных книг.


- `test_add_book_in_favorites_double_add_book` - проверяет метод `add_new_book`, `add_book_in_favorites` и 
`get_list_of_favorites_books`. Повторное добавление в избранное одной и тоей же книги.


- `test_delete_book_from_favorites_delete_book` - проверяет методы `add_new_book`, `add_book_in_favorites`, 
`delete_book_from_favorites` и `get_list_of_favorites_books`. Удаление сущности из списка избранных книг.