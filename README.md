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
- **Archive**: Move expense files to organized directory structure (`expenses/YYYY/MM/`)
- **Search**: Find and display archived expenses by date
- **Logging**: All operations logged with timestamps to `archive_log.txt`

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


**Enjoy Expense Tracking!**