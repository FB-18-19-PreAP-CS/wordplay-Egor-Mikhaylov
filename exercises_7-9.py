def has_three_double_letters(word):
    '''
    >>> has_three_double_letters("abc")
    False
    
    >>> has_three_double_letters("abcabc")
    False
    
    >>> has_three_double_letters("aabbcc")
    True
    
    >>> has_three_double_letters("aAbBCC")
    True
    
    >>> has_three_double_letters("aabbcjcc")
    False
    '''
    prev_letter = ""
    count = 0
    consecutive_doubles = 0
    word = word.lower()
    if len(word) >= 6:
        for i in range(len(word)-5):
            if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                return True
    return False

def print_three_double_letter_word():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if has_three_double_letters(word):
                    print(word)

def is_reversed_age(age1, age2):
    age1 = str(age1)
    age2 = str(age2)
    if age1 < 2:
        new_age1 == "0" + age1
    if age2 < 2:
        new_age2 == "0" + age1
    if len(age1) >= 2 and len(age2) >= 2:
        if age1[0] == age2[1] and age1[1] == age2[0]:
            return True
    return False

def reversed_age():
    for i in range(100):
        for j in range(100):
            if is_reversed_age(i, j):
                print(i, j)
    
if __name__ == "__main__":
    print("Exercise #7:")
    print_three_double_letter_word()
    print()
    