def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                    
def no_e():
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.strip().split():
                if "e" not in word:
                    count += 1
        print(count)

def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    return True

if __name__ == "__main__":
    #at_least
    #no_e
    #print(avoids("hello", "abcde"))
    pass