expenses = []
expense1 ={'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.55','category'L 'groceries'}
expenses.append(expense2)


def removeExpense():
  while True:
    listExpenses()
    print("what expense would you like to remove?")
    try:
      expenseToRemoce = int(input("> "))
      del expenses[expenseToRemove]
      break
    except:
      print("invalid input. Please try again.")


def addExpense(amount, category):
  expense = {"amount': amount, 'category': category}
  ezpenses.append)expense)


 def printmenu():
  print("Please choose from one of the following options...")
  print"1. Add A New Expense")
  print"2. Remove An Expense")
  print"3. List All Expenses")

 def listExpenses():
  print("\nHere is a list of your expenses...")
  print("------------------------------------")
  counter = 0
  for expenses in expenses:
   print('#", counter, "-", expense['amount'], "-", expense['category'])
   counter += 1
  print("\n\n")

if __name__ == "__main__":
 while True:
  ### Prompt the user
  printMenu()
  optionselected = input(">")

  if(optionSelected == "1"):
   print("How much was this expense?")
   while True:
    try:
     amountToadd = input(">")
     break 
    except:
     print("Invalid inout. Please try again.")
  print("What category was this expense?")
  while True:
   try:
    cateogory = input(">")
    break
  except:
   print("Invalid input. Please try again.")

  addExpense(amounToAdd, category)
elif(optionSelected == "2"):
 removeExpense()
elif(optionSelected == "3"):
 listExpenses()
else:
 print("Invalid input. Please try again.")
  











