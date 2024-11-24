import tkinter as tk
from tkinter import messagebox


class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def get_info (self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__ (self):
        self.books = []

    def add_book (self, book):
        self.books.append(book)

    def display_books (self):
        return [book.get_info() for book in self.books]

    def levenshtein_distance (self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

    def find_books (self, title):
        titles = [book.title for book in self.books]
        matches = []
        for t in titles:
            if self.levenshtein_distance(title, t) <= 4:  # Можно настроить порог
                matches.append(t)
        return matches


class LibraryApp:
    def __init__ (self, root):
        self.library = Library()
        self.root = root
        self.root.title("Система управления библиотекой")

        self.title_label = tk.Label(root, text="Название книги:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Автор:")
        self.author_label.pack()
        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.add_button = tk.Button(root, text="Добавить книгу", command=self.add_book)
        self.add_button.pack()

        self.search_button = tk.Button(root, text="Поиск книг", command=self.search_books)
        self.search_button.pack()

        self.display_button = tk.Button(root, text="Показать все книги", command=self.display_books)
        self.display_button.pack()

        self.books_list = tk.Text(root, height=10, width=50)
        self.books_list.pack()

    def _validate_book_data (self, title, author):
        if not title or not author:
            return False, "Название книги и имя автора не могут быть пустыми."
        if len(title) > 100:
            return False, "Название книги не должно превышать 100 символов."
        if len(author) > 100:
            return False, "Имя автора не должно превышать 100 символов."
        return True, ""

    def add_book (self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        is_valid, message = self._validate_book_data(title, author)

        if is_valid:
            book = Book(title, author)
            self.library.add_book(book)
            messagebox.showinfo("Успех", "Книга успешно добавлена!")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Ошибка ввода", message)

    def search_books (self):
        title = self.title_entry.get()
        if title:
            matches = self.library.find_books(title)
            self.books_list.delete(1.0, tk.END)  # Очистить текстовое поле
            if matches:
                for match in matches:
                    self.books_list.insert(tk.END, match + "\n")
            else:
                self.books_list.insert(tk.END, "Книги не найдены.\n")
        else:
            messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите название книги для поиска.")

    def display_books (self):
        self.books_list.delete(1.0, tk.END)  # Очистить текстовое поле
        books = self.library.display_books()
        if books:
            for book in books:
                self.books_list.insert(tk.END, book + "\n")
        else:
            self.books_list.insert(tk.END, "Нет добавленных книг.\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()