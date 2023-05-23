# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
### WRITE CODE HERE

def encrypt (text, key):
    """
    Takes in a string and a key number, returns an encrypted string based on Caeser cipher

    Parameters:
        text (str): A sentence we need to encrypt
        key (int): An integer that contains the key for the encryption
    Returns:
      encrypted_string (str): A string of the encrypted sentence
    """

    #Creating 2 strings that contain all the letters in the alphabet, lowercase and uppercase
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #Creating a string that is going to contain the encrypted string
    encrypted_string = ""

    #First loop iterates the input string, second loop iterates the letters of the alphabet
    #First we check if the letter is lowercase or uppercase
    #Then we add the desired letter to the new encrypted string
    #If the character is not a letter we should add it to the string as it is
    for i in range(0, len(text)):
        for k in range(0,26):
            if text[i] == alphabet_lower[k]:
                encrypted_string = encrypted_string + alphabet_lower[(k+key)%26]
            elif text[i] == alphabet_upper[k]:
                encrypted_string = encrypted_string + alphabet_upper[(k + key)%26]
        if text[i] not in alphabet_lower and text[i] not in alphabet_upper:
                encrypted_string = encrypted_string + text[i]

    #Returning the encrypted string
    return(encrypted_string)

# ************************ QUESTION 2 **************************
### WRITE CODE HERE

def decrypt(text, key):
    """
    Takes in a string and a key number, returns an decrypted string based on Caeser cipher

    Parameters:
        text (str): A sentence we need to decrypt
        key (int): An integer that contains the key for the decryption
    Returns:
      decrypted_string (str): A string of the decrypted sentence
    """

    #This requires the same process in the first question (with the encryption)
    #except this time we are going to substract the key instead of adding it because in
    #order to decrypt we need to go backwards
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_string = ""

    for i in range(0, len(text)):
        for k in range(0, 26):
            if text[i] == alphabet_lower[k]:
                decrypted_string = decrypted_string + alphabet_lower[(k - key) % 26]
            elif text[i] == alphabet_upper[k]:
                decrypted_string = decrypted_string + alphabet_upper[(k - key) % 26]
        if text[i] not in alphabet_lower and text[i] not in alphabet_upper:
            decrypted_string = decrypted_string + text[i]

    #Returning the decrypted string
    return decrypted_string

# ************************ QUESTION 3 **************************
### WRITE CODE HERE

def naive_break(text):
    """
    Takes in a string, returns a list of all the possible decrypted strings based on Caeser cipher

    Parameters:
        text (str): A sentence we need to decrypt
    Returns:
      list_of_strings (str): A list of all the possible decryptions of the sentence
    """

    #I created a list with 26 elements. The loop iterates the list and puts in every element a decrypted
    #string, using the function I wrote in the previous question
    list_of_strings = ["empty"] * 26
    for i in range (0,26):
        list_of_strings[i] = decrypt(text, i)

    #Returning the list of decrypted strings
    return list_of_strings

# ************************ QUESTION 4.1 **************************
### WRITE CODE HERE

def find_common_letter(text):
    """
    Takes in a string, returns the letter that appears the most in the string

    Parameters:
        text (str): The string in which we need to find the most common letter
    Returns:
      most_common_letter (char): A character that contains the most common letter
    """

    #Creating 2 strings that contain all the letters in the alphabet, lowercase and uppercase
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #A string that is going to contain the most common letter
    most_common_letter = ""

    #A list that is going to contain the counting for the number of times each letter appears
    counting_list = [0] * 26

    #A loop that iterates the list and counts the number of times each letter appears in the text
    for i in range (0, 26):
        counting_list[i] = text.count(alphabet_lower[i]) + text.count(alphabet_upper[i])

    #Finding the position of the most common letter and returning that letter
    max_position = counting_list.index(max(counting_list))
    most_common_letter = alphabet_lower[max_position]
    return most_common_letter

# ************************ QUESTION 4.2 **************************
### WRITE CODE HERE

def frequency_break(text, common_letter):
    """
    Takes in a string and a character and returns a decrypted string based on Caeser cipher

    Parameters:
        text (str): The string we need to decrypt
        common_letter (char): A character of the most common letter in the original decrypted string
    Returns:
      decrypted_str (str): The right decrypted string
    """

    #Creating a list with all the possibilities for the right decrypted string using the function
    #I wrote in question 3
    list_of_options = naive_break(text)

    #An empty string that is going to contain the right decrypted string
    decrypted_str = ""

    #A loop that iterates the list and finds the right string by matching it to its common letter
    #using the function I wrote in the previous question
    for i in range (0,26):
        if find_common_letter(list_of_options[i]) == common_letter:
            decrypted_str = list_of_options[i]

    #Returning the right decrypted string
    return decrypted_str
