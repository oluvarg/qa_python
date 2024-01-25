import pytest
import random
import string


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2, 'Колличество сущностей в списке не совпадает'

    def test_add_new_book_validation_name_book_negative(self,collector):

        collector.add_new_book(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(41)))
        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0, ('Была создана сущность с названием с кол-вом симоволов:'
                                                       ' 0 или больше 40')

    def test_set_book_genre_set_new_book_genre(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre(name='Гордость и предубеждение и зомби') == 'Ужасы', ('Жанр книги'
                                                                                              'не соответствует'
                                                                                              'ожидаемому результату')

    @pytest.mark.parametrize('books_genre, expected_result',
                             [
                                 (
                                         {'Книга1': 'Ужасы',
                                          'Книга2': 'Фантастика',
                                          'Книга3': 'Детективы',
                                          'Книга4': 'Ужасы',
                                          'Книга5': 'Комедии',},
                                         ['Книга2']
                                 )
                             ]

    )
    def test_get_books_with_specific_genre(self, books_genre, expected_result, collector):

        collector.books_genre = books_genre

        assert collector.get_books_with_specific_genre('Фантастика') == expected_result, ('Выведенный список книг не '
                                                                                          'соответстует ожидаемому '
                                                                                          'результату')

    @pytest.mark.parametrize('books_genre, expected_result',
                             [
                                 (
                                         {'Книга1': 'Ужасы',
                                          'Книга2': 'Фантастика',
                                          'Книга3': 'Детективы',
                                          'Книга4': 'Мультфильмы',
                                          'Книга5': 'Комедии'},
                                         ['Книга2', 'Книга4', 'Книга5']
                                 ),
                                 (
                                         {'Книга1': 'Ужасы',
                                          'Книга2': 'Мультфильмы',
                                          'Книга3': 'Детективы',
                                          'Книга4': 'Ужасы',
                                          'Книга5': 'Ужасы'},
                                         ['Книга2']
                                 )
                             ]
                             )
    def test_get_books_for_children_check_age_rating(self, books_genre, expected_result, collector):

        collector.books_genre = books_genre

        assert collector.get_books_for_children() == expected_result,  ('Выведенный список книг не '
                                                                        'соответстует ожидаемому '
                                                                        'результату')

    def test_add_book_in_favorites_add_one_book(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1, ('Число книг в избранном не соответствует ожидаемому '
                                                                   'результату')

    def test_add_book_in_favorites_double_add_book(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1, ('Число книг в избранном не соответствует ожидаемому '
                                                                   'результату')

    def test_delete_book_from_favorites_delete_book(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0, ('Число книг в избранном не соответствует ожидаемому '
                                                                   'результату')
