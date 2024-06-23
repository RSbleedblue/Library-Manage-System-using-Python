from BookData import books
from LibraryFunctions import add_book, borrow_book, return_book, view_books, save_books, load_books

def display_welcome_message():
    print("""
 __        __   _                            _          _   _             
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___    
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \   
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/   
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|   
                                                                          
 ______            _     _                 __  __                                   
|  ____|          | |   | |               |  \/  |                                  
| |__  __  ___ __ | | __| | ___ _ __ ___  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
|  __| \ \/ / '_ \| |/ _` |/ _ \ '__/ __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |____ >  <| |_) | | (_| |  __/ |  \__ \ | |  | | (_| | | | | (_| | (_| |  __/ |   
|______/_/\_\ .__/|_|\__,_|\___|_|  |___/ |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
            | |                                                     __/ |          
            |_|                                                    |___/           

    Welcome to the Library Management System!
    Choose an option from the menu below:
    """)

def display_menu():
    print("=========================")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. View Books")
    print("5. Save Books")
    print("6. Load Books")
    print("7. Exit")
    print("=========================")

def main():
    global books
    display_welcome_message()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            view_books(books)
        elif choice == '7':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
