from expense_tracker import *

def main():
    # Create an instance of the ExpenseTracker class
    tracker = ExpenseTracker()

    # Display the menu
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        # Get the user's choice
        choice = input("Enter choice (1-5): ")

        # Perform the desired action
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
        
        elif choice == "2":
            index = int(input("Enter the expense number to remove: ")) - 1
            tracker.remove_expense(index)
        
        elif choice == "3":
            tracker.view_expenses()
        
        elif choice == "4":
            tracker.total_expenses()
        
        elif choice == "5":
            print ("Exiting...")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


