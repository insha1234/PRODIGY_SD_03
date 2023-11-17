import json

class ContactManagementSystem:
    def _init_(self):
        self.contacts = {}

    def save_contacts_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass  

    def add_contact(self, name, phone_number, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email}
            print(f"Contact added: {name} - {phone_number} - {email}")
        else:
            print(f"Contact {name} already exists.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for name, contact_info in self.contacts.items():
                print(f"{name} - Phone: {contact_info['phone_number']} - Email: {contact_info['email']}")

    def edit_contact(self, name, new_phone_number, new_email):
        if name in self.contacts:
            self.contacts[name]['phone_number'] = new_phone_number
            self.contacts[name]['email'] = new_email
            print(f"Contact updated: {name} - {new_phone_number} - {new_email}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted: {name}")
        else:
            print(f"Contact {name} not found.")

contact_manager = ContactManagementSystem()
contact_manager.load_contacts_from_file('contacts.json')  
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save and Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_manager.add_contact(name, phone_number, email)

    elif choice == '2':
        contact_manager.view_contacts()

    elif choice == '3':
        name = input("Enter the name of the contact to edit: ")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        contact_manager.edit_contact(name, new_phone_number, new_email)

    elif choice == '4':
        name = input("Enter the name of the contact to delete: ")
        contact_manager.delete_contact(name)

    elif choice == '5':
        contact_manager.save_contacts_to_file('contacts.json')
        print("Contacts saved. Exiting.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
