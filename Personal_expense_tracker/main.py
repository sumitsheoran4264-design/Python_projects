from expenses_txt import project_logo
print(project_logo)

 #total of all expenses

# for desplay menu
def menu():
    """function for display menu."""
    print("# Menu\n1. Add Expense\n2. View Expenses\n3. Calculate Total\n4. Search by Category\n5. Exit\n")


 
def add_expense(name, price, category):
    '''this function return dictionary of expenses.'''
    expense = {"name": name,
               "price": price,
               "category": category}
    return expense

def expense_format(expenses):
    for expense in expenses:
        name = expense['name']
        price = expense['price']
        category = expense['category']
        print(f"Name      : {name}\nPrice     : {price}\nCategory  : {category}\n")

    

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['price']
    return total

def search_by_category(expenses):
    choose_category = input("Enter category: ").lower()
    for expense in expenses:
        if choose_category == expense["category"]:
            print(expense)
    






expenses = []

is_program_running = True
while is_program_running:
    print("\n")
    menu()
    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        expense_name = input("Enter Expense Name: ").lower()
        expense_price = int(input("Enter Expense Price: $ "))
        expense_category = input("Enter Category: ").lower()
        dict_of_expenses = add_expense(expense_name, expense_price, expense_category)
        expenses.append(dict_of_expenses)
        
    elif choice == 2:
        expense_format(expenses)

    elif choice == 3:
        print(f"The total amount of expenses is: ${calculate_total(expenses)}")
    
    elif choice == 4:
        (search_by_category(expenses))

    elif choice == 5:
        print("Thank you for using Personal Expense Tracker!")
        is_program_running = False

    else:
        print("Please enter a valid choice.")
