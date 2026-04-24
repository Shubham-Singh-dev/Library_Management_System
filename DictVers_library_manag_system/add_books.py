from utils import books_dict


def add_book():
    book_name = input("Enter the book name : ").strip().upper()
    if book_name in books_dict:
        books_dict[book_name] += 1
    else :
        books_dict[book_name] = 1
    print(f"Book {book_name} added successfully")