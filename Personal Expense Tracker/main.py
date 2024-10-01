
from expense import Expense
from tracker import ExpenseTracker
from utils import validate_amount

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. List All Expenses")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter expense name: ")
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")

            try:
                amount = validate_amount(amount)
                expense = Expense(name, amount, category)
                tracker.add_expense(expense)
            except ValueError as e:
                print(e)

        elif choice == '2':
            total = tracker.get_total_expenses()
            print(f"Total Expenses: {total}")

        elif choice == '3':
            tracker.list_expenses()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
