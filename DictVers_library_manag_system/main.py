from add_books import add_book
from issued_books import issue_book
from show_books import show_book
from return_books import return_book

def library():
    while True:
        print("\n" + "-"*35)
        print("       📚 LIBRARY MANAGEMENT SYSTEM")
        print("-"*35)
        print("  1. ➕ Add Book")
        print("  2. 📖 Show Books")
        print("  3. 📤 Issue Book")
        print("  4. 📥 Return Book")
        print("  5. 🚪 Exit")
        print("-"*35)

        choice = int(input("👉 Enter your choice (1-5): "))

        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("\n✅ Thank you for using the Library System. Goodbye! 👋")
            break
        else:
            print("⚠️  Invalid choice! Please enter a number between 1 and 5.")


library()
