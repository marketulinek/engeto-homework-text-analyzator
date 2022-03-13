# engeto-homework-text-analyzator

CURRENTLY WORK IN PROGRESS

Homework for Python Academy - Text Analyzator


# Task Assignment

The goal is to creat Text Analyzator - program which can process arbitrarily long text a get some stats.

The program has to contain:

    1) Ask user to enter username and password
    2) Check if entered values correspond to the registered users list
    3) If YES, welcome the user and enable him to analyze texts
    4) If NO, alert the user and terminate the program

    5) The program has to let the user choose between available texts:
        If the user entered the wrong number or something else instead,
        alert the user and terminate the program

    6) For the chosen text the program will do these statistics:
        - number of words
        - number of words starting with upper letter
        - number of words with all upper letters
        - number of words with all lower letters
        - number of numbers (not cipher)
        - summary of numbers in the text (not cipher)

    7) The program will create a bar graph representing the word length frequency

        EXAMPLE:

        ------------------------
        LEN|  OCCURENCES  |NR.
        ------------------------
        1|*             |1
        2|*********     |9
        3|******        |6
        4|***********   |11
        ...
