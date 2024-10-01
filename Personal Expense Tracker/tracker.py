# tracker.py

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Added: {expense}")

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def list_expenses(self):
        for expense in self.expenses:
            print(expense)
