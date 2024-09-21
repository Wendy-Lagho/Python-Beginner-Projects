import contact_book  # Importing the contact_book module

def main():
    print("Welcome to the Contact Book Application!")

    while True:
        print("\nAvailable options: Add, View, Search, Update, Delete, Exit")
        choice = input("Choose an option: ").lower()
        if choice == 'add':
            contact_book.add_contact()  # Call the function from the module
        elif choice == 'view':
            contact_book.view_contacts()
        elif choice == 'search':
            name = input("Enter a name to search: ")
            contact_book.search_contact(name)
        elif choice == 'update':
            name = input("Enter a name to update: ")
            contact_book.update_contact(name)
        elif choice == 'delete':
            name = input("Enter a name to delete: ")
            contact_book.delete_contact(name)
        elif choice == 'exit':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
