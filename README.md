# expense-tracker

## overview
"Welcome to our expense tracker project!" This tool is designed to help users manage their finances accodingly to everyones individual goals. It enables you to categorize, record and track expenses effortlessly. It will provide insight into your spending habits and help assist with your financial goals. Get started, get organized, and take control of your expenses. 

## Usage 

  '''bash
  git clone https://www.youtube.com/watch?v=-adT3bRWchI
  '''

  Navigate to the project directory 

  '''bash 
  cd expense-tracker
  '''

Run the script

  '''bash
  Pytho expense_tracker.py
  '''
## Features 
  **Add Expense:** you can add expenses by specifying the category and the amount.
  ** view Total Expenses:** check the total expense incurred.
  **view Expenses by Category:** see the expenses for a specific category.
## Example 
'''python 
# Example usage 
tracker = ExpenseTracker()

tracker.add.expense('food',50.75)
tracker.add.expense("transportation",30.50)
tracker.add.expense('food", 20.25) # additional expense in the "food" category 

print('Total Expenses: $",tracker.total. expenses())
print('\nAll Expenses:)
tracker.view_expenses()
categoru_to_view + "food"
print(f"\nViewing expenses for (catefory_to_view:")
tracker.view.expenses_by_category(category_to_view)
