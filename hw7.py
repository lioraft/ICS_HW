########################################################
# Intro to CS - Assignment 7
# replace the exception raising in each function with your solution
################### GOOD LUCK ##########################
########################################################
from functools import reduce
########################################################
# Q1:
########################################################
# 1
def get_months_under_limit(monthly_shopping_costs, monthly_limit):
    """
    Takes in a dictionary with months as keys and monthly expenses as values, and a monthly limit as int, and returns a
    list of the months in which the expenses were under the limit.
    Args:
        monthly_shopping_costs(Dict(str, List(int))): A dictionary with string keys and list of integers values. it
        contains the expenses of each month.
        monthly_limit: An integer. it represents the monthly limit.
    Returns: A list of strings. the list contains the month in which the expenses were under the limit.
    """
    return list(filter(lambda element: element is not None, list(map(lambda lst: lst[0] if sum(lst[1]) <= monthly_limit else None, list(monthly_shopping_costs.items())))))
# 2
def sum_under_limit_number_of_purchases(monthly_shopping_costs, max_number_of_purchases):
    """
    Takes in a dictionary with months as keys and monthly expenses as values, and a maximum number of purchases as int,
    and returns the total expenses.

    Args:
        monthly_shopping_costs(Dict(str, List(int))): A dictionary with string keys and list of integers values. it
        contains the expenses of each month.
        max_number_of_purchases: An integer. it represents the maximum number of purchases.
    Returns: If in each month all the expenses were under the maximum number of purchases, the function returns the
    sum of the expenses. Else, the function returns -inf.
    """
    return reduce(lambda x, y: x + y, reduce(lambda x, y: x + y, monthly_shopping_costs.values())) if all(map(lambda lst: len(lst[1]) <= max_number_of_purchases, monthly_shopping_costs.items())) else float('-inf')
# 3
def verify_monthly_monotonic_growing_expenses(monthly_shopping_costs):
    """
    Takes in a dictionary with months as keys and monthly expenses as values, and returns whether the expenses
    grow monotonically each month.
    Args:
        monthly_shopping_costs(Dict(str, List(int))): A dictionary with string keys and list of integers values. it
        contains the expenses of each month.
    Returns: if the expenses in all of the months grow monotonically, the function returns True. else, the function
    returns False.
    """
    return list(map(lambda lst: lst[1], list(monthly_shopping_costs.items()))) == list(map(lambda lst: sorted(lst[1]), list(monthly_shopping_costs.items())))

# 4
def divide_monthly_bills(apartment_bills, bob_weekly_income):
    """
    Takes in a dictionary with services and a list of the expenses of each service, and bob's weekly income,
    and returns a string that contain who would pay the expenses of each month.
    Args:
        apartment_bills(Dict(str, List(int))): A dictionary with string keys and list of integers values. The keys are
        the services which bob and alice used, and the values are the expenses of each service.
        bob_weekly_income(int): An integer. it is bob's weekly income.
    Returns: A string that contains who should pay for each one of the services. If expenses were under bob's weekly
    income, bob pays. if the expenses were above bob's weekly income, alice pays.
    """
    return ", ".join(list(map(lambda lst: "Bob: " + lst[0] if sum(lst[1]) <= bob_weekly_income else "Alice: " + lst[0], list(apartment_bills.items()))))


########################################################
# Q2:
########################################################
# 1
def operations_parser_function(code):
    """
    Takes in a string, return the function the suitable function.
    Args:
        code(str): a string of two chars.
    Returns: if the sum of the digits in the string is 1, the function returns adding function. else, the function returns
    multiplication function.
    """
    def add_func(num1, num2):
        return num1 + num2

    def mul_func(num1, num2):
        return num1 * num2

    num1, num2 = int(code[0]), int(code[1])
    return add_func if num1 + num2 == 1 else mul_func

# 2
def triplets_structure_checker(triplets):
    """
    Takes in a tuple of strings, returns if its in the right structure
    Args:
         triplets (tuple(str)): A tuple of strings. each string consists of 3 chars.
    Returns:
         A boolean: if the structure is valid, returns True. if not valid, False.
    """
    # The length of each triplet should be 3
    if len(triplets) != 3:
        return False
    valid_str = lambda t, i, j: t[i][j] == "0" or t[i][j] == "1"
    # Checking that the triplet is in the right order: number, arithmetic function, number.
    # And checking that each string is binary (only has 0 or 1)
    if triplets[0][0] != "0" or not valid_str(triplets, 0, 1) or not valid_str(triplets, 0, 2):
        return False
    if triplets[1][0] != "1" or not valid_str(triplets, 1, 1) or not valid_str(triplets, 1, 2):
        return False
    if triplets[2][0] != "0" or not valid_str(triplets, 2, 1) or not valid_str(triplets, 2, 2):
        return False
    # If structure is valid, returns True
    return True

def binary_code_compiler(lines_of_code_triplets, value_parser, operations_parser):
    """
    Takes in a list of tuples of strings, a value parser and an operations parser, and returns the sum of all the code lines
    of the list.
    Args:
        lines_of_code_triplets (List(Tuple(str, str, str)): A list of tuples, each tuple consists of strings that contain 3 chars and
        represent a code line: the first and third string represent numbers, the second string represent an arithmetic function.
        value_parser (function): A function that receives a string of two chars, and returns a float which is their value.
        operations_parser (function): A function that receives a string of two chars, and returns a function that
        receives two float.
    Returns: If the lines of the code are valid, the function returns the sum of all the code lines. If one of the
    lines is not valid, the function returns the index of the first invalid line.
    """
    sum_of_funcs = 0
    # If one of the lines of the code is invalid, the function returns the number of the invalid function
    # If code is valid, function returns the sum of the lines
    for i in range(len(lines_of_code_triplets)):
        if not triplets_structure_checker(lines_of_code_triplets[i]):
            return str(i)
        else:
            num1 = value_parser(lines_of_code_triplets[i][0][1:])
            func = operations_parser(lines_of_code_triplets[i][1][1:])
            num2 = value_parser(lines_of_code_triplets[i][2][1:])
            sum_of_funcs = sum_of_funcs + func(num1, num2)
    return sum_of_funcs
