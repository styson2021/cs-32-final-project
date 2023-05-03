from wordle_list import get_wordle_answer_list, get_wordle_allowed_words
from colorama import Fore, Back, Style
import random

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

    print(Back.RESET+"       "+Back.RESET)
    feedback_colors = Back.RESET+Style.DIM+Style.RESET_ALL
    for i in range(len(guess)):
        if feedback_string[i] == '-':
            feedback_colors += (Back.BLACK+Fore.WHITE+guess[i])
        elif feedback_string[i] != '-' and feedback_string[i].islower():
            feedback_colors += (Back.YELLOW+Fore.WHITE+guess[i])
        else:
            feedback_colors += (Back.GREEN+Fore.WHITE+guess[i])
    feedback_colors += (Back.RESET+Style.DIM+Style.RESET_ALL)
    print(feedback_colors)
    print(Back.RESET+"       "+Back.RESET+Fore.RESET)

def get_AI_hint(guesses, feedback_strings):
    '''
    Uses list of previous guesses and previous feedback to narrow down list of Wordle answers, then uses letter frequencies in English language to produce an AI-generated guess

    Args:
        guesses(list): A list of previous guesses (strings)
        feedback_strings(list): A list of previous feedback-strings corresponding to a particular guess
    Returns:
        str: An AI-generated, 5-letter guess
    '''

    ai_guess = ""

    word_list = get_wordle_answer_list()

    #Frequency of each letter in the English language (Wikipedia)
    letter_frequencies = {
        "A": 8.2,
        "B": 1.5,
        "C": 2.8,
        "D": 4.3,
        "E": 13,
        "F": 2.2,
        "G": 2,
        "H": 6.1,
        "I": 7,
        "J": 0.15,
        "K": 0.77,
        "L": 4,
        "M": 2.4,
        "N": 6.7,
        "O": 7.5,
        "P": 1.9,
        "Q": 0.095,
        "R": 6,
        "S": 6.3,
        "T": 9.1,
        "U": 2.8,
        "V": 0.98,
        "W": 2.4,
        "X": 0.15,
        "Y": 2,
        "Z": 0.074
    }

    if len(guesses)==0:
        #We will always use the popular first guess, CRATE
        ai_guess = "CRATE"
    else:
        for i, guess in enumerate(guesses):
            guess.upper()
            #Remove previous guesses from all remaining possible guesses 
            if guess in word_list:
                word_list.remove(guess)
            for j, letter in enumerate(feedback_strings[i]):
                if letter == "-" and guess[j] not in feedback_strings[i].upper():
                    #Remove all words that have an incorrect letter from remaining possible guesses
                    word_list = [word for word in word_list if guess[j] not in word]
                    
                elif letter.isupper():
                    #Remove all words that do not have correct letters in the same, exact spot as where it was guessed
                    word_list = [word for word in word_list if word[j] == letter]
                elif letter.islower():
                    #Remove all words that (1) have correct letters incorrect spots in the spot it was guessed or (2) are missing correct letters in incorrect spots altogether
                    word_list = [word for word in word_list if ((letter.upper() in word) and (word[j]!=letter.upper()))]

        max_frequency = 0
        max_frequency_word = ""
        for word in word_list:
            sum_frequencies = 0
            for letter in word:
                sum_frequencies += letter_frequencies[letter]
            if sum_frequencies>max_frequency:
                max_frequency = sum_frequencies
                max_frequency_word = word
        #Guess is word left in remaining possible guesses with highest sum of letter frequencies
        ai_guess = max_frequency_word
        
    return ai_guess

def get_user_guess(feedback_strs, guess_strs):
    '''
    Asks for a user's 5-letter guess and only allows them to input a five-letter word included in the allowable list of words

    Args: 
        feedback_strs(list): Previous feedback strings for AI guess
        guess_strs(list): Previous guesses (strs) for AI guess
    Returns:
        str: User's 5-letter, allowable guess
    '''

    guess = input("Enter your guess (Type 'HINT' to use an AI-generated guess):\n")

    while guess.upper() not in get_wordle_allowed_words() and guess.upper() != "HINT":
        print("Your guess must be a five-letter, English word, or you must ask for a hint by typing 'HINT.'\n")
        guess = input("Enter your guess (Type 'HINT' to use an AI-generated guess):\n")

    if guess.upper() == "HINT":
        guess = get_AI_hint(guess_strs, feedback_strs)
    
    return guess

def test_AI_guesser():
    '''
    Tests the get_AI_hint function across all possible Wordle answers and outputs the average number of guesses it takes to get the word correct, the percentage of words it gets correct within 6 guesses, and the percentage it fails to guess within 6 guesses

    Args: N/A
    Returns: Prints metrics on get_AI_hint function described above
    '''
    
    total_guesses = 0
    total_correct = 0
    total_missed = 0
    for word in get_wordle_answer_list():
        num_guesses = 0
        guesses = []
        feedback_strings = []
        while True:
            guess = get_AI_hint(guesses, feedback_strings)
            num_guesses += 1
            guesses.append(guess)
            feedback_strings.append(get_feedback_string(guess, word))

            if guess == word:
                if num_guesses <= 6:
                    total_correct += 1
                else:
                    total_missed += 1
                total_guesses += num_guesses
                break
    avg_guesses = round(total_guesses / len(get_wordle_answer_list()), 3)
    percent_correct = 100*round(total_correct / len(get_wordle_answer_list()), 2)
    percent_missed = 100*round(total_missed / len(get_wordle_answer_list()), 2)

    print("The average number of guesses is", avg_guesses)
    print(f"The percentage of words the algorithm guessed within 6 guesses is {percent_correct}%.")
    print(f"The percentage of words the algorithm failed to guess within 6 guesses is {percent_missed}%.")

if __name__ == "__main__":
    secret_word = random.choice(get_wordle_answer_list())
    print("\nWelcome to Wordle!\n")
    feedback_strings = []
    guesses = []
    
    guess = get_user_guess(feedback_strings, guesses)
    num_guesses = 1
    show_feedback(guess, secret_word)
    guesses.append(guess)
    feedback_strings.append(get_feedback_string(guess, secret_word))
    
    while num_guesses < 6 and ('-' in get_feedback_string(guess, secret_word) or not get_feedback_string(guess, secret_word).isupper()):
        guess = get_user_guess(feedback_strings, guesses)
        show_feedback(guess, secret_word)
        num_guesses += 1
        guesses.append(guess)
        feedback_strings.append(get_feedback_string(guess, secret_word))
        
    if guess.upper() == secret_word:
        print("You won in", num_guesses, "guesses!")
    else:
        print(f"You did not guess the word. The word was {secret_word}.")