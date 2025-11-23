#! usr/bin/python3

import os
from datetime import datetime


def read_balance():
    try:
        if not os.path.exists('balance.txt'):
            with open('balance.txt', 'w') as file:
                file.write('0.00')
            return 0.00
        
        with open('balance.txt', 'r') as file:
            balance = float(file.read().strip())
            return balance
    except ValueError:
        print("Error: Invalid balance format. Resetting to 0.00")
        with open('balance.txt', 'w') as file:
            file.write('0.00')
        return 0.00


def write_balance(balance):
    with open('balance.txt', 'w') as file:
        file.write(f'{balance:.2f}')


def calculate_total_expenses():
    total = 0.00
    
    for filename in os.listdir('.'):
        if filename.startswith('expenses_') and filename.endswith('.txt'):
            try:
                with open(filename, 'r') as file:
                    for line in file:
                        parts = line.strip().split('|')
                        if len(parts) == 5:
                            amount = float(parts[4])
                            total += amount
            except (ValueError, FileNotFoundError):
                continue
    
    return total


def check_balance():
    print("\n" + "-"*20)
    print("BALANCE REPORT")
    print("-"*20)
    
    current_balance = read_balance()
    total_expenses = calculate_total_expenses()
    available_balance = current_balance - total_expenses
    
    print(f"Current Balance:        ${current_balance:,.2f}")
    print(f"Total Expenses to Date: ${total_expenses:,.2f}")
    print(f"Available Balance:      ${available_balance:,.2f}")
    print("-"*20)
    
    while True:
        choice = input("\nWould you like to add money to your balance? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    
    if choice == 'y':
        while True:
            try:
                amount = input("Enter amount to add: $").strip()
                amount = float(amount)
                
                if amount <= 0:
                    print("Error: Amount must be a positive number.")
                    continue
                
                new_balance = current_balance + amount
                write_balance(new_balance)
                
                print(f"\nSuccessfully added ${amount:,.2f} to your balance!")
                print(f"New balance: ${new_balance:,.2f}")
                break
            except ValueError:
                print("Error: Please enter a valid number.")


def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_next_expense_id(date):
    filename = f'expenses_{date}.txt'
    
    if not os.path.exists(filename):
        return 1
    
    max_id = 0
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 5:
                try:
                    expense_id = int(parts[0])
                    max_id = max(max_id, expense_id)
                except ValueError:
                    continue
    
    return max_id + 1


def add_expense():
    print("\n" + "-"*20)
    print("ADD NEW EXPENSE")
    print("-"*20)
    
    current_balance = read_balance()
    total_expenses = calculate_total_expenses()
    available_balance = current_balance - total_expenses
    
    print(f"\n*** AVAILABLE BALANCE: ${available_balance:,.2f} ***\n")
    
    while True:
        date = input("Enter date (YYYY-MM-DD, e.g., 2025-11-07): ").strip()
        if validate_date(date):
            break
        print("Error: Invalid date format. Please use YYYY-MM-DD format.")
    
    while True:
        item = input("Enter item name: ").strip()
        if item:
            break
        print("Error: Item name cannot be empty.")
    
    while True:
        try:
            amount = input("Enter amount paid: $").strip()
            amount = float(amount)
            
            if amount <= 0:
                print("Error: Amount must be a positive number.")
                continue
            
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
    print("\n" + "-"*20)
    print("EXPENSE DETAILS:")
    print("-"*20)
    print(f"Date:   {date}")
    print(f"Item:   {item}")
    print(f"Amount: ${amount:,.2f}")
    print("-"*20)
    
    while True:
        confirm = input("\nConfirm this expense? (y/n): ").strip().lower()
        if confirm in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    
    if confirm == 'n':
        print("Expense cancelled.")
        return
    
    if amount > available_balance:
        print("\nERROR: Insufficient balance! Cannot save expense.")
        print(f"Available balance: ${available_balance:,.2f}")
        print(f"Expense amount:    ${amount:,.2f}")
        print(f"Shortage:          ${amount - available_balance:,.2f}")
        return
    
    expense_id = get_next_expense_id(date)
    
    now = datetime.now()
    current_date = now.strftime('%Y-%m-%d')
    current_time = now.strftime('%H:%M:%S')
    
    filename = f'expenses_{date}.txt'
    with open(filename, 'a') as file:
        file.write(f'{expense_id}|{current_date}|{current_time}|{item}|{amount:.2f}\n')
    
    new_balance = current_balance - amount
    write_balance(new_balance)
    
    print(f"\nExpense saved successfully!")
    print(f"Expense ID: {expense_id}")
    print(f"Saved to: {filename}")
    print(f"Remaining balance: ${new_balance - calculate_total_expenses() + amount:,.2f}")


def display_menu():
    print("\n" + "-"*20)
    print("PERSONAL EXPENSES TRACKER")
    print("-"*20)
    print("1. Check Remaining Balance")
    print("2. View Expenses")
    print("3. Add New Expense")
    print("4. Exit")
    print("-"*20)


def main():
    print("\n" + "*"*20)
    print("WELCOME TO PERSONAL EXPENSES TRACKER")
    print("*"*20)
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            print("\n[Feature 4: View Expenses - Coming soon]")
        elif choice == '3':
            add_expense()
        elif choice == '4':
            print("\n" + "-"*20)
            print("Saving all data...")
            print("Thank you for using Personal Expenses Tracker!")
            print("Goodbye!")
            print("-"*20 + "\n")
            break
        else:
            print("\nInvalid option. Please select a number between 1 and 4.")


main()