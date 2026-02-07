import json
import os

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn
        }

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.books = [Book(**data) for data in json.load(f)]
        else:
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added successfully!")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return results

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f"{book.title} by {book.author} ({book.year}) - ISBN: {book.isbn}")

def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display All Books")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter year: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)

        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            results = library.search_book(keyword)
            if results:
                print("Search Results:")
                for book in results:
                    print(f"{book.title} by {book.author} ({book.year}) - ISBN: {book.isbn}")
            else:
                print("No matching books found.")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
