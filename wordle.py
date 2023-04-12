from wordle_list import get_wordle_list
from colorama import Fore, Back, Style

def get_feedback_string(guess, secret_word):
    '''
    Returns a feedback string by comparing the 5-letter guess with the secret word
    - Correct letters in the correct spot are represented by capital letters,
    - Correct letters in the incorrect spot are represented by lowercase letters,
    - Incorrect letters are represented by dashes

    Args:
        guess(str): 5-letter guess
        secret_word(str): 5-letter secret word
    Returns:
        str: Feedback string for the given guess
    '''

    feedback_letters = ['-', '-', '-', '-', '-']
    guess = list(guess.upper())

    for i in range(len(guess)):
        #Correct letter, correct spot
        if guess[i]==secret_word[i]:
            feedback_letters[i]=guess[i]
    for j in range(len(guess)):
        #Correct letter, incorrect spot
        if guess[j] in secret_word and guess[j] != secret_word[j]:
            if "".join(feedback_letters).upper().count(guess[j])<"".join(secret_word).upper().count(guess[j]):
                #If letter shows up more than once in guess but once in secret word, both should not be highlighted
                feedback_letters[j] = guess[j].lower()
            else:
                #Incorrect letter
                feedback_letters[j] = '-'
    return "".join(feedback_letters)

def show_feedback(guess, secret_word):
    '''
    Prints feedback to shell using wordle color scheme
    - Green for correct letters in correct spot
    - Yellow for correct letters in incorrect spot
    - Gray for incorrect letters

    Args:
        guess(str): 5-letter guess
        secret_word(str): 5-letter secret word
    Returns: N/A
    '''

    feedback_string = get_feedback_string(guess, secret_word)
    guess = guess.upper()

    print(Back.WHITE+"       "+Back.RESET)
    feedback_colors = Back.RESET+Style.DIM+"`"+Style.RESET_ALL
    for i in range(len(guess)):
        if feedback_string[i] == '-':
            feedback_colors += (Back.BLACK+Fore.WHITE+guess[i])
        elif feedback_string[i] != '-' and feedback_string[i].islower():
            feedback_colors += (Back.YELLOW+Fore.WHITE+guess[i])
        else:
            feedback_colors += (Back.GREEN+Fore.WHITE+guess[i])
    feedback_colors += (Back.RESET+Style.DIM+'`'+Style.RESET_ALL)
    print(feedback_colors)
    print(Back.WHITE+"       "+Back.RESET+Fore.RESET)