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
    
    def remove_expense(self, expense_id):
        self.cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
        expense = self.cursor.fetchone()
        if expense is None:
            print("Error: Expense ID not found")
        else:
            self.cursor.execute('''
                DELETE FROM expenses WHERE id = ?
            ''', (expense_id,))
            self.conn.commit()
            print("Expense removed")

    def view_expenses(self):
        self.cursor.execute('SELECT * FROM expenses')
        expenses = self.cursor.fetchall()
        if len(expenses) == 0:
            print("No expenses to display")
        else:
            print("Expenses:")
            for exp in expenses:
                print(f"{exp[0]}. {exp[1]} - {exp[2]} - {exp[3]}")
    
    def total_expenses(self):
        self.cursor.execute('SELECT SUM(amount) FROM expenses')
        total = self.cursor.fetchone()[0]
        print(f"Total expenses: {total:.2f}")
    
    def __del__(self):
        self.conn.close()
        print("Database connection closed")
    