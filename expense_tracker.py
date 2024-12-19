class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def remove_expense(self, expense):
        if 0 <= expense < len(self.expenses):
            del self.expenses[expense]
            print("Expense removed")
        else:
            print("Expense not found")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses to display")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i + 1}. {expense.date} - {expense.description} - {expense.amount}")
    
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: {total:.2f}")
    