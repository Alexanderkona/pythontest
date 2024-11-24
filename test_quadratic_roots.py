import unittest
from main import Library, Book


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

    def test_find_books_positive (self):
        book = Book("1984", "George Orwell")
        self.library.add_book(book)
        matches = self.library.find_books("1984")
        self.assertIn("1984", matches)  # Проверяем только название книги

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


if __name__ == '__main__':
    unittest.main()