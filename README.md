# Lab3-Personal-Expenses-Tracker_imenarh

## Overview

A command-line application that helps users track their daily expenses, manage their balance, and generate expense records. The project combines Python for the main application and shell scripting for file management.

## Features

### Python Script Application
- **Main Menu System**: Interactive CLI with 4 options
- **Check Balance**: View current balance, total expenses, and add money
- **Add Expense**: Record new expenses with validation and confirmation
- **View Expenses**: Search expenses by item name or amount range

### Shell Script Features
- **Interactive Menu**: Easy-to-use menu for archiving and searching
- **Auto-Archive**: Automatically moves all `expenses_*.txt` files to `archives/` folder
- **Search**: Find archived expenses by date
- **Logging**: Operations logged to `archive_log.txt`

## Usage

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/imenarh/Lab3-Personal-Expenses-Tracker_imenarh.git
   cd Lab3-Personal-Expenses-Tracker_imenarh
   ```

### Running the Python Application

```bash
python3 expenses-tracker.py
```

**Main Menu Options**:
1. **Check Remaining Balance**
2. **View Expenses**
3. **Add New Expense**
4. **Exit**

### Using the Archive Script

Run the script and follow the on-screen prompts:

```bash
./expense_report.sh
```

**Options:**
1. **Archive**: Moves all current `expenses_*.txt` files to the `archives/` folder.
2. **Search**: Asks for a date and shows any matching archived records.

**Enjoy Expense Tracking!**