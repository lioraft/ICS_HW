# *************** HOMEWORK 3 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE
def verify_nonogram_board(board, rows_constraints, columns_constraints):
    """
    Takes in a Nonogram matrix and two limitation lists, returns if the matrix is the correct solution or not

    Parameters:
    board (List[List[bool]]): A nested list in the size of m*n that contains bool values (True or False).
                              It is the matrix of the Nonogram.
    rows_constraints (List[int]): A list of integers. each integer represents the number of True variables
                                  that are supposed to be in the current row in the matrix, respectively.
    rows_constraints (List[int]): A list of integers. each integer represents the number of True variables
                                  that are supposed to be in the current column in the matrix, respectively.
    Returns:
      valid_solution (bool): A boolean that represent if the solution is correct or not. if it's correct
                             the boolean will be True, if it's incorrect the boolean will be False.
    """

    #Auxiliary function - this function recieves a matrix (Nested list) and the index of a column (integer)
    #and returns the column as a list
    def column_to_list(matrix, column):
        column_list = []
        for i in range(0, len(matrix)):
            column_list.append(matrix[i][column])
        return column_list

    #The bool that the function needs to return. it is false until proven otherwise
    valid_solution = False

    #Lists that are going to contain the length of the True sequences in each row and column, respectively
    continuous_rows = [0] * len(rows_constraints)
    continuous_columns = [0] * len(columns_constraints)

    #A loop that iterates the rows of the matrix, counts the length of the True sequence in each row
    #and puts it in the list of the row sequences
    for i in range(0, len(rows_constraints)):
        if True in board[i]:
            row_position = board[i].index(True)
        else:
            break
        for j in range(row_position, len(columns_constraints)):
          if board[i][j] == True:
              continuous_rows[i] = continuous_rows[i] + 1
          else:
              break

    # A loop that iterates the columns of the matrix, using the auxiliary function.
    #then it counts the length of the True sequence in each column
    #and puts it in the list of the column sequences
    for k in range(0, len(columns_constraints)):
        current_column = column_to_list(board, k)
        if True in current_column:
            column_position = current_column.index(True)
        else:
            break
        for l in range(column_position, len(current_column)):
            if current_column[l] == True:
                continuous_columns[k] = continuous_columns[k] + 1
            else:
                break

    #If the lists I created are identical to the lists given in the function, it means that the solution is correct
    if rows_constraints == continuous_rows and columns_constraints == continuous_columns:
        valid_solution = True

    return valid_solution

# ************************ QUESTION 2a **************************
### WRITE CODE HERE
def get_all_capital_letters(text):
    """
    Takes in a string, returns a list that contains all the uppercase letters in the string

    Parameters:
        text (str): A string that has a text in it

    Returns:
       list_of_upper_letters (List): A list that contains, in chronological order of appearance,
        all the uppercase letters that are in the string
    """
    #The list that the function is going to return
    list_of_upper_letters = []

    #A loop that iterates the string, finds the uppercase letters and adds them to the list
    for i in range(0, len(text)):
        if text[i].isupper() == True:
            list_of_upper_letters.append(text[i])
    return list_of_upper_letters

# ************************ QUESTION 2b **************************
### WRITE CODE HERE
def split_text_to_tokens(text):
    """
    Takes in a string of "unclean" sentence, returns a list of all the words after "cleaning"

    Parameters:
      text (str): A string of a sentence that contains different characters

    Returns:
        copy_list (List): A list that consists of different strings, each string is a word after
        "cleaning" - meaning it contains only alphabetical letters
    """
    #A list consists of the sentence after spliting the words
    list_of_words = text.split(" ")

    #Creating empty list in the length of the original list
    copy_list = [""] * len(list_of_words)

    #A loop that iterates the list and "cleans" each word:
    #It adds to the copy list only alphabetical letters
    for j in range(0,len(list_of_words)):
        for k in range(0,len(list_of_words[j])):
            if list_of_words[j][k].isalpha() == True:
                copy_list[j] = copy_list[j] + list_of_words[j][k]

    #Counting how many empty elements there are in the list, because the string
    #was seperated in spaces and there can be mulitple spaces between words
    empty_count = copy_list.count("")

    # Iterating the list and removing empty elements
    for i in range(0,empty_count):
        copy_list.remove("")

    return copy_list

# ************************ QUESTION 2c **************************
### WRITE CODE HERE
def grade_text_tone(text):
    """
    Takes in a string, returns the grade of the string in its cleaned form

    Parameters:
      text (str): A string of a sentence that contains different characters.

    Returns:
        avg_grade (float): The average grade of the string
    """

    #Auxiliary function: Calculates the avarage grade of a single letter - if the letter is uppercase it
    #adds it to counting variable. in the end it returns the grade that is calculated with dividing the number
    #of uppercase letters by the total number of letters that are in the word
    def single_word_grade(word):
        upper_count = 0
        for i in range(0,len(word)):
            if word[i].isupper() == True:
                upper_count = upper_count + 1
        grade = upper_count / len(word)
        return grade

    #Spliting the text to a list of cleaned words with the function from the previous question
    total_sum = 0
    clean_text_list = split_text_to_tokens(text)

    #Iterating the list and using the auxiliary function to sum the grades of all the words in the text
    for j in range(0, len(clean_text_list)):
        total_sum = total_sum + single_word_grade(clean_text_list[j])
    avg_grade = total_sum / len(clean_text_list)
    return '%.4f' % avg_grade

# ************************ QUESTION 3a **************************
### WRITE CODE HERE
def register_students_submissions(students_raw_submissions):
    """
    Takes in a list of strings, returns a dictionary

    Parameters:
      students_raw_submissions (List(str)): A list of strings that contain students' names and essays

    Returns:
        dict_of_submissions (dict(str, str)): A dictionary that matches between two strings - the keys
         that are the students' names and the values that contain their essays
    """

    #Auxiliary function: Takes in a full name, splits it to first and last name, capitalizes
    #the names and returns the string of the full name in its proper form
    def capitalizing_names(text):
        list_of_names = text.split(" ")
        name = ""
        list_of_names[0] = list_of_names[0].casefold()
        list_of_names[1] = list_of_names[1].casefold()
        list_of_names[0] = list_of_names[0].capitalize()
        list_of_names[1] = list_of_names[1].capitalize()
        name = list_of_names[0] + " " + list_of_names[1]
        return name

    dict_of_submissions = {}

    #A loop that iterates the list, separates and caplitalizes (using the auxiliary function)
    #the names from the essays and matches them together in the dictionary
    for i in range(0,len(students_raw_submissions)):
        new_sub_list = students_raw_submissions[i].split("|")
        dict_of_submissions[capitalizing_names(new_sub_list[0])] = new_sub_list[1]
    return dict_of_submissions

# ************************ QUESTION 3b **************************
### WRITE CODE HERE
def grade_students_submissions(students_submissions):
    """
    Takes in a dictionary that contains students' names and essays, and returns a dictionary that
    contains students' names and the grades of their essays.

    Parameters:
        students_submissions (dict(str, str)): A dictionary that contains str keys and str values. the keys are
        students' full names, and the values are their essays, respectively.

    Returns:
        dict_of_grades (dict(str,str)): A dictionary that contains str keys and str values. the keys are
        students' names as given in the input dictionary, and the values are grades that are calculated based
        on the ratio between uppercase letters and total letters in the essay.
    """

    #Creating a dictionary that will contain the grades, and two lists: a list of the keys and
    #a list of the values. the lists are going to be used to iterate the dictionary and calculate
    #the grades
    dict_of_grades = students_submissions.copy()
    list_of_keys = list(students_submissions)
    list_of_values = list(students_submissions.values())

    #Auxiliary function: this function takes in a string and returns the number of words it contains
    def count_words(text):

        #Spliting the words of the string
        list_of_words = text.split(" ")

        # Counting how many empty elements there are in the list, because the string
        # was seperated in spaces and there can be mulitple spaces between words
        empty_count = list_of_words.count("")

        #Iterating the list and removing empty elements
        for i in range(0, empty_count):
            list_of_words.remove("")

        return len(list_of_words)

    #A loop that iterates the dictionary. if the essay is in a proper length, the grade will
    #be calculated (using the function from question 2c) and will be put in the value matching
    #the name of the student who wrote the essay. if the essay is too short or too long, the grade
    #will be F.
    for i in range(0, len(list_of_keys)):
        if count_words(list_of_values[i]) >= 2 and count_words(list_of_values[i]) <=10:
            dict_of_grades[list_of_keys[i]] = grade_text_tone(list_of_values[i])
        else:
            dict_of_grades[list_of_keys[i]] = "F"

    return dict_of_grades

# ************************ QUESTION 3c **************************
### WRITE CODE HERE
def calculate_tokens_frequencies(students_submissions):
    """
    Takes in a dictionary that contains students' names and essays, and returns a dictionary that
    contains the frequency of each word that appears in the essays.

    Parameters:
     students_submissions (dict(str,str)): A dictionary that contains str keys and str values. the keys are
        students' full names, and the values are their essays, respectively.
    Returns:
        dict_of_freq (dict(str, int)): A dictionary that contains str keys and int values. the keys are the
        words that appear in the essays, and the values are the total number of times each word appears
        in the essays, respectively.
    """

    #Creating a list of all the essays, and an empty dict that is going contain and words and their frequencies
    list_of_essays = list(students_submissions.values())
    dict_of_freq = {}

    #A loop that iterates the list of the essays. if the word is already a key in the dict,
    #the count of its frequency will increase by 1. if not, a new key will be made for the word
    for i in range(0, len(list_of_essays)):
        current_essay = split_text_to_tokens(list_of_essays[i])
        for k in range(0, len(current_essay)):
            if current_essay[k].casefold() in dict_of_freq.keys():
                num = dict_of_freq.get(current_essay[k].casefold())
                dict_of_freq.update({current_essay[k].casefold() : num + 1})
            else:
                dict_of_freq.update({current_essay[k].casefold(): 1})

    return dict_of_freq

