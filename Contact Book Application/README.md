## Contact Book Application

This is a simple Contact Book Application built using Python and CSV files to manage a list of contacts. 
It allows users to add, view, search, update, delete, export, and import contacts, with basic validation 
for phone numbers and email addresses.

### Features
1. **Add Contact:** Add a new contact with name, phone number, email, and address. The application checks for duplicate contact names before adding.
2. **View Contacts:** Display all saved contacts in the CSV file.
3. **Search Contact:** Search for a specific contact by name.
4. **Update Contact:** Update the phone number, email, or address of an existing contact.
5. **Delete Contact:** Delete a contact by name after confirming with the user.
6. **Export Contacts:** Export all contacts to a separate CSV file.
7. **Import Contacts:** Import contacts from an external CSV file into the main contact list.
8. **Data Validation:** Validate phone numbers to ensure they are digits only and at least 7 digits long. Validate email addresses using a regular expression.

### Project Structure

### How It Works

### *Add Contact*
* When adding a new contact, the program checks if a contact with the same name already exists in the `contacts.csv` file.
* If the contact doesn't exist, it validates the phone number (must be digits and at least 7 characters) and the email format (must be a valid email address).
* If all validations pass, the contact is saved in `contacts.csv`.

### *View Contacts*
* Displays all contacts saved in the `contacts.csv` file. If no contacts exist, it will notify the user that the contact list is empty.

### *Search Contact*
* Allows the user to search for a contact by name. If the contact exists, it will display the details; otherwise, it will notify the user that no contact was found.

### *Update Contact*
* The user can search for a contact to update and modify their phone number, email, and address. If the user chooses not to update a field, they can simply press Enter to keep the old value.

### *Delete Contact*
* Prompts the user for confirmation before deleting a contact by name. If confirmed, the contact is removed from `contacts.csv`.

### *Export Contacts*
* Exports all contacts from `contacts.csv` to `contacts_export.csv`.

### *Import Contacts*
* Allows importing contacts from a file named `contacts_import.csv` into `contacts.csv`.


### Installation
1. **Clone the repository or download the files.**
2. **Ensure you have Python installed (Python 3.x recommended).**
3. **Ensure you have an IDE as well**
4. **Run the application.**

