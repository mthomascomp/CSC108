# Student Name: Mervin Thomas
# Course Code: CSC108
# Instructor: Sadia Sharmin 
# Due Date: January 28, 2018 
# Assignment: bobs_compatibility

import random

def fave_number():
    '''
    (int) -> int

    A prederminted number called fave_number is in the function.
    This function Returns a new_fave number by implementing a
    certain set of calculations. Then determines if that number
    is divisible by 5. 

    >>> fave_number()
    124480
    Is new fave number divisible by 5? True
    '''
    fave_number = 1
    new_fave = ((((fave_number + fave_number) *2 ) ** 5) + 123456)
    print (new_fave)
    new_fave_mod = new_fave % 5
    if new_fave_mod == 0:
        print("Is new fave number divisible by 5? True")
    else:
        print("Is new fave number divisible by 5? False")
fave_number()

def fave_number_2():
    '''
    (int) -> int

    A predetermined number called fave_number_2 is set in the function.
    This function takes the fave_number_2 and returns a new_fav_number_2
    based on the calculations inside the functions.
    then checks if it is divisible by 5 or not. Then determines if
    that number is divisible by 5. 

    >>> fave_number_2()
    133827698112
    Is new fave number #2 divisible by 5? False
    '''
    fave_number_2 = 42
    new_fave_2 = (((((fave_number_2 + fave_number_2) * 2) ** 5) + 123456))
    print (new_fave_2)
    if (new_fave_2 % 5 == 0):
        print("Is new fave number #2 divisible by 5? True")
    else:
        print("Is new fave number #2 divisible by 5? False")       
fave_number_2()

def fave_word():
    '''
    (str) -> str

    A predetermined fave_Word called 'helloworld' is set.
    This function adds the word bob n times where in n is
    determined by the random number generator. 

    >>> fave_word()
    helloworldBobBobBob
    '''
    fave_word = 'helloworld'
    final_1 = fave_word + ("Bob" * random.randint(0,3))
    print(final_1)
fave_word()

def fave_word_2():
    '''
    (str) -> str

    A predetermined fave_Word called 'csc108world' is set.
    This function adds the word bob n times where in n is
    determined by the random number generator. 

    >>> fave_word_2()
    csc108worldbob
    '''
    fave_word_2 = 'csc108world'
    final_2 = fave_word_2 + ("Bob" * random.randint(0,3))
    print(final_2)
fave_word_2()

def fave_word_3():
    '''
    (str) -> str

    A predetermined fave_Word called 'catzworld' is set.
    This function adds the word bob n times where in n
    is determined by the random number generator. 

    >>> fave_word_3()
    catzworldbobbob
    '''
    fave_word_3 = 'catzworld'
    final_3  = fave_word_3 + ("Bob" * random.randint(0,3))
    print (final_3)
fave_word_3()
