from models.book import Book
import sqlite3

con = sqlite3.connect("data/dataBooks.db")
cur = con.cursor()

class System:
    def __init__(self):
        cur.execute("CREATE TABLE IF NOT EXISTS books("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "title TEXT NOT NULL, "
                    "writer TEXT NOT NULL, "
                    "year INTEGER, "
                    "state_Read INTEGER)")

    def register_book(self, title: str, writer: str, year: int):
        new_book = Book(title=title, writer=writer, year=year, state_Read=0)

        self.__save_book_in_data_base(new_book)

    def delete_book(self, bookTitle):
        book_exist = self.__check_if_title_exist(bookTitle)

        if book_exist == True:
            self.search_book_by_title(bookTitle)

            try:
                id_to_delete = int(input("Choice book/id you want delete (press N to cancel): "))
            except ValueError:
                print("Operation to delete book canceled by input letter")
            else:
                id_exist = self.__check_if_id_exist(id_to_delete)
                if id_exist == True:
                    sql_query_delete = "DELETE FROM books WHERE id = ?"
                    cur.execute(sql_query_delete, (id_to_delete,))

                    self.search_book_by_title(bookTitle)
                    con.commit()
                else:
                    print("This id dont exist")
        else:
            print("This title dont exist")

    def search_book_by_title(self, bookTitle):
        title_exist = self.__check_if_title_exist(bookTitle)
        if title_exist == True:
            sql_query = "SELECT * FROM books WHERE title LIKE '%' || ? || '%'"

            cur.execute(sql_query, (bookTitle,))
            results = cur.fetchall()

            for row in results:
                print(f"Book: {row[1]} | Release Year: {row[3]}")
        else:
            print("This title dont exist")

    def update_state(self, bookTitle):
        title_exist = self.__check_if_title_exist(bookTitle)

        if title_exist == True:
            self.search_book_by_title(bookTitle)
            try:
                id_to_update = int(input("Choose title/id to update case to read as true: "))
            except ValueError:
                print("Operation cancelled by input error")
            else:
                sql_query = "UPDATE books SET state_Read = 1 WHERE id = ?"
                cur.execute(sql_query, (id_to_update,))
                self.search_book_by_title(bookTitle)
                con.commit()
        else:
            print(f"This title dont exist")

    def print_all_read_book(self):
        for row in cur.execute("SELECT * FROM books WHERE state_Read = 1"):
            print(f"Book: {row[1]} | Release Year: {row[3]}")

    def print_all_unread_book(self):
        for row in cur.execute("SELECT * FROM books WHERE state_Read = 0"):
            print(f"Book: {row[1]} | Release Year: {row[3]}")

    def print_all_books(self):
        for row in cur.execute("SELECT * FROM books"):
            print(f"Book: {row[1]} | Release Year: {row[3]}")

    def delete_all_books(self):
        user_choice = input(
            "Are you really sure that you want to delete all books in data base? (Press Y and Enter to continue) ").upper()

        if user_choice == "Y":
            user_type_securety = input(
                "To delete all data base, you must type a safe word to continue and delete: 'DELETEALLDATABASE' -").upper()
            if user_type_securety == "DELETEALLDATABASE":
                cur.execute("DELETE FROM books")
                con.commit()

    def __save_book_in_data_base(self, book):
        sql_query = "INSERT INTO books (title, writer, year, state_Read) VALUES (?, ?, ?, ?)"
        cur.execute(sql_query, (book.title, book.writer, book.year, book.state_Read))
        con.commit()

    def __check_if_id_exist(self, id):
        sql_query = "SELECT EXISTS(SELECT 1 FROM books WHERE id = ?)"
        cur.execute(sql_query, (id,))
        result = cur.fetchone()

        return result[0] == 1

    def __check_if_title_exist(self, bookTitle):
        sql_query = "SELECT EXISTS(SELECT 1 FROM books WHERE title = ?)"
        cur.execute(sql_query, (bookTitle,))
        result = cur.fetchone()

        return result[0] == 1

