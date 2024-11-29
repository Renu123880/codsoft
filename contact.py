# Contact Book Application

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, details in self.contacts.items():
                print(f"{name} - {details['phone']}")
            print("--------------------")

    def search_contact(self, search_term):
        found = [
            {name: details} for name, details in self.contacts.items()
            if search_term.lower() in name.lower() or search_term in details["phone"]
        ]
        if found:
            print("\n--- Search Results ---")
            for contact in found:
                for name, details in contact.items():
                    print(f"Name: {name}")
                    print(f"Phone: {details['phone']}")
                    print(f"Email: {details['email']}")
                    print(f"Address: {details['address']}\n")
            print("---------------------")
        else:
            print("No contact found.")

    def update_contact(self, name):
        if name in self.contacts:
            print("Enter new details (leave blank to keep unchanged):")
            phone = input("New phone: ") or self.contacts[name]["phone"]
            email = input("New email: ") or self.contacts[name]["email"]
            address = input("New address: ") or self.contacts[name]["address"]
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    book = ContactBook()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone to search: ")
            book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            book.update_contact(name)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            book.delete_contact(name)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
