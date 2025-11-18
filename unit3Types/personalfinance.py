'''
Personal Finance Manager
Program: presonalfinance.py
Author: Berry gavigan
Date: 11/18/25

This progrma demonstrates proper Python program structre usiong a main() function and helper functions to corrdinate progream flow.
'''

def display_header():
    '''
    Display the program header and welcome message

    This fuction has no parameters and returns nothing.
    Only for display purposes
    '''

    print("\n\n\n")
    print("=" * 50)
    print("              PERSONAL FINANCE MANAGER")
    print("              Plan your college budget!")
    print("=" * 50)
    print("")

def get_user_name():
    '''
    Get the user's name

    Returns:
        name (str): the user's name

    NOTE: We use a separater finction for this to keep each function doing ONE speific task
    '''

    name = input("What is your name? ")
    return name

def get_income():
    '''
    Get and retirn the user's monthly income

    Returns:
        Income (float): Monthly income ot dollars

    NOTE: We convert to a float to handle decimal values and to enable mathmatical operations
    '''
    print("Enter your monthly income: $", end="")
    income_str = input()
    income = float(income_str)
    return income


def get_expenses():
    '''
    Collect all expense catergorys from the user

    Returns:
        expenses_dict (dict): Dictonary with expense categories
        total_expesnes (float): Sum of all expenses

        NOTE: This function demonstrates collecting muliple related inputs and organizing them in a dictionary for easy access later
    '''

    print("\n--- EXPENSES TRACKING ---")
    # Dictionary to store all expenses
    expenses = {}

    # Get each expense category
    print("Enter your rent/housing cost: $", end="")
    expenses['Rent/Housing'] = float(input())

    print("Enter your food and grocery buget: $", end="")
    expenses['Food/Grocery'] = float(input())

    print("Enter your transportation costs: $", end="")
    expenses['Transportation'] = float(input())

    print("Enter you entertainment budget: $", end="")
    expenses['Entertainment'] = float(input())

    print("Enter your savings goal: $", end="")
    expenses['Savings'] = float(input())

    print("Enter miscellaneous expenses: $", end="")
    expenses['Miscellaneous'] = float(input())

    # Calculate total expenses
    total = sum(expenses.values())

    # Return dictonary and total
    return expenses, total

def calcylate_remaining(income, expenses):
    pass

def provide_feedback(remaining, income):
    pass

def display_summary(name, income, expenses_dict, total_expenses, remaining, feedback):
    pass

def main():
    '''
    Main function -coordinates the entire program

    Notice how main() reads like a story:
    1. Display header
    2. Get user info
    3. Get expenses
    4. Calculate results
    5. Get feedback
    6. Display summary
    7. Say goodbye

    Each step is one fuction call, making the logic easy to follow.
    '''

    # Display welcome
    display_header()
    print("Welcome! Let's track your monthly finances.\n")

    # Get user info
    user_name = get_user_name()
    monthly_income = get_income()

    # Get expense information
    # NOTE: This function returns TWO values (tuple unpacking
    expense_catergories, total_expenses = get_expenses()

if __name__ == "__main__":
    main()