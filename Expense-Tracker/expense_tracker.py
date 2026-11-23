import json
import os

FILE_NAME = "expenses.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_data(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    item = input("Enter item name: ").strip()
    category = input("Enter category (Food, Travel, etc.): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return

    expenses.append({
        "item": item,
        "category": category,
        "amount": amount
    })
    save_data(expenses)
    print("Expense added.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['item']} ({exp['category']}) - Rs.{exp['amount']}")

def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spent: Rs.{total:.2f}")

def main():
    expenses = load_data()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Total Spent\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Wrong choice, try again.")

if __name__ == "__main__":
    main()