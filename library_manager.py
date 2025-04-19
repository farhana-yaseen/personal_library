import json
import os           # handle file system, directories, environment variables etc

print("Personal Library Manager")

# create json file
libraryName = "personal_library.json"

# *************************************************************************************************************************

#     """Load the library from the JSON file. """
def load_library() :
    # Check if a path exists:
    if os.path.exists(libraryName) :
        with open(libraryName, "r") as file :  # r means read
            return json.load(file)
    else : 
        return []
    

# *************************************************************************************************************************

# """Save the current state of the library to the JSON file. (if not then create)"""
def save_library(library):
    with open(libraryName, "w") as file : # w means write
        # serializes the data to JSON format, and writes it to the file with readable formatting (indentation).
        json.dump(library, file, indent=4)  

# *************************************************************************************************************************

# add books in library
def add_book(library) :
    title = input("Enter Book Title: ")
    author = input("Enter Book Author Name: ")
    publication_year = int(input("Enter Publication Year: "))
    genre = input("Enter Book Category: ") # "genre" refers to the category or type of books 
    status = input("Have you read this book (Yes/No: ")

    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "status": status
    }

    library.append(book)
    save_library(library)
    print(f"Book {title} added successfully!!!")

# *************************************************************************************************************************
    
# Delete Book from Library
def delete_book(library):
    title = input("Enter the title of the book to remove: ").lower()

    for book in library :
        if book["title"].lower() == title :
            library.remove(book)
            save_library(library)
            print(f"\n🗑️ Book '{title}' removed successfully!\n")
            break
    else:
        print(f"\n❌ Book '{title}' not found.\n")

# *************************************************************************************************************************

# use for multiple time print
def print_book(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Publishing Year: {book['publication_year']}, Genre: {book['genre']}, Reading Status: {book['status']}")

# *************************************************************************************************************************

# search for a Book
def search_book(library):
    keyword = input("Enter title or author to search: ").lower()

    found = [book_keyword for book_keyword in library if keyword in book_keyword["title"].lower() or keyword in book_keyword["author"].lower()]

    if found :
        print("\n🔎 Search Results:")
        for book in found :
            print_book(book)
    else:
        print("\n❌ No matching books found.")

# *************************************************************************************************************************

# Display all Books
def display_book(library) :
    if library :
        print("\n📖 All Books in Library:")

        for book in library :
            print_book(book)

    else:
        print("\n📭 Your library is empty!")

# *************************************************************************************************************************

# Display statistics (total books, percentage read)
def statistics(library):

    total_books = len(library)

    if total_books == 0 :
        print("\n📊 Library Statistics:")
        print("No books in the library to calculate statistics.\n")
        return

    read_books = len([book for book in library if book["status"].lower() == "yes"])
    unread_books = total_books - read_books
    read_percentage = read_books / total_books * 100

# print all statistic
    print(f"\n📊 Library Statistics:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    print(f"Percentage read: {read_percentage:.2f}%\n")

# *************************************************************************************************************************

# main function
def main() :
    library = load_library()

    while True :
        print("\n====== Menu ======")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics (total books, percentage read)")
        print("6. Exit")

        user_choice:int = input("Select an option (1-6): ")

        if user_choice == "1" :
            add_book(library)
        elif user_choice == "2" :
            delete_book(library)
        elif user_choice == "3" :
            search_book(library)
        elif user_choice == "4" :
            display_book(library)
        elif user_choice == "5" :
            statistics(library)
        elif user_choice == "6" :
            print("👋 Exiting the program. Goodbye!")
            break
        else: 
            print("❗ Invalid option. Please select a number from 1 to 6.\n")

main()



