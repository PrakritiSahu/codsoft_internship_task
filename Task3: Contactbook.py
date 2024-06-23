class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

contacts = [ ]

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print("Contact added successfully!") 

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if contact.name == search_term or contact.phone == search_term:
            contact.name = input("Enter new name: ")
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            contact.address = input("Enter new address: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")  

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    for contact in contacts:
        if contact.name == search_term or contact.phone == search_term:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if contact.name == search_term or contact.phone == search_term:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")
        select = input("Choose an option: ")
        
        if select == '1':
            add_contact()
        elif select == '2':
            view_contacts()
        elif select == '3':
            update_contact()
        elif select == '4':
            search_contact()
        elif select == '5':
            delete_contact()
        elif select == '6':
            break
        else:
            print("Invalid select. Please try again.")

if __name__ == "__main__":
    main()
