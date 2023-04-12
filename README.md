# CS 32 Final Project: AI Wordle Game

## FP Choice (due 3/27)
Our final project for CS 32 will be a Wordle game that can be played by users and provides feedback (using green, yellow, and gray letters, like the New York Times) for each guess players provide. We plan to have the game played in the Python shell, and we expect we will use various Python libraries to help format the shell output as similarly as possible to the actual Wordle game. Additionally, we plan to build an AI guesser that provides a one of the best possible guess, based on the user's previous guesses and feedback received from those guesses. Users will be able to ask for a hint, in which case the AI guesser will provide its guess to them. We are all avid Wordle players, so we are excited to get started on this project!

## FP Design (due 4/10)
We have enjoyed getting going on our AI Wordle Game, and we are planning to double-down on this original final project idea. We have made a fair amount of progress thus far. In particular, we have written two functions that will be key to developing our project. These are:
* `get_feedback_string(guess, secret_word)`, which takes a player's 5-letter guess and the 5-letter chosen secret word and outputs a string that provides feedback on the accuracy of the guess. In this string, correct letters in the correct spot are given a capital letter, correct letters in the incorrect spot are given a lowercase letter, and incorrect letters are given a dash.
* `show_feedback(guess, secret_word)`, which takes a player's 5-letter guess and the 5-letter chosen secret word and calls `get_feedback_string`. It then uses the python *colorama* library to print the feedback to the shell using the same color scheme as the New York Times Wordle game. Specifically, correct letters in the correct spot are printed with a green background, correct letters in the incorrect spot are printed with a yellow background, and incorrect letters are printed with a black background.

Below are some sample inputs and outputs from these two functions:
* `get_feedback_string("MOMMY", "MADAM")` --> "M-m--"
* `get_feedback_string("LEVER", "LOWER")` --> "L--ER"

* `show_feedback("MOMMY", "MADAM")` --> MOMMY (background colors: green, black, yellow, black, black)
* `show_feedback("LEVER", "LOWER")` --> LEVER (background colors: green, black, black, green, green)

*Note: Cannot show these colors in markdown, but they are currently working in the python shell using the colorama library*

In writing this code, we have been able to narrow down the steps necessary to get from this initial prototype to our eventual final product. There are two broad portions of the project left: making the Wordle game playable and building our AI Guesser. For making the game playable, the key steps will be to build a function that takes user input for guesses and makes sure it is within the proper boundaries (5 letters, within a list of allowable English words) and then to build a function that actually runs the gameplay in the shell (5 gueses, using `show_feedback` for each guess). For the AI Guesser, we plan to begin coding a method that will allow us to take all previous feedback and narrow down the list of allowable words to an AI-generated guess. We are looking forward to getting moving on these two milestones, and we hope to have some more progress to show soon!
