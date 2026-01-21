from services.system import System

new_system = System()

continue_using_system = True

print("WELCOME TO THE LIBRARY SYSTEM")

while continue_using_system:

    try:
        user_choice = int(input("Choice what you want to do by the number: "
                                "\n1 - Register Book        |"
                                "2 - Update State Book      |"
                                "3 - Search Print Mode      |"
                            "4 - Delete Mode            "
                            "\n --- Input: "))

    except ValueError:
        print("You must type a number")

    else:
        match user_choice:
            case 1:
                book_title = input("Type the book title: ").title()
                book_writer = input("Type the writer of the book: ").title()
                try:
                    book_year = int(input("Type the year of release: "))
                except ValueError:
                    print("You must type a number\nOperation canceled")
                else:
                    new_system.register_book(book_title, book_writer, book_year)

            case 2:
                print("\n" * 10)
                book_title = input("Type the book title to update the state: ").title()
                new_system.update_state(book_title)

            case 3:
                print("\n" * 10)
                user_search_mode = int(input("Choice what you want to search by the number: "                            
                                "\n1 - Search Book By Title |"
                                "2 - Print All Books        |"
                                "3 - Print All Read Book    |"
                                "4 - Print All Unread Book  |"
                                "\n --- Input: "))
                match user_search_mode:
                    case 1:
                        book_title = input("Type the book title to search for it: ").title()
                        new_system.search_book_by_title(book_title)
                    case 2:
                        new_system.print_all_books()
                    case 3:
                        new_system.print_all_read_book()
                    case 4:
                        new_system.print_all_unread_book()
                break_read = input("Press enter to continue ")
                print("\n" * 10)

            case 4:
                user_delete_mode = int(input("Choice what you want to delete by the number: "                            
                                "\n1 - Delete One Book      |"
                                "2 - Delete All Books       |"
                                "\n --- Input: "))
                match user_delete_mode:
                    case 1:
                        book_title = input("Type the book title to delete it: ").title()
                        new_system.delete_book(book_title)
                    case 2:
                        new_system.delete_all_books()
                print("\n" * 10)