from datetime import datetime
from utils import books_dict, issued_books_dict,person_detail

def issue_book():

    print("*"*40)
    print("NOTE :\n If missed the chance to return the book by the given date :\n   1st week - 10 Rs /day/book \n 2nd week - 10*2/day/book \n 3rd  week - 10*2*3/day/book\n ...  ")
    print("*"*40)

    book_name = input("Enter the name of the book : ").strip().upper()
    
    person_detail["Name"] = input("Enter Name : ").strip().upper()
    person_detail["TimePeriod"] = int(input("For how many days : (#Max 15 days only ) : "))
    today = datetime.now().date()
    person_detail["DateTime"] = today

    print(person_detail)
    if book_name in books_dict:

        if books_dict[book_name]>= 1:
            books_dict[book_name] -= 1

            issued_books_dict[book_name] = person_detail
            print(f"Congratulation ✌🏻 The book {book_name} has been issued to {person_detail["Name"]}")

        else :
            print(f"Ohh!! SORRY \n This book {book_name} is not available NOW ")



