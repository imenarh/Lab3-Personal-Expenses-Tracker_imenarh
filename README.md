# Lab3-Personal-Expenses-Tracker_imenarh

## Overview

A command-line application that helps users track their daily expenses, manage their balance, and generate expense records. The project combines Python for the main application and shell scripting for file management.

---

## Features

### Python Application
- **Main Menu System**: Interactive CLI with 4 options
- **Check Balance**: View current balance, total expenses, and add money
- **Add Expense**: Record new expenses with validation and confirmation
- **View Expenses**: Search expenses by item name or amount range

### Shell Script
- **Archive**: Move expense files to organized directory structure (`expenses/YYYY/MM/`)
- **Search**: Find and display archived expenses by date
- **Logging**: All operations logged with timestamps to `archive_log.txt`

---

## File Structure

```
Lab3-Personal-Expenses-Tracker_imenarh/
├── expenses-tracker.py          # Main Python application
├── expense_report.sh            # Shell script for archiving
├── balance.txt                  # Current balance storage
├── README.md                    # This file
│
├── expenses_YYYY-MM-DD.txt      # Daily expense files (auto-generated)
├── archive_log.txt              # Archive operation logs (auto-generated)
│
└── expenses/                    # Archive directory (auto-generated)
    └── YYYY/MM/                 # Organized by year/month
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/imenarh/Lab3-Personal-Expenses-Tracker_imenarh.git
   cd Lab3-Personal-Expenses-Tracker_imenarh
   ```

2. **Set script permissions**:
   ```bash
   chmod +x expense_report.sh
   ```

---

## Usage

### Running the Python Application

```bash
python3 expenses-tracker.py
```

**Main Menu Options**:
1. **Check Remaining Balance** - View financial summary and add money
2. **View Expenses** - Search and view expense records
3. **Add New Expense** - Record a new expense
4. **Exit** - Save and quit

### Using the Archive Script

**Archive an expense file**:
```bash
./expense_report.sh archive 2025-11-07
```

**Search archived expenses**:
```bash
./expense_report.sh search 2025-11-07
```

**Get help**:
```bash
./expense_report.sh help
```

---

## Data Format

### balance.txt
```
1000.00
```
Single line containing the current balance.

### expenses_YYYY-MM-DD.txt
```
ID|Date|Time|Item|Amount
1|2025-11-23|14:30:45|Groceries|45.50
2|2025-11-23|16:20:10|Coffee|5.75
```
Pipe-delimited format with sequential IDs per day.

### archive_log.txt
```
[2025-11-23 14:07:30] ARCHIVED: expenses_2025-11-07.txt to expenses/2025/11/
[2025-11-23 14:10:15] SEARCHED: expenses/2025/11/expenses_2025-11-07.txt
```
Timestamp-based log of all archive operations.

---

## Examples

### Adding an Expense

```
--------------------
ADD NEW EXPENSE
--------------------

*** AVAILABLE BALANCE: $1,000.00 ***

Enter date (YYYY-MM-DD, e.g., 2025-11-07): 2025-11-23
Enter item name: Lunch
Enter amount paid: $15.50

--------------------
EXPENSE DETAILS:
--------------------
Date:   2025-11-23
Item:   Lunch
Amount: $15.50
--------------------

Confirm this expense? (y/n): y

Expense saved successfully!
Expense ID: 1
Saved to: expenses_2025-11-23.txt
Remaining balance: $984.50
```

### Searching Expenses

```
--------------------
VIEW EXPENSES
--------------------
1. Search by item name
2. Search by amount
3. Back to main menu
--------------------
Select an option (1-3): 1

Enter item name to search: lunch

--------------------------------------------------------------------------------
SEARCH RESULTS FOR: 'lunch'
--------------------------------------------------------------------------------
ID    Date         Time       Item                           Amount
--------------------------------------------------------------------------------
1     2025-11-23   14:30:45   Lunch                          $    15.50
2     2025-11-24   12:15:30   Business Lunch                 $    45.00
--------------------------------------------------------------------------------
Total: 2 expense(s) found | Total Amount: $60.50
--------------------------------------------------------------------------------
```

---

## Key Features

### Validation
- Date format validation (YYYY-MM-DD)
- Positive number validation for amounts
- File existence checks
- Balance sufficiency checks
- Empty input prevention

### Error Handling
- Try-catch blocks for file operations
- Graceful handling of missing files
- Invalid input recovery
- Detailed error messages

### Data Persistence
- Automatic file creation
- Balance updates after each transaction
- Sequential ID generation per day
- Organized file structure

---

## Requirements

- **Python**: 3.6 or higher
- **Operating System**: Ubuntu/Linux with Bash shell
- **No external libraries required** - Uses only Python standard library

---

## Author

**Imen Arh**
- GitHub: [@imenarh](https://github.com/imenarh)
- Repository: [Lab3-Personal-Expenses-Tracker_imenarh](https://github.com/imenarh/Lab3-Personal-Expenses-Tracker_imenarh)

---

## License

This project is created for educational purposes as part of the Introduction to Python Programming and Databases course at African Leadership University.

---

**Happy Expense Tracking! 💰📊**
