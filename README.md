# Expense-Tracker.python
Daily Expense Tracker
This is a Tkinter-based desktop application designed to help you track and manage your daily expenses. The app uses a simple SQLite database for storing and retrieving records, allowing users to add, view, update, and delete their transactions efficiently.

Features
Add Expense: Input details such as item name, price, and the date of purchase.
View Expense History: A table view that displays all recorded expenses.
Update/Delete Records: Easily modify or remove records from the database.
Calculate Total Expenses and Remaining Balance: Track your total expenditure and check your remaining balance.
Real-time Date Setting: Automatically set the current date for easier entry of new expenses.
Installation
Clone the repository:

bash

cd expense-tracker
Install required libraries:

bash
Copy code
pip install tkinter
Run the script:

bash
Copy code
python expense_tracker.py
Usage
Add a Record: Fill in the item name, price, and date of purchase, then click "Save Record."
View Records: All expenses are listed in the table below. Scroll to see older records.
Update a Record: Click on a row to select it, modify the details in the input fields, and click "Update."
Delete a Record: Select a row and click "Delete" to remove the entry.
Check Balance: Click "Total Balance" to view your total expense and the remaining balance (assumed from an initial balance of ₹5000).
Screenshots
[Include screenshots or images showcasing the interface and features]

File Structure
expense_tracker.py: Main Python file containing the Tkinter GUI and all functional logic.
mydb.py: Contains the Database class that handles SQLite operations (insert, fetch, update, delete).
test.db: The SQLite database file storing your expense records.
Dependencies
Python 3.x
Tkinter (comes with Python by default)
SQLite (built-in with Python)
ttk (Themed Tkinter widgets)
Future Improvements
Add categories for expenses (e.g., Food, Entertainment, Bills, etc.)
Provide graphical insights such as pie charts for expenses.
Enable exporting reports to CSV or Excel format.
Add user authentication for personalized expense tracking.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please create an issue or submit a pull request for any feature enhancements or bug fixes.

Author

Debapratim Bhattacharjee

