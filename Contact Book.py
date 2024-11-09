import json

# A file to store the contact data in JSON format
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    """Save the contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Allow the user to add a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    if name in contacts:
        print("This contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print(f"Contact for {name} added successfully!")

def view_contacts(contacts):
    """Display all contacts with their name and phone number."""
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    """Allow the user to search for a contact by name or phone number."""
    search_term = input("Enter the name or phone number to search: ").strip()
    
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found with that search term.")

def update_contact(contacts):
    """Allow the user to update an existing contact's details."""
    name = input("Enter the contact name to update: ").strip()
    
    if name not in contacts:
        print(f"No contact found with the name {name}.")
        return
    
    print("Enter the new details (leave blank to keep current value):")
    phone = input(f"Phone ({contacts[name]['phone']}): ").strip() or contacts[name]['phone']
    email = input(f"Email ({contacts[name]['email']}): ").strip() or contacts[name]['email']
    address = input(f"Address ({contacts[name]['address']}): ").strip() or contacts[name]['address']
    
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print(f"Contact for {name} updated successfully!")

def delete_contact(contacts):
    """Allow the user to delete a contact."""
    name = input("Enter the contact name to delete: ").strip()
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact for {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}.")

def display_menu():
    """Display the menu options."""
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
def main():
    contacts = load_contacts()
    
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
