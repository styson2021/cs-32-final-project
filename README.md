# CS 32 Final Project: AI Wordle Game

## FP Choice (due 3/27)
Our final project for CS 32 will be a Wordle game that can be played by users and provides feedback (using green, yellow, and gray letters, like the New York Times) for each guess players provide. We plan to have the game played in the Python shell, and we expect we will use various Python libraries to help format the shell output as similarly as possible to the actual Wordle game. Additionally, we plan to build an AI guesser that provides a one of the best possible guess, based on the user's previous guesses and feedback received from those guesses. Users will be able to ask for a hint, in which case the AI guesser will provide its guess to them. We are all avid Wordle players, so we are excited to get started on this project!

## FP Design (due 4/10)
We have enjoyed getting going on our AI Wordle Game, and we are planning to double-down on this original final project idea. We have made a fair amount of progress thus far. In particular, we have written two functions that will be key to developing our project. These are:
* `get_feedback_string(guess, secret_word)`, which takes a player's 5-letter guess and the 5-letter chosen secret word and outputs a string that provides feedback on the accuracy of the guess. In this string, correct letters in the correct spot are given a capital letter, correct letters in the incorrect spot are given a lowercase letter, and incorrect letters are given a dash.
* `show_feedback(guess, secret_word)`, which takes a player's 5-letter guess and the 5-letter chosen secret word and calls `get_feedback_string`. It then uses the python *colorama* library to print the feedback to the shell using the same color scheme as the New York Times Wordle game. Specifically, correct letters in the correct spot are printed with a green background, correct letters in the incorrect spot are printed with a yellow background, and incorrect letters are printed with a black background.

Below are some sample inputs and outputs from these two functions:

