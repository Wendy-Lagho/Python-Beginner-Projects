import csv
import re

"""
Contact functions: add, view, search, update, delete
"""

def add_contact():
    with open('contacts.csv', 'a+', newline='') as csvfile:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Go back to start of file to check for duplicates
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        name = input("Enter contact name: ")

        for row in reader:
            if row['name'].lower() == name.lower():
                print(f"Contact with name {name} already exists.")
                return

        phone = input("Enter contact phone: ")
        if not validate_phone(phone):
            return

        email = input("Enter contact email: ")
        if not validate_email(email):
            return

        address = input("Enter contact address: ")
        writer.writerow({'name': name, 'phone': phone, 'email': email, 'address': address})
        print(f"Contact {name} added successfully.")

def view_contacts():
    try:
        with open('contacts.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            print("\nContacts List:")
            for row in reader:
                print(f"Name: {row['name']}, Phone: {row['phone']}, Email: {row['email']}, Address: {row['address']}")
    except FileNotFoundError:
        print("No contacts found. The contact list is empty.")


def search_contact(name):
    try:
        with open('contacts.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'].lower() == name.lower():
                    print(f"Found contact: Name: {row['name']}, Phone: {row['phone']}, Email: {row['email']}, Address: {row['address']}")
                    return
            print(f"No contact found with name: {name}")
    except FileNotFoundError:
        print("Contact list is empty.")


def update_contact(name):
    contacts = []
    contact_found = False

    try:
        with open('contacts.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'].lower() == name.lower():
                    contact_found = True
                    print(f"Updating contact {name}")
                    row['phone'] = input(f"Enter new phone (Current: {row['phone']}): ") or row['phone']
                    row['email'] = input(f"Enter new email (Current: {row['email']}): ") or row['email']
                    row['address'] = input(f"Enter new address (Current: {row['address']}): ") or row['address']
                contacts.append(row)

        if contact_found:
            with open('contacts.csv', 'w', newline='') as csvfile:
                fieldnames = ['name', 'phone', 'email', 'address']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(contacts)
                print(f"Contact {name} updated successfully.")
        else:
            print(f"No contact found with name: {name}")

    except FileNotFoundError:
        print("Contact list is empty.")


def delete_contact(name):
    confirm = input(f"Are you sure you want to delete {name}? (yes/no): ").lower()
    if confirm == 'yes':
        contacts = []
        contact_found = False

        try:
            with open('contacts.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'].lower() != name.lower():
                        contacts.append(row)
                    else:
                        contact_found = True

            if contact_found:
                with open('contacts.csv', 'w', newline='') as csvfile:
                    fieldnames = ['name', 'phone', 'email', 'address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(contacts)
                    print(f"Contact {name} deleted successfully.")
            else:
                print(f"No contact found with name: {name}")

        except FileNotFoundError:
            print("Contact list is empty.")
    else:
        print("Deletion canceled.")


def validate_phone(phone):
    if phone.isdigit() and len(phone) >= 7:
        return True
    else:
        print("Invalid phone number. Please enter digits only and a minimum of 7 digits.")
        return False

def validate_email(email):
    # Simple email validation using regex
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        print("Invalid email address format.")
        return False

def export_contacts():
    try:
        with open('contacts.csv', 'r') as csvfile:
            with open('contacts_export.csv', 'w', newline='') as export_file:
                reader = csv.reader(csvfile)
                writer = csv.writer(export_file)
                for row in reader:
                    writer.writerow(row)
        print("Contacts exported successfully to contacts_export.csv.")
    except FileNotFoundError:
        print("No contacts to export.")

def import_contacts():
    try:
        with open('contacts_import.csv', 'r') as importfile:
            with open('contacts.csv', 'a+', newline='') as csvfile:
                reader = csv.reader(importfile)
                writer = csv.writer(csvfile)
                for row in reader:
                    writer.writerow(row)
        print("Contacts imported successfully from contacts_import.csv.")
    except FileNotFoundError:
        print("No contacts_import.csv file found.")

