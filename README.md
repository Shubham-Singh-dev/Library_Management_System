# 📚 DictVers Library Management System

A simple command-line based Library Management System built in Python using dictionaries as the core data structure. It allows librarians to add books, issue them to users, track returns, and calculate late fines.

---

## 📁 Project Structure

```
DictVers_Library_Management_System/
│
├── main.py            # Entry point — runs the main library menu loop
├── add_books.py       # Handles adding new books or increasing copies
├── issued_books.py    # Handles issuing books to users
├── return_books.py    # Handles book returns and fine calculation
├── show_books.py      # Displays all available books
└── utils.py           # Shared data stores (dictionaries)
```

---

## 🗂️ File Descriptions

### `utils.py`
Holds three shared in-memory dictionaries used across all modules:
- `books_dict` — stores book names and their available copy count
- `issued_books_dict` — tracks which books are currently issued
- `person_detail` — stores the current borrower's details (name, issue date, time period)

---

### `main.py`
The entry point of the program. Displays an interactive menu in a loop:

```
📚 LIBRARY MANAGEMENT SYSTEM
1. ➕ Add Book
2. 📖 Show Books
3. 📤 Issue Book
4. 📥 Return Book
5. 🚪 Exit
```

---

### `add_books.py`
Allows adding a new book or incrementing the copy count if it already exists.

- Input: Book name (auto-converted to uppercase)
- If book exists → increments count by 1
- If new book → adds it with count 1

---

### `issued_books.py`
Handles the book issuing process.

- Accepts book name, borrower's name, and loan duration (max 15 days)
- Records issue date using `datetime.now().date()`
- Decrements available copy count in `books_dict`
- Stores borrower details in `issued_books_dict`

**Late Fine Policy (displayed at issue time):**

| Period        | Fine              |
|---------------|-------------------|
| Week 1        | ₹10 / day / book  |
| Week 2        | ₹20 / day / book  |
| Week 3        | ₹60 / day / book  |
| Beyond Week 3 | Escalating charges|

---

### `return_books.py`
Handles book returns and calculates any applicable late fines.

- Computes days elapsed since issue date
- Compares against the allowed loan period
- Calculates fine based on the week-wise slab system
- Removes the entry from `issued_books_dict` upon return

**Fine Calculation Logic:**

| Days Late     | Daily Charge      |
|---------------|-------------------|
| Day 1–7       | ₹10 / day         |
| Day 8–14      | ₹20 / day         |
| Day 15–21     | ₹60 / day         |
| Beyond day 21 | ₹10 × week number |

---

### `show_books.py`
Displays all books currently in the library along with available copy counts in a formatted table.

---

## ▶️ How to Run

Make sure you have **Python 3.6+** installed.

```bash
python main.py
```

No external libraries are required — only Python's built-in `datetime` module is used.

---

## ⚙️ Requirements

- Python 3.6 or above
- No third-party packages needed

---



## 🚀 Possible Future Improvements

- Persist data using file storage (JSON/CSV) or a database (SQLite)
- Support multiple borrowers per book
- Add search functionality
- Build a GUI using Tkinter or a web interface

---

## 👨‍💻 Author

Built as a beginner Python project to practice dictionary operations, modular programming, and date/time handling.
