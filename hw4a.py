def is_palindrom_no_helper(st):
    """
    Takes in a string, returns if the string is palindrom or not

    Args:
        st (str): A string that the function is going to determine whether it's a palindrom or not

    Returns:
        A boolean (True or False): If the string is a palindrom it will return True, if it's not a
        palindrom it will return False.
    """
    # A function that checks if the the word is a palindrom by comparing the first letter and
    # the last letter of the word, and then slices the ends of the string and keeps comparing recursively
    if len(st) == 0:
        return True
    if st[len(st) - 1] != st[0] and len(st) != 0:
        return False
    if st[len(st)-1] == st[0] and len(st) != 0:
        is_palindrom_no_helper(st[1:len(st) - 1])
        return True

def is_palindrom_with_wrapper(st, right_index, left_index):
    """
    Takes in a string and two indexes (as integers), returns if the string is a palindrom or not

    Args:
        st (str): A string. the function is going to determine whether it's a palindrom or not
        right_index (int): An integer. it is the index of the first character in the string
        left_index (int): An integer. it is the index of the last character in the string

    Returns:
        A boolean (True or False): If the string is a palindrom it will return True, if it's not a
        palindrom it will return False.
    """
    # Checks if the the word is a palindrom by comparing the first letter and last letter by indexes
    if st[right_index] == st[left_index] and right_index != left_index:
        right_index = right_index + 1
        left_index = left_index - 1
    if st[right_index] != st[left_index] and right_index != left_index:
        return False
    if right_index == left_index and st[right_index] == st[left_index]:
        return True
    return is_palindrom_with_wrapper(st, right_index, left_index)

def is_palindrom_with_helper(st):
    """
    A wrapper function that takes in a string, returns if the string is palindrom or not

    Args:
        st (str): A string that the function returns whether it's a palindrom or not

    Returns:
        A boolean (True or False): If the string is a palindrom it will return True, if it's not a
        palindrom it will return False.

    """

    # Determines whether a string is a palindrom or not by using the recursive function "is_palindrom_with_wrapper"
    if len(st) == 0:
        return True
    return is_palindrom_with_wrapper(st,0,len(st) - 1)

def remove_spaces(st, index):
    """
    Auxiliary function. Takes in a string and the last index of the string (as int),
    returns the string without spaces

    Args:
        st (str): A string. the function will "clean" it from spaces
        index (int): An integer. it is the last index of the string

    Returns:
        str: the string without spaces
    """
    # Auxiliary function - a recursive function that takes in a string
    # and the length of the string (as index), and returns the string without spaces
    if index < 0:
        return ""
    if st[index] != " ":
        return remove_spaces(st, index-1) + st[index]
    return remove_spaces(st, index - 1)

def is_palindrom_no_spaces(st):
    """
    A wrapper function that takes in a string, returns if the string is palindrom or not regardless of spaces

    Args:
        st (str): A string that the function is going to determine whether it's a palindrom or not

    Returns:
        A boolean (True or False): If the string is a palindrom it will return True, if it's not a
        palindrom it will return False.

    """
    # "Cleans" the function from spaces using auxiliary function, and using another function
    # that determines whether the string is a palindrom or not after cleaning spaces
    new_st = remove_spaces(st, len(st)-1)
    if len(new_st) == 0:
        return True
    return is_palindrom_with_wrapper(new_st, 0, len(new_st) - 1)

def weighted_average_with_wrapper(grades, numerator, denominator, counter):
    """
    Takes in a nested list of tuples that consists of grades and their weights,
    returns a list of two elements that can be used to calculate the average of the grades

    Args:
        grades (List(tuple(int, float)): A nested list of tuples, each tuple contains 2 elements: a grade
        and its weight in the final average grade calculation.
        numerator (int): An integer. Will be used to sum all the grades multiply by the weights, and
        therefore should be 0 in the input.
        denominator (int): An integer. Will be used to sum all the weights, and therefore should be 0 in the input.
        counter (int): An integer. Will be used as a stop condition for the recursion, should be 0 in the input.

    Returns:
        return_elements_list (list(float,float)): A list of two floats, the first element is the numerator and
        the second element is the denominator.
    """
    # Calculates the numerator and the denominator, and then puts it in a return list. the numerator
    # the counter is the stop condition of the recursion - if it's equal to the length of the list,
    # it means the function reached the end of the list. The function returns the list.
    if counter == len(grades):
        return_elements_list = [numerator, denominator]
        return return_elements_list
    else:
        numerator = numerator + (grades[counter][0] * grades[counter][1])
        denominator = denominator + grades[counter][1]
        counter = counter + 1
        return weighted_average_with_wrapper(grades, numerator, denominator, counter)

def weighted_average(grades):
    """
    A wrapper function. Takes in a list of tuples of grades and their weights in the calculation, returns the average grade
    as a float

    Args:
        grades (List(tuple(int, float)): A nested list of tuples, each tuple contains 2 elements: a grade
        and its weight in the final average grade calculation.
    Returns:
        avg_grade (float): The average grade of all the grades in the list.
    """
    list_of_elements = weighted_average_with_wrapper(grades, 0, 0, 0)

    # Calculates the average grade and rounds up to 2 decimal
    avg_grade = round((list_of_elements[0] / list_of_elements[1]), 2)
    return avg_grade

def is_prime_with_wrapper(num, divider):
    """
    Takes in a number and a divider (both integers), and returns of the number is prime or not.

    Args:
        num (int): An integer. The function determines whether this number is prime or not.
        divider (int): An integer. The function uses this variable to divide the number. Should be 2 in the input.

    Returns:
        A boolean (True or False):
        if the number is prime, the function will return True.
        if the number is not a prime number, the function will return False.

    """
    # Checks if the number is divisible. the value we should put in the divider is 2,
    # because it is the smallest prime number. the function calls itself and checks if the number can be divided
    # by any number from 2 to the number itself. if it can be divided, the function will return false.
    # if the divider reaches the number itself, it means that the number couldn't be divided and therefore it is prime.
    if num == divider:
        return True
    if num % divider == 0:
        return False
    else:
        return is_prime_with_wrapper(num, divider+1)

def is_prime(num):
    """
    A wrapper function. It takes in an integer, returns if the integer is a prime number or not

    Args:
        num (int): An integer. the function determines whether this number is prime or not.

    Returns:
        A boolean (True or False):
        if the number is prime, the function will return True.
        if the number is not a prime number, the function will return False.
    """
    return is_prime_with_wrapper(num, 2)

def is_perfect_with_wrapper(num, divider, counter):
    """
    Takes in 3 integers (a number, divider and counter), returns if the number is perfect or not.

    Args:
        num (int): An integer. the function determines whether or not this number is a perfect number
        divider (int): An integer. used as the dividers of the number. should be 1 in the input.
        counter (int): An integer. used to sum all the dividers of the number. should be 0 in the input.

    Returns:
        counter (int): An integer. the sum of all the dividers of the number.
    """
    if num == divider:
        return counter
    if num % divider == 0:
        counter = counter + divider
    return is_perfect_with_wrapper(num, divider+1, counter)

def is_perfect(num):
    """
    A wrapper function
    If a number is equal to the sum of its dividers, it is a perfect number
    The function takes in an integer, returns if the integer is a perfect number or not

    Parameters:
        num (int): An integer. the function determines whether or not this number is a perfect number

    Returns:
        A boolean (True or False):
        if the number is a perfect number, the function will return True.
        if the number is not a perfect number, the function will return False.
    """
    # Uses the recursive function above (is_perfect_with_wrapper). if the number is equal
    # to the sum of its dividers, the function will return true. otherwise it will return false
    if is_perfect_with_wrapper(num, 1, 0) == num:
        return True
    return False

def if_seven_is_digit(num):
    """
    Takes in an integer (num), returns if 7 is one of its digits

    Args:
        num (int): An integer. The function determines if it has 7 in it.

    Returns:
        A boolean (True or False): If 7 is one of the number's digits, the function will return True.
        otherwise, it will return False.
    """
    if num == 0:
        return
    if (num % 10) == 7:
        return True
    else:
        return if_seven_is_digit(num // 10)

def is_7_boom(num):
    """
    A wrapper function.
    A number will be defined as a "7 boom" number if it maintains at least one of the following:
    7 is one of its dividers, or one of its digits is 7.
    The function takes in an integer, returns if the integer is a "7 boom" number or not.

    Parameters:
        num (int): An integer. the function determines whether it is a "7 boom" number or not.

    Returns:
        A boolean (True or False): If the number is 7 boom, the function will return True.
        otherwise, it will return False.
    """

    # Checks if 7 is one of the number's dividers or if it has 7 as one of its digits
    if if_seven_is_digit(num) == True or num % 7 == 0:
        return True
    return False