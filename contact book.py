Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print()
            found = True
    if not found:
        print("No contacts found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_phone = input(f"Enter new phone number (current: {contact['phone']}): ")
            new_email = input(f"Enter new email (current: {contact['email']}): ")
            contact['phone'] = new_phone
...             contact['email'] = new_email
...             print("Contact updated successfully!")
...             return
...     print("Contact not found.")
... 
... def delete_contact():
...     name = input("Enter name of contact to delete: ")
...     for i, contact in enumerate(contacts):
...         if contact['name'].lower() == name.lower():
...             del contacts[i]
...             print("Contact deleted successfully!")
...             return
...     print("Contact not found.")
... 
... while True:
...     print("\nContact Book Menu:")
...     print("1. Add Contact")
...     print("2. View Contacts")
...     print("3. Search Contacts")
...     print("4. Update Contact")
...     print("5. Delete Contact")
...     print("6. Exit")
... 
...     choice = input("Enter your choice (1-6): ")
... 
...     if choice == "1":
...         add_contact()
...     elif choice == "2":
...         view_contacts()
...     elif choice == "3":
...         search_contact()
...     elif choice == "4":
...         update_contact()
...     elif choice == "5":
...         delete_contact()
...     elif choice == "6":
...         print("Exiting contact book...")
...         break
...     else:
