#!/usr/bin/env python3

import os
from datetime import datetime


def check_balance():
    print("\n" + "-"*20)
    print("BALANCE REPORT")
    print("-"*20)
    
    if os.path.exists('balance.txt'):
        with open('balance.txt', 'r') as f:
            balance = float(f.read().strip())
    else:
        balance = 0.00
        with open('balance.txt', 'w') as f:
            f.write('0.00')
    
    total_expenses = 0.00
    for filename in os.listdir('.'):
        if filename.startswith('expenses_') and filename.endswith('.txt'):
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 5:
                        total_expenses += float(parts[4])
    
    available = balance - total_expenses
    
    print(f"Current Balance:        ${balance:.2f}")
    print(f"Total Expenses to Date: ${total_expenses:.2f}")
    print(f"Available Balance:      ${available:.2f}")
    print("-"*20)
    
    choice = input("\nWould you like to add money to your balance? (y/n): ").strip().lower()
    if choice == 'y':
        amount = float(input("Enter amount to add: $").strip())
        if amount > 0:
            new_balance = balance + amount
            with open('balance.txt', 'w') as f:
                f.write(f'{new_balance:.2f}')
            print(f"\nSuccessfully added ${amount:.2f} to your balance!")
            print(f"New balance: ${new_balance:.2f}")


def add_expense():
    print("\n" + "-"*20)
    print("ADD NEW EXPENSE")
    print("-"*20)
    
    with open('balance.txt', 'r') as f:
        balance = float(f.read().strip())
    
    total_expenses = 0.00
    for filename in os.listdir('.'):
        if filename.startswith('expenses_') and filename.endswith('.txt'):
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split('|')
                    if len(parts) == 5:
                        total_expenses += float(parts[4])
    
    available = balance - total_expenses
    print(f"\n*** AVAILABLE BALANCE: ${available:.2f} ***\n")
    
    date = input("Enter date (YYYY-MM-DD, e.g., 2025-11-07): ").strip()
    item = input("Enter item name: ").strip()
    amount = float(input("Enter amount paid: $").strip())
    
    print("\n" + "-"*20)
    print("EXPENSE DETAILS:")
    print("-"*20)
    print(f"Date:   {date}")
    print(f"Item:   {item}")
    print(f"Amount: ${amount:.2f}")
    print("-"*20)
    
    confirm = input("\nConfirm this expense? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Expense cancelled.")
        return
    
    if amount > available:
        print("\nInsufficient balance! Cannot save expense.")
        return
    
    filename = f'expenses_{date}.txt'
    expense_id = 1
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1].strip().split('|')
                expense_id = int(last_line[0]) + 1
    
    now = datetime.now()
    with open(filename, 'a') as f:
        f.write(f'{expense_id}|{now.strftime("%Y-%m-%d")}|{now.strftime("%H:%M:%S")}|{item}|{amount:.2f}\n')
    
    new_balance = balance - amount
    with open('balance.txt', 'w') as f:
        f.write(f'{new_balance:.2f}')
    
    print(f"\nExpense saved successfully!")
    print(f"Remaining balance: ${new_balance:.2f}")


def view_expenses():
    while True:
        print("\n" + "-"*20)
        print("VIEW EXPENSES")
        print("-"*20)
        print("1. Search by item name")
        print("2. Search by amount")
        print("3. Back to main menu")
        print("-"*20)
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            search_term = input("\nEnter item name to search: ").strip().lower()
            
            print("\n" + "-"*70)
            print(f"SEARCH RESULTS FOR: '{search_term}'")
            print("-"*70)
            
            for filename in sorted(os.listdir('.')):
                if filename.startswith('expenses_') and filename.endswith('.txt'):
                    with open(filename, 'r') as f:
                        for line in f:
                            parts = line.strip().split('|')
                            if len(parts) == 5 and search_term in parts[3].lower():
                                print(f"{parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | ${float(parts[4]):.2f}")
            print("-"*70)
        
        elif choice == '2':
            min_amount = input("\nEnter minimum amount (or press Enter): $").strip()
            min_amount = float(min_amount) if min_amount else 0.00
            max_amount = input("Enter maximum amount (or press Enter): $").strip()
            max_amount = float(max_amount) if max_amount else 999999.00
            
            print("\n" + "-"*70)
            print(f"SEARCH RESULTS FOR: ${min_amount:.2f} - ${max_amount:.2f}")
            print("-"*70)
            
            for filename in sorted(os.listdir('.')):
                if filename.startswith('expenses_') and filename.endswith('.txt'):
                    with open(filename, 'r') as f:
                        for line in f:
                            parts = line.strip().split('|')
                            if len(parts) == 5:
                                amount = float(parts[4])
                                if min_amount <= amount <= max_amount:
                                    print(f"{parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | ${amount:.2f}")
            print("-"*70)
        
        elif choice == '3':
            break


def main():
    print("WELCOME TO PERSONAL EXPENSES TRACKER")
    
    while True:
        print("\n" + "-"*20)
        print("PERSONAL EXPENSES TRACKER")
        print("\n"*2)
        print("1. Check Remaining Balance")
        print("2. View Expenses")
        print("3. Add New Expense")
        print("4. Exit")
        print("-"*20)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            add_expense()
        elif choice == '4':
            print("\n" + "-"*20)
            print("Saving all data...")
            print("Thank you for using Personal Expenses Tracker!")
            print("Goodbye!")
            print("-"*20 + "\n")
            break


main()