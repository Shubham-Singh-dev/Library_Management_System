from utils import books_dict, issued_books_dict,person_detail
from datetime import datetime

def return_book():
    book_name = input("Enter the name of the book you want to return : ").strip().upper()

    print("\nLate Charges Rules")
    print("1st week  = Rs 10/day/book")
    print("2nd week  = Rs 20/day/book")
    print("3rd week  = Rs 60/day/book")
    print("After that charges keep increasing.\n")

    # print(issued_books_dict)
    if book_name in issued_books_dict:
        
    
        issued_books_dict.pop(book_name)
        return_date = datetime.now().date()
        issue_date = person_detail["DateTime"]
        allowed_days = person_detail["TimePeriod"]

        days_passed = (return_date - issue_date).days
    
        late_days = days_passed - allowed_days
            

        fine = 0

        if late_days > 0:

            for day in range(1, late_days + 1):
                if day <= 7:
                    fine += 10

                elif day <= 14:
                    fine += 20

                elif day <= 21:
                    fine += 60

                else:
                    week = (day // 7) + 1
                    charge = 10 * week
                    fine += charge

            print("Book returned late by", late_days, "days")
            print("Total Fine = Rs", fine)

        else:
            print("No Fine")

        

        print(f"The book {book_name} has been successfully returned on {datetime.now()}")

    else:
        print(f"It seems like this book {book_name} doesn't belong to our library.")
                    
        



    
