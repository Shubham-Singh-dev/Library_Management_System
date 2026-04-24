from utils import books_dict,issued_books_dict

def show_book():
    if len(books_dict)== 0:
        print("UNFORTUNATELY ! No books are available in present")
    
    else :
        print("\nList of the books 📚 : ")
        print(f"\n{'Name':<10}{'No of copies ':<10} ")
        
        for k,v in books_dict.items():

            print(f"{k : <10}{v :<10}")