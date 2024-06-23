from BookData import search_by_title,books,update_Book_available,return_Book

def add_book(books):
    id = len(books)+1
    title = input("Enter the Title of the book: ")
    author = input("Enter the Author name: ")
    books.append({'id':id,'title':title, 'author':author, 'available' : True})
    print(f"Book '{title} by {author} added to the library")

def borrow_book():
    book_to_find = input("Enter the title of the book: ")
    searchBook = search_by_title(book_to_find)
    if(len(searchBook) == 0):
        print("Book is not in the Store yet! Contact in near future")
        return
    update_Book_available(book_to_find=book_to_find)
    

def return_book():
    book_to_return = input("Enter the Title of the book: ")
    isDone = return_Book(book_to_return)
    if isDone != True:
        print("Error Updating Book")
        return
    print(f"Book '{book_to_return}' is successfully returned")
    return

def view_books(books):
    for i in books:
        print(i)
    