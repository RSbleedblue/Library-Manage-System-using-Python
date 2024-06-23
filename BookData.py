books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell', 'available': True},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'available': True},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'available': True}
]

def search_by_title(title):
    for book in books:
        if title.lower() in book['title'].lower():
            return book
    return []

def update_Book_available(book_to_find):
    bookExist = search_by_title(book_to_find)
    if bookExist['available'] :
        bookExist['available'] = False
        print(f"Book has been successfully been borrowed!")
        update_book_list(bookExist)
    else:
        print(f"Sorry, '{bookExist['title']}' is already been borrowed")

def return_Book(book_title):
    isExist = search_by_title(book_title)
    isExist['available'] = True
    update_book_list(isExist)
    return True

def update_book_list(bookToUpdate):
    for i,book in enumerate(books):
        if(book['id'] == bookToUpdate['id']):
            books[i] = bookToUpdate
            break
        