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

def uses_only(word, letters):
    '''
    >>> uses_only("hello", 'hello')
    True
    
    >>> uses_only("hello", 'HELLO')
    True
    
    >>> uses_only("hello", 'HELLOU')
    True
    
    >>> uses_only('jack', 'hello')
    False

    '''
    for letter in word:
        if letter.lower() not in letters.lower():
            return False
    return True
    
def words_with_only(letters):
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word, letters) == True:
                    print(word)
    
def uses_all(word, letters):
    '''
    >>> uses_all('hello', 'hel')
    True
    
    >>> uses_all('hello', 'helLO')
    True
    
    >>> uses_all('hello', 'HelloJ')
    False
    
    >>> uses_all('heLLo', 'HEllo')
    True
    '''
    for letter in letters:
        if letter.lower() not in word.lower():
            return False
    return True
    
def how_many_uses_all(letters):
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word, letters) == True:
                    count += 1
    print(count)

def is_abecedarian(word):
    '''
    >>> is_abecedarian("Aegilops")
    True
    
    >>> is_abecedarian("abcde")
    True
    
    >>> is_abecedarian('abCdde')
    True
    
    >>> is_abecedarian('abcdzy')
    False
    '''
    old_letter = "a"
    for letter in word:
        if letter.lower() >= old_letter.lower():
            old_letter = letter
        else:
            return False
    return True

def count_abecedarian():
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abecedarian(word):
                    count += 1
    print(count)




if __name__ == "__main__":
    #at_least()
    #no_e()
    #print(avoids("hello", "abcdE"))
    #count_avoids('jxzwq')
    #print(uses_only("hello", "hEloj"))
    #words_with_only('catb')
    #print(uses_all("hello", "hElo"))
    #how_many_uses_all("heLO")
    #print(is_abecedarian("Aegilops"))
    #count_abecedarian()
    pass
    

    