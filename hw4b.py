def subset_sum_memo_with_wrapper(arr, num, num_of_left, mem):
    """
    Takes in a list of numbers, a target number, the number of numbers that we didn't add up
    from the list yet, and a dictionary. returns if we can reach the target number by summing numbers from the list.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need to sum up to
    the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.
    num_of_left (int): An integer. This number is the number of elements we didn't add from the list yet. Will be used
    for memoization.
    mem (dict(tuple(int,int),boolean): A dictionary. Will contain a key which will be a tuple that contains num_of_left and num. the values
    of the dictionary will be either True or False. that way we can avoid calculating False combinations that we already
    calculated.

    Returns:
        A boolean: If we can find a combination of numbers that reach the target number, the function returns True. otherwise,
        it returns False.
    """
    key = (num_of_left, num)
    if key not in mem:
        if num == 0:
            mem[key] = True
        elif len(arr) == 0 or num < 0:
            mem[key] = False
        elif num > 0:
            return subset_sum_memo_with_wrapper(arr[1:], num - arr[0], num_of_left, mem) or subset_sum_memo_with_wrapper(arr[1:], num, num_of_left, mem)
    return mem[key]

def subset_sum_memo(arr, num):
    """
    A wrapper function. Takes in a list of numbers and a target number, returns if we can reach the target number by
    summing numbers from the list.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need to sum up to
    the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.

    Returns:
        A boolean: If we can find a combination of numbers that reach the target number, the function returns True. otherwise,
        it returns False.
    """
    mem = {}
    num_of_left = len(arr)
    return subset_sum_memo_with_wrapper(arr, num, num_of_left, mem)

def subset_sum_count(arr, num):
    """
    Takes in a list of numbers and a target number, returns the number of elements sum combinations that add
    up to the target number.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need to sum up to
    the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.

    Returns:
        An integer: the number of elements sum combinations that add up to the target number.
    """
    # A recursive function - it can either add a number or not add it.
    # If it adds the number we should substract it from the target number.
    # If the number reaches 0, it means we found a combination. if the number is smaller than
    # the target or we reached the end of the list, we couldn't find a combination.
    if num == 0:
        return 1
    if len(arr) == 0 or num < 0:
        return 0
    if len(arr) > 0:
        return subset_sum_count(arr[1:], num - arr[0]) + subset_sum_count(arr[1:], num)

def subset_sums_with_wrapper(arr, num, list_of_lists, current_lst, current_index):
    """
    Takes in a list of numbers, a target number, two empty lists, and current index. returns
    a nested list that contains lists of elements sum combinations that add up to the target number.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need to sum up to
    the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.
    list_of_lists (List): An empty list. This list will contain all of the combinations that add up to the
    target number.
    current_lst (List): An empty list. This list will store the list combination until put in the nested list.
    current_index (int): An integer. the current index of the list that we are examining.

    Returns:
        list_of_lists (List(List(int)): A nested list of lists that contain integers. Each list is a combination
        of numbers that add up to the target number.
    """
    # If target number is 0 it means we found a combination, so we add the list of addends to the list of lists
    if num == 0:
        list_of_lists.append(current_lst)
    if num < 0:
        return []
    if current_index == len(arr):
        return []
    # Creating a copy of the current list. we add the next element only to the copy list. in the option that
    # takes the next element in, the input will be the copy of the current list. in the option that doesn't take the
    # next element, the input will be the current list itself
    current_lst_with_next = current_lst.copy()
    current_lst_with_next.append((arr[current_index]))
    if num > 0 and current_index != len(arr):
        # If we take the element in the current index, we continue to the next element
        subset_sums_with_wrapper(arr, num - arr[current_index], list_of_lists, current_lst_with_next, current_index+1)
        # If we don't take the element in the current index, we continue to the next element without adding it
        subset_sums_with_wrapper(arr, num, list_of_lists, current_lst, current_index+1)
    return list_of_lists

def subset_sums(arr, num):
    """
    A wrapper function. Takes in a list of numbers and a target number, returns
    a nested list that contains lists of elements sum combinations that add up to the target number.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need
    to sum up to the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.

    Returns:
        A List (List(List(int)): A nested list of lists that contain integers. Each list is a combination
        of numbers that add up to the target number.
    """
    return subset_sums_with_wrapper(arr, num, [], [], 0)

def subset_sum_with_repeats_with_wrapper(lst, num, list_of_lists, current_lst, current_index, back_index):
    """
        Takes in a list of numbers, a target number, two empty lists, current index and a back index. returns
    a nested list that contains lists of elements sum combinations that add up to the target number with repetition of numbers.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need to sum up to
    the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.
    list_of_lists (List): An empty list. This list will contain all of the combinations that add up to the
    target number.
    current_lst (List): An empty list. This list will store the list combination until put in the nested list.
    current_index (int): An integer. the current index of the list that we are examining.
    back_index (int): An integer. an index we are going to use to return back to the beginning of the list.

    Returns:
        list_of_lists (List(List(int)): A nested list of lists that contain integers. Each list is a combination
        of numbers that add up to the target number.
    """
    # If target number is 0 it means we found a combination, so we add the list of addends to the list of
    # lists (if it's not already there)
    if num == 0:
        for i in range(0, len(list_of_lists)):
            if list_of_lists[i] == current_lst:
                return
        list_of_lists.append(current_lst)
    if num < 0:
        return
    if current_index == len(lst):
        return
    # Creating a copy of the current list. we add the next element only to the copy list. in the option that
    # takes the next element in, the input will be the copy of the current list. in the option that doesn't take the
    # next element, the input will be the current list itself
    current_lst_with_next = [] + current_lst
    current_lst_with_next.append((lst[current_index]))
    # If we take the element in the current index, we have two more options to do:
    # Continue to the next element
    subset_sum_with_repeats_with_wrapper(lst, num - lst[current_index], list_of_lists, current_lst_with_next, current_index+1, back_index)
    # Take the same element again
    subset_sum_with_repeats_with_wrapper(lst, num - lst[current_index], list_of_lists, current_lst_with_next, current_index, back_index)
    # If we don't take the element in the current index, we continue to the next element
    subset_sum_with_repeats_with_wrapper(lst, num, list_of_lists, current_lst, current_index+1, back_index)
    # We can also go back to the beginning of the list
    back_index = back_index + 1
    subset_sum_with_repeats_with_wrapper(lst, num, list_of_lists, current_lst, -1 + back_index, back_index)
    return list_of_lists

def subset_sum_with_repeats(lst, num):
    """
    A wrapper function. Takes in a list of numbers and a target number, returns
    a nested list that contains lists of elements sum combinations, including repetition of elements,
    that add up to the target number.

    Args:
    arr (List(int)): A list of integers. The elements of the list are used to create combinations that need
    to sum up to the target number.
    num (int): An integer. The target number we need to reach by adding up numbers from the list.

    Returns:
        A List (List(List(int)): A nested list of lists that contain integers. Each list is a combination
        of numbers that add up to the target number.
    """
    return subset_sum_with_repeats_with_wrapper(lst, num, [], [], 0, 0)

def abc_words_with_wrapper(num, list_of_words, current_word):
    """
    Takes in a number, an empty list and an empty string, returns a list with all the strings you can create from
    the letters "a", "b", "c", each string is in the length of num.

    Args:
        num(int): An integer. the length of each string.
        list_of_words(List): An empty list. this list is going to contain all the possible strings.
        current_word(str): An empty string. this string is going to contain possible string.

    Returns:
        list_of_words (List(str)): A list of strings. each string is in the length of num is made of at least one of
         the letters "a", "b", "c".
    """
    if num == 0:
        list_of_words.append(current_word)
    if num < 0:
        return
    abc_words_with_wrapper(num - 1, list_of_words, current_word + "a")
    abc_words_with_wrapper(num - 1, list_of_words, current_word + "b")
    abc_words_with_wrapper(num - 1, list_of_words, current_word + "c")
    return list_of_words

def abc_words(num):
    """
    Takes in a number, returns a list with all the strings you can create from the letters "a", "b", "c", each string is in the length
    of num.

    Args:
        num(int): An integer. the length of each string.

    Returns:
        A list (List(str)): A list of strings. each string is in the length of num is made of at least one of the letters "a", "b", "c".
    """
    return abc_words_with_wrapper(num, [], "")

def char_to_char_words_with_wrapper(start, end, num, list_of_words, current_word, start_index):
    """
    A wrapper function. Takes in start letter, end letter, a length of string, empty list, empty string
    and the ascii number of the start letter. returns a list with all the possible strings that can be made
    from the letters from start letter to end letter, in the proper length.

    Args:
    start (str): A string. consists of single letter that is the minimum alphabetical placed letter we can use.
    end (str): A string. consists of single letter that is the maximum alphabetical placed letter we can use.
    num (int): An integer. it is the length of each string that is going to be in the list.
    list_of_words (List): An empty list. will contain all the strings of the possible combinations.
    current_words (str): An empty string. will be used to contain the strings.
    start_index (int): An integer. will be set as the ascii number of the start letter.

    Returns:
        A list (List(str)): A list of strings. each string is made of at least on of the letters from
        start letter to end letter, and it is in the length of num.
    """
    # If num is 0, it means we reached the desired length of the string and therefore need to append it to the list
    if num == 0:
        for i in range(0, len(list_of_words)):
            if list_of_words[i] == current_word:
                return
        list_of_words.append(current_word)
    if num < 0:
        return
    if ord(start) <= ord(end):
        # Go back to the first letter
        char_to_char_words_with_wrapper(chr(start_index), end, num - 1, list_of_words, current_word + start, start_index)
        # Take the same current letter again
        char_to_char_words_with_wrapper(start, end, num - 1, list_of_words, current_word + start, start_index)
        # Take current letter and continue to the next letter
        char_to_char_words_with_wrapper(chr(ord(start) + 1), end, num - 1, list_of_words, current_word + start, start_index)
        # Don't take current letter and continue to the next letter
        char_to_char_words_with_wrapper(chr(ord(start) + 1), end, num, list_of_words, current_word, start_index)
    return list_of_words

def char_to_char_words(start, end, num):
    """
    Takes in start letter, end letter and a length of string, returns a list with all the possible strings that can be made
    from the letters from start letter to end letter, in the proper length.

    Args:
    start (str): A string. consists of single letter that is the minimum alphabetical placed letter we can use.
    end (str): A string. consists of single letter that is the maximum alphabetical placed letter we can use.
    num (int): An integer. it is the length of each string that is going to be in the list.

    Returns:
        A list (List(str)): A list of strings. each string is made of at least on of the letters from
        start letter to end letter, and it is in the length of num.
    """
    return char_to_char_words_with_wrapper(start, end, num, [], "", ord(start))

def solve_maze_monotonic_with_wrapper(mat, rows_index, columns_index, path_lst):
    """
    Takes in a maze which is nested list of lists of integers, indexes of rows and columns, and an empty list.
    Returns a list with the indexes for the solution to the maze, if there is any.

    Args:
    mat (List(List(int))): A nested list of lists of integers. It is a maze.
    rows_index (int): An integer. it is the index of the rows.
    columns_index (int): An integer. it is the index of the columns.
    path_lst (List): An empty list. will contain the indexes of the solution to the maze.

    Returns:
        path_lst List(List(int))): A nested list of lists of integers. We can continue in the maze only if the value in the next cell
        is bigger than the current value. if there's a solution for the maze, the function will return a list with the indexes of the
        solution. if not, the function will return None.
    """
    # If the indexes are the last indexes of the nested list, it means we reached our goal cell and found a solution
    if rows_index == len(mat)-1 and columns_index == len(mat[0]) - 1:
        return path_lst
    # Move right
    if columns_index < len(mat[0]) - 1:
        if mat[rows_index][columns_index] < mat[rows_index][columns_index+1]:
            path_lst.append([rows_index, columns_index+1])
            checking_lst = solve_maze_monotonic_with_wrapper(mat, rows_index, columns_index+1, path_lst)
            if checking_lst is None:
                path_lst.pop(len(path_lst)-1)
            else:
                return path_lst
    # Move down
    if rows_index < len(mat) - 1:
        if mat[rows_index][columns_index] < mat[rows_index+1][columns_index]:
            path_lst.append([rows_index+1, columns_index])
            checking_lst = solve_maze_monotonic_with_wrapper(mat, rows_index+1, columns_index, path_lst)
            if checking_lst is None:
                path_lst.pop(len(path_lst)-1)
            else:
                return path_lst
    # Move left
    if columns_index > 0:
        if mat[rows_index][columns_index] < mat[rows_index][columns_index-1]:
            path_lst.append([rows_index, columns_index-1])
            checking_lst = solve_maze_monotonic_with_wrapper(mat, rows_index, columns_index-1, path_lst)
            if checking_lst is None:
                path_lst.pop(len(path_lst)-1)
            else:
                return path_lst
    # Move up
    if rows_index > 0:
        if mat[rows_index][columns_index] < mat[rows_index-1][columns_index]:
            path_lst.append([rows_index-1, columns_index])
            checking_lst = solve_maze_monotonic_with_wrapper(mat, rows_index-1, columns_index, path_lst)
            if checking_lst is None:
                path_lst.pop(len(path_lst)-1)
            else:
                return path_lst

def solve_maze_monotonic(mat):
    """
    A wrapper function. Takes in a maze which is nested list of lists of integers,
    Returns a list with the indexes for the solution to the maze, if there is any.

    Args:
    mat (List(List(int))): A nested list of lists of integers. It is a maze.

    Returns:
        path_lst List(List(int))): A nested list of lists of integers. We can continue in the maze only if the value in the next cell
        is bigger than the current value. if there's a solution for the maze, the function will return a list with the indexes of the
        solution. if not, the function will return an empty list.
    """
    solution = solve_maze_monotonic_with_wrapper(mat, 0, 0, [[0,0]])
    if solution is None:
        return []
    else:
        return solution
