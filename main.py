class Library:

    def __init__(self):
        #ქმნის dictionary-ს წიგნების ბიბლიოთეკისთვის
        # amis gadatana ar dagaviwydes
        self.books = {
            '1': {'name': 'learn python3 the hard way 2018', 'availability': 'free'},
            '2': {'name': 'Red Rising', 'availability': 'free'},
            '3': {'name': 'A Dance of Dragons', 'availability': 'free'},
            '4': {'name': 'The Two Towers', 'availability': 'free'},
            '5': {'name': 'Introduction to Algorithms', 'availability': 'free'},
            '6': {'name': 'Coding in java', 'availability': 'free'},
            '7': {'name': 'The Decline and Fall of the Roman Empire', 'availability': 'free'},
            '8': {'name': 'Brothers Karamazov', 'availability': 'free'}
        }


    def display_books(self):
        #ეს ფუნქცია აჩვენებს თავისუფალ წიგნებს
        book_count = 0
        print("Our available books: ")
        for book_id, book_data in self.books.items():
            if book_data['availability'] == 'free':
                book_count += 1
                #თუ კოდი ნახავს თავისუფალ წიგნს მიუმატებს 1-ს
                print(f"BookID: {book_id}, name: {book_data['name']}")
                # აჩვენებს მათ სახელს და id-ს
        if not self.books:
            print("No books are available now, please check back later.")
        elif book_count == 0:
            print("all books are borrowed")
            #თუ დაითვალა 0 ზემოთ მოცემულს დაპრინტავს


    def borrow_book(self, user, book_name):
            #ფუნქციაა რომლიც მიცემს მომხმარებელს წიგნის აღების უფლებას
            for book_id, book_data in self.books.items():
                if book_data["name"].lower() == book_name.lower():
                    if book_data['availability'] == 'free':
                        self.books[book_id]['availability'] = 'unavailable'
                        return f'{user} has borrowed {book_data["name"]}'
                    else:
                        return f'{book_data["name"]} is already borrowed.'
            return 'please enter a name of a book from the books displayed.'
            #იმ შემთხვევაში თუ წიგნი უკვე აღებულია ან თუ შეყვანილი სახელი არასწორაი ამ მესიჯს დაპრინტავს


    def return_book(self, user, book_name):
        #ეს ფუნქცია აბრუმებს წიგნებს
        for book_id, book_data in self.books.items():
            if book_data["name"].lower() == book_name.lower():
                if book_data['availability'] == 'unavailable':
                    self.books[book_id]['availability'] = 'free'
                    return f'{user} has returned {book_data["name"]}'
                else:
                    return f'{book_data["name"]} is not borrowed by you.'
        return "please enter a name of a book from the books displayed."
        # თუ წიგნი არ არის აღებული ან სახელი არ არის სწორად ამ მესიჯს დააბრუნებს

    def view_books(self):
        # ნახავს აღებულ წიგნებს ამ ფუნქციის დახმარებით
        borrowed_books = []
        for book_id, book_data in self.books.items():
            if book_data['availability'] == 'unavailable':
                borrowed_books.append(f"BookID: {book_id}, name: {book_data['name']}")
            # if the book is unavailable it will be appended to the borrowed books list
        return borrowed_books


def func():
    library = Library()

    # სახელის მიღება
    user = input('enter your username: ')
    print("Welcome to Our library, here you will find a wide range of bestselling books.")

    while True:
        #  while loop-ი იმუშავებს სანამ უზერი არ გამოვა კოდიდან
        print('=============')
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View your books")
        print("5. Exit")
        print("=============")

        choice = input("Enter a number corresponding to the commands listed above: ")
        if choice == '1':  # displays available books
            library.display_books()
        elif choice == '2':  # allows user to borrow a book
            book_name = input("enter the name of the book you would like to borrow: ")
            print(library.borrow_book(user, book_name))
        elif choice == '3':  # allows user to return a book
            book_name = input("enter the name of the book you would like to return: ")
            print(library.return_book(user, book_name))
        elif choice == '4':  # displays users borrowed books
            borrowed_books = library.view_books()
            if borrowed_books:
                print("list of books you borrowed:")
                for books in borrowed_books:
                    print(books)
            else:
                "you have not borrowed any books, press 2 in the main menu and enjoy a our selection of books"
        elif choice == '5':  # exits the program
            print('Exiting, thank you for using our library system.')
            break
        else:
            print("Please enter a choice ranging from 1-5.")  # in case user inputs an invalid choice


if __name__ == "__main__":
    func()
# checks if the program is being run directly, if so it will return true and start the main function titled "func"


