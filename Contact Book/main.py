import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact\n2. View All\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email (optional): ").strip()
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            print("Saved.")

        elif choice == "2":
            if not contacts:
                print("No contacts saved yet.")
            else:
                for name, info in contacts.items():
                    print(f"{name} | {info['phone']} | {info['email']}")

        elif choice == "3":
            query = input("Search name: ").strip().lower()
            found = False
            for name, info in contacts.items():
                if query in name.lower():
                    print(f"{name} -> {info['phone']} ({info['email']})")
                    found = True
            if not found:
                print("Contact not found.")

        elif choice == "4":
            name = input("Enter exact name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Deleted.")
            else:
                print("No such contact.")

        elif choice == "5":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()