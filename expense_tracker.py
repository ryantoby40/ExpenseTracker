import sqlite3

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                description TEXT,
                amount REAL
            )
        ''')
        self.conn.commit()

    def add_expense(self, expense):
        self.cursor.execute('''
            INSERT INTO expenses (date, description, amount)
            VALUES (?, ?, ?)
        ''', (expense.date, expense.description, expense.amount))
        self.conn.commit()
        print("Expense added")
    
    def remove_expense(self, expense):
        self.cursor.execute('''
            DELETE FROM expenses WHERE id = ?
        ''', (expense.id,))
        self.conn.commit()
        print("Expense removed")

    def view_expenses(self):
        self.cursor.execute('SELECT * FROM expenses')
        expenses = self.cursor.fetchall()
        if len(expenses) == 0:
            print("No expenses to display")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{expense[0]}. {expense[1]} - {expense[2]} - {expense[3]}")
    
    def total_expenses(self):
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        total = self.cursor.fetchone()[0]
        print(f"Total expenses: {total:.2f}")
    
    def __del__(self):
        self.conn.close()
        print("Database connection closed")
    