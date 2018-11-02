def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)

def has_no_e(word):
    '''
    >>> has_no_e('texas')
    False
    
    >>> has_no_e('longhorn')
    True

    >>> has_no_e('UTEP')
    False
    '''
    if "e" not in word.lower():
        return True
    return False

def no_e():
    with open("words.txt") as file:
        count = 0
        word_count = 0
        for line in file:
            for word in line.strip().split():
                word_count += 1
                if "e" not in word:
                    count += 1
        print(f"{count/word_count*100:.3f}")

def avoids(word, forbidden_letters):
    '''
    >>> avoids('Texas', 'tpr')
    False
    
    >>> avoids('Texas', 'bcd')
    True
    
    >>> avoids('TEXAS', 'top')
    False
    
    >>> avoids('texas', 'Top')
    False
    '''
    for letter in forbidden_letters:
        if letter.lower() in word.lower():
            return False
    return True

def count_avoids(forbidden_letters):
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word, forbidden_letters) == True:
                    count += 1
    print(count)
        

if __name__ == "__main__":
    #at_least()
    #no_e()
    #print(avoids("hello", "abcdE"))
    #count_avoids('jxzwq')
    pass