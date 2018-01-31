# Student Name: Mervin Thomas
# Course Code: CSC108
# Instructor: Sadia Sharmin 
# Due Date: January 28, 2018 
# Assignment: bobs_compatibility

################

# NOTE FROM BOB: DO NOT EDIT THIS STRING
# SIGNS_GROUPS is a string representing a group for each sign:
# - Group 0 has Aries, Leo, and Saggitarius
# - Group 1 has Taurus, Virgo and Capricorn
# - Group 2 has Gemini, Libra, Aquarius
# - Group 3 has Pisces, Scorpio and Cancer
SIGN_GROUPS = '[ARI,LEO,SAG],[TAU,VIR,CAP],[GEM,LIB,AQU],[PIS,SCO,CAN]'

# NOTE FROM BOB: DO NOT EDIT THIS STRING
# SIGNS is a string representing the start and end date of each sign
# Each star sign is represented using three characters (e.g. Aries = ARI)
# This is followed by a : and then the start month and start date
# and then a - and then the end month and end date
# (e.g. Aries starts on 03,21 (March 21), and ends on 04,19 (April 19))
# Each star sign's information ends with a semicolon
SIGNS = 'ARI:03,21-04,19;TAU:04,20-05,20;GEM:05,21-06,21;CAN:06,22-07,22;' + \
        'LEO:07,23-08,22;VIR:08,23-09,22;LIB:09,23-10,23;SCO:10,24-11,20;' + \
        'SAG:11,21-12,21;CAP:12,22-01,20;AQU:01,21-02,21;PIS:02,22-03,20;'
'''
ARI - march 21 - April 19 
LEO - july 23 - August 22 
SAG - November 21 - December 21
TAU - April 20 - May 20 
VIR - August 23 - September 22
CAP - decmber 22 - January 20
GEM - May 21 - june 21
LIB - September 23 - October 23 
AQU - January 21 - February 21 
PIS - February 22 - March 20 
SCO - October 24 - November 20 
CAN - june 22 - July 22 
'''

def extract_month(bday):
    '''
    (str) -> int

    Given a string representing a date in the format DD-MM-YYYY, return the
    month within the string as an int.

    >> extract_month('02-08-1991')
    8

    >> extract_month('22-12-1995')
    12
    '''

    return int(bday[3:5])
    

def extract_date(bday):
    '''
    (str) -> int

    Given a string representing a date in the format DD-MM-YYYY, return the
    date within the string as an int.

    >> extract_date('02-08-1991')
    2

    >> extract_date('22-12-1995')
    22
    '''

    return int(bday[0:2])
 

def count_common_occurrences(word1, word2):
    '''
    (str, str) -> int

    Given two strings, word1 and word2, return how many characters in word1 are
    letters that also occur in word2. You can assume all characters in the
    given string are lowercase. Also, spaces do not count as a common character.

    Algorithm:
    - Go through each character in word1, one by one. If this character
      occurs in word2, then add 1 to the count. Return total count after
      you're done going through the characters.

    >>> count_common_occurrences('bob y', 'bobbette z')
    3

    >>> count_common_occurrences('bobbette z', 'bob y')
    4
    '''
    count = 0
    for letter in word1:
        if letter !=' ':
            if letter in word2:
                count += 1
    return count 
        
def get_sign_group(sign):
    '''
    (str) -> int

    Given a three character string representing a star sign, return
    which group (out of 0, 1, 2, or 3) this star sign belongs to.

    Use the SIGN_GROUPS string (already defined for you above) to figure
    out the group.
    i.e. As given by this string '[ARI,LEO,SAG],[TAU,VIR,CAP],[GEM,LIB,AQU],
    [PIS,SCO,CAN]'the signs ARI, LEO and SAG are in group 0, the signs TAU, /
    VIR, CAP are in group 1,and so on.

    >>> get_sign_group('ARI')
    0

    >>> get_sign_group('CAN')
    3
    '''
    # Broken down the groups in lists. 
    group_0= ['ARI','LEO','SAG']
    group_1= ['TAU','VIR','CAP']
    group_2 = ['GEM','LIB','AQU']
    group_3 = ['PIS','SCO','CAN']
    if sign in group_0:
        return 0
    if sign in group_1: 
        return 1
    if sign in group_2:
        return 2
    if sign in group_3:
        return 3 

def find_astrological_compatibility(sign_1, sign_2):
    '''
    (str, str) -> int

    Given two 3-character strings representing star signs, return an int
    representing how compatible they are.
    
    According to Bob's rules, the compatibility between signs is calculated
    based on the SIGN_GROUPS they belong in, as follows:
    - If the signs are in the same group, return 100
    - If both the signs are in an odd-numbered group (i.e. 1 and 3)
      OR if both are in an even group (i.e. 0 and 2), then return 70
    - For all other cases, return 50

    >>> find_astrological_compatibility('ARI', 'LEO')
    100

    >>> find_astrological_compatibility('GEM', 'LIB')
    100

    >>> find_astrological_compatibility('SAG', 'AQU')
    70
    
    >>> find_astrological_compatibility('VIR', 'PIS')
    70
    
    >>> find_astrological_compatibility('LEO', 'TAU')
    50

    >>> find_astrological_compatibility('AQU', 'SCO')
    50
    '''

    sign_groups = ['ARI','LEO','SAG','TAU','VIR','CAP','GEM','LIB'\
                   ,'AQU','PIS','SCO','CAN','']

    # used if statements to categorize the astrological_compaitibility
    # used index position method to sort it.

    # Group 0 Index 
    if sign_1 in sign_groups[0:3] and sign_2 in sign_groups[0:3]:
        return 100
    # Group 1 Index 
    if sign_1 in sign_groups[3:7] and sign_2 in sign_groups[3:7]:
        return 100
    # Group 2 Index 
    if sign_1 in sign_groups[7:10] and sign_2 in sign_groups[7:10]:
        return 100
    #Group 3 Index 
    if sign_1 in sign_groups[10:12] and sign_2 in sign_groups[10:12]:
        return 100
    # Even Groups of signs: 
    if (sign_1 in sign_groups[0:3]) and (sign_2 in sign_groups[6:9]):
        return 70
    # Odd groups of signs: 
    if (sign_1 in sign_groups[3:6]) and (sign_2 in sign_groups[9:12]):
        return 70
    else:
        return 50

def find_astrological_sign(month, date):
    '''
    (int, int) -> str
    
    Given two int values representing a month and a date, return a
    3-character string that gives us what star sign a person born in that
    month and on that date belongs to. Use the SIGNS string (already
    defined for you at the top of this file) to figure this out.

    NOTE FROM BOB: A lot of string slicing to do here. It looks like the
                   information for each sign is exactly 16 characters long.
                   We can probably use that.
                   
    >>>find_astrological_sign(1, 21)
    'AQU'
    >>>find_astrological_sign(2, 20)
    'AQU'
    >>> find_astrological_sign(10, 24)
    'SCO'
    >>>find_astrological_sign(12, 20)
    'SAG'
    '''

    #Astrological sign for month of january - February 
    if (int(month) == 1 and int(date) >= 21) or (int(month) == 2 and\
                                                 int(date) <= 21):
        astrological_sign = 'AQU'
        return astrological_sign
    #Astrological sign for month of February - March 
    elif (int(month) == 2 and int(date) >= 22) or (int(month) == 3 and\
                                                   int(date) <= 20):
        astrological_sign = 'PIS'
        return astrological_sign
    #Astrological sign for month of March - April
    elif (int(month) == 3 and int(date) >= 21) or (int(month) == 4 and \
                                                   int(date) <= 19):
        astrological_sign = 'ARI'
        return astrological_sign
    #Astrological sign for month of April - May
    elif (int(month) == 4 and int(date) >= 20) or (int(month) == 5 and \
                                                   int(date) <= 20):
        astrological_sign = 'TAU'
        return astrological_sign
    #Astrological sign for month of May - June
    elif (int(month) == 5 and int(date) >= 21) or (int(month) == 6 and \
                                                   int(date) <= 21):
        astrological_sign = 'GEM'
        return astrological_sign
    #Astrological sign for month of June - July 
    elif (int(month) == 6 and int(date) >= 22) or (int(month) == 7 and\
                                                   int(date) <= 22):
        astrological_sign = 'CAN'
        return astrological_sign
    #Astrological sign for month of July - August
    elif (int(month) == 7 and int(date) >= 23) or (int(month) == 8 and\
                                                   int(date) <= 22):
        astrological_sign = 'LEO'
        return astrological_sign
    #Astrological sign for month of August - September
    elif (int(month) == 8 and int(date) >= 23) or (int(month) == 9 and \
                                                   int(date) <= 22):
        astrological_sign = 'VIR'
        return astrological_sign
    #Astrological sign for month of September - October
    elif (int(month) == 9 and int(date) >= 23) or (int(month) == 10 and \
                                                   int(date) <= 23):
        astrological_sign = 'LIB'
        return astrological_sign
    #Astrological sign for month of October - November
    elif (int(month) == 10 and int(date) >= 24) or (int(month) == 11 and\
                                                    int(date) <= 20):
        astrological_sign = 'SCO'
        return astrological_sign
    #Astrological sign for month of November - December
    elif (int(month) == 11 and int(date) >= 21) or (int(month) == 12 and\
                                                    int(date) <= 21):
        astrological_sign = 'SAG'
        return astrological_sign


def get_bday_compatibility(bday1, bday2):
    '''
    (str, str) -> int

    Given two strings representing birthdates in the format DD-MM-YYYY,
    figure out what star sign each birthdate belongs to and return
    the astrological compatibility of the two signs.

    NOTE FROM BOB: This code should look similar in structure to the
                   get_name_compatibility function that I already finished.
                   That is, it should call on other functions for help,
                   and not be more than a couple of lines long in total.

    >>> get_bday_compatibility('12-05-1995', '11-05-1995')
    100
    >>> get_bday_compatibility('24-08-1957', '12-11-1980')
    70
    >>>get_bday_compatibility('12-05-1955', '19-03-1955')
    70
    >>>get_bday_compatibility('19-04-1957', '12-11-1980')
    50
    '''
    # Extract the month and the dates of both bday1 and bday2 by calling
    # for extract_month function built earlier
    bday1_month = (extract_month(bday1))
    bday1_date = (extract_date(bday1))
    bday2_month =(extract_month(bday2))
    bday2_date = (extract_date(bday2))

   # Creates two variables called astro_sign
   # These variables create the astrological sign of each pair of bday
    astro_sign_1 = (find_astrological_sign(bday1_month, bday1_date))
    astro_sign_2 = (find_astrological_sign(bday2_month, bday2_date))

    # Calculated the astro compatibility of the two signs which results
    # in the birthday sign 
    astro_compatibility = (find_astrological_compatibility(astro_sign_1,\
                                                           astro_sign_2 ))
    return astro_compatibility 
    
def get_name_compatibility(name1, name2):
    '''
    (str, str) -> int
    
    Given two strings, return their name compatibility.
    
    According to Bob's rules, this should be calculated by checking
    how many letters in the first name occurs in the second, and
    adding this to how many letters in the second name occurs in
    the first, and then multiplying this sum by 10.
    
    For example:
    If the names are BOB Y and BOBBETTE Z, then
    - for BOB Y, we get the number 3, because 3 letters in this name
      occur in the other
    - for BOBBETTE Z, we get the number 4, because 4 letters in this
      name occur in the other.
    
    The number returned for these two names should be 3 + 4 = 7,
    multiplied by 10 = 70.

    >>> get_name_compatibility('bob y', 'bobbette z')
    70

    >>> get_name_compatibility('sadia sharmin', 'ryan gosling')
    150
    '''

    return (count_common_occurrences(name1, name2) + \
            count_common_occurrences(name2, name1)) * 10

def calculate_love_score(name1, name2, bday1, bday2):
    '''
    (str, str, str, str) -> int

    Given four strings representing two names and two birthdates in the
    format DD-MM-YYYY, return the average of the name compatibility of the
    names given and the birthdate compatibility of the birthdates given.
    
    NOTE FROM BOB: I'm not going to worry about checking if this number
                   is greater than 100. It's fine.

    >>> calculate_love_score('csc', 'mat', '09-19-1999', '12-11-1998')
    25.0
    >>> calculate_love_score('Sadia Sharmin', 'Ryan Gosling', '24-08-1957', '12-11-1980')
    85.0
    '''
    
    return (get_name_compatibility(name1, name2) + \
            get_bday_compatibility(bday1, bday2)) / 2

def is_valid_date(bday):
    '''
    (str) -> bool

    Given a string, return True iff it is in the format DD-MM-YYYY, where
    each character in DD, MM, and YYYY is a number, and each are separated
    by a - character.

    >>> is_valid_date('30-02-1903')
    True

    >>> is_valid_date('01-20-1999')
    False
    
    >> is_valid_date('310-31-3123')
    False
    '''
    
    if count_common_occurrences(bday, '0123456789') == 8 and bday[2] == '-'\
       and bday[5] == '-':
        month = extract_month(bday)
        date = extract_date(bday)
        if ((month >= 1) and (month <= 12)) and \
           ((date >= 1) and (date <= 31)):
            return True
        
    return False

# ===================================================================== 
# NOTE FROM BOB:
# Do NOT change any of the lines below (feel free to comment them out
# for testing purposes though)
# p.s. remember to delete all your test stuff, and keep the code below
#      exactly the same as it is now as when you're handing it in
# =====================================================================

if __name__ == "__main__":

    name1 = input("Give me your first and last name: ")
    bday1 = input("Give me your birthdate in the format DD-MM-YYYY: ")
    while not is_valid_date(bday1):
        bday1 = input("Invalid input. Give me your birthdate in the format DD-MM-YYYY: ")

    print("=====")
    name2 = input("Give me your crush's first and last name: ")
    bday2 = input("Give me your crush's birthdate in the format DD-MM-YYYY: ")
    while not is_valid_date(bday2):
        bday2 = input("Invalid input. Give me your birthdate in the format DD-MM-YYYY: ")

    # The .lower() after the names turns all characters into lowercase so you don't
    # have to worry about comparisons taking into consideration both upper and lowercase of each letter
    print("You are " + str(calculate_love_score(name1.lower(), name2.lower(), bday1, bday2)) +"% compatible in love!")



