def main():
    # Ask for total monthly budget
    try:
        budget_input = input("Enter your total monthly budget: ")
        total_budget = float(budget_input)
        
        total_expenses = 0.0
        print("Enter your expenses one by one. Type 'done' to finish.")
        
        while True:
            expense_input = input("Enter expense (or 'done'): ").strip().lower()
            
            if expense_input == 'done':
                break
                
            try:
                expense = float(expense_input)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a numerical value or 'done'.")

        # Calculate remaining balance
        remaining_balance = total_budget - total_expenses

        # Display the results
        print(f"\nTotal Budget: {total_budget:.2f}")
        print(f"Total Expenses: {total_expenses:.2f}")
        print(f"Remaining Balance: {remaining_balance:.2f}")

        # Check for low funds warning
        if remaining_balance < 500:
            print("Warning: Low Funds")

    except ValueError:
        print("Invalid input. Please enter a numerical value for the total budget.")

if __name__ == "__main__":
    main()
