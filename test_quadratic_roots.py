import unittest
from main import Library, Book, LibraryApp
from unittest.mock import patch
import tkinter as tk



class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book = Book("1984", "George Orwell")
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].get_info(), "1984 by George Orwell")

    def test_display_books(self):
        book1 = Book("1984", "George Orwell")
        book2 = Book("Brave New World", "Aldous Huxley")
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.assertEqual(self.library.display_books(), ["1984 by George Orwell", "Brave New World by Aldous Huxley"])

    def test_find_books_positive(self):
        book = Book("1984", "George Orwell")
        self.library.add_book(book)
        matches = self.library.find_books("1984")
        self.assertIn("1984", matches)

    def test_find_books_negative(self):
        book = Book("1984", "George Orwell")
        self.library.add_book(book)
        matches = self.library.find_books("Animal Farm")
        self.assertNotIn("Animal Farm", matches)

    def test_levenshtein_distance(self):
        self.assertEqual(self.library.levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(self.library.levenshtein_distance("flaw", "lawn"), 2)

    def test_levenshtein_distance_negative(self):
        # Проверяем, что расстояние Левенштейна для двух совершенно разных строк
        self.assertGreaterEqual(self.library.levenshtein_distance("cat", "dog"), 3)

class TestLibraryApp(unittest.TestCase):

    def setUp(self):
        self.library_app = LibraryApp(tk.Tk())
        self.library_app.library = Library()  # Заменяем библиотеку на новую для тестов

    @patch('tkinter.messagebox.showinfo')
    def test_add_book_valid_data(self, mock_showinfo):
        self.library_app.title_entry.insert(0, "1984")
        self.library_app.author_entry.insert(0, "George Orwell")
        self.library_app.add_book()
        self.assertEqual(len(self.library_app.library.books), 1)
        mock_showinfo.assert_called_with("Успех", "Книга успешно добавлена!")

    @patch('tkinter.messagebox.showwarning')
    def test_add_book_empty_title(self, mock_showwarning):
        self.library_app.author_entry.insert(0, "George Orwell")
        self.library_app.add_book()
        self.assertEqual(len(self.library_app.library.books), 0)
        mock_showwarning.assert_called_with("Ошибка ввода", "Название книги и имя автора не могут быть пустыми.")

    @patch('tkinter.messagebox.showwarning')
    def test_add_book_empty_author(self, mock_showwarning):
        self.library_app.title_entry.insert(0, "1984")
        self.library_app.add_book()
        self.assertEqual(len(self.library_app.library.books), 0)
        mock_showwarning.assert_called_with("Ошибка ввода", "Название книги и имя автора не могут быть пустыми.")

    @patch('tkinter.messagebox.showwarning')
    def test_add_book_title_too_long(self, mock_showwarning):
        long_title = "A" * 101  # Длина больше 100 символов
        self.library_app.title_entry.insert(0, long_title)
        self.library_app.author_entry.insert(0, "George Orwell")
        self.library_app.add_book()
        self.assertEqual(len(self.library_app.library.books), 0)
        mock_showwarning.assert_called_with("Ошибка ввода", "Название книги не должно превышать 100 символов.")

    @patch('tkinter.messagebox.showwarning')
    def test_add_book_author_too_long(self, mock_showwarning):
        long_author = "A" * 101  # Длина больше 100 символов
        self.library_app.title_entry.insert(0, "1984")
        self.library_app.author_entry.insert(0, long_author)
        self.library_app.add_book()
        self.assertEqual(len(self.library_app.library.books), 0)
        mock_showwarning.assert_called_with("Ошибка ввода", "Имя автора не должно превышать 100 символов.")

if __name__ == '__main__':
    unittest.main()