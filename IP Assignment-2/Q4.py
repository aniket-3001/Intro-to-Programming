import random
import requests


def valid_guess(guess):  # function to check if entered word is valid or not
    if len(guess) != 5 or (not guess.islower()):
        return False
    try:
        api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        req_obj = requests.get(api_url+guess)  # api_url+guess is our endpoint

        # since an API call made to check for non-meaningful words would return a dictionary having three elements
        if len(req_obj.json()) == 3:
            return False
        return True
    except:
        return True  # in case API gets shut down, run the program for a possible non-meaningful word instead of throwing an error


def hangman(word, guess):  # main hangman function
    hangman_str = ""  # string to be printed
    occ = ""  # string containing letters occuring in hangman word but not at right index
    l = []  # list containing letters occuring in hangman word not occuring in hangman string and not at right index

    for i in range(5):
        if word[i] == guess[i]:
            hangman_str += word[i]
        else:
            hangman_str += '-'
            if word[i] not in l:
                l += [word[i]]

    for c in l:
        if word.count(c) > guess.count(c):
            occ += c*(guess.count(c)-hangman_str.count(c))
        elif word.count(c) < guess.count(c):
            occ += c*(word.count(c)-hangman_str.count(c))
        else:
            occ += c*(guess.count(c)-hangman_str.count(c))

    print(hangman_str)

    if len(occ) != 0:  # for printing the characters which are present in the hangman word but not at correct index
        print("other characters present: ", end='')
        for i in range(len(occ)):
            if i == len(occ)-1:
                print(occ[i])
                print()
            else:
                print(occ[i], end=', ')
    else:
        print()


l = ["abuse", "adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "board", "brain", "bread", "break", "brown", "buyer", "cause", "chain", "chair", "chest", "chief", "child", "china", "claim",
     "class", "clock", "coach", "coast", "court", "cover", "cream", "crime", "cross", "crowd", "crown", "cycle", "dance", "death", "depth", "doubt", "draft", "drama", "dream", "dress", "drink", "drive", "earth", "enemy", "entry"]

word = l[random.randint(0, len(l)-1)]
print(word)

print()
print("Now you will be asked to guess the hangman word. You have six tries. Please add five-letter lowercase words.")
print()

tries = 0
while tries < 6:
    guess = input("Enter a guess: ")
    if not valid_guess(guess):
        print("Enter a valid word!")
        print()
        continue
    if guess == word:
        print("You got it right!")
        break
    hangman(word, guess)
    tries += 1
else:
    print("Failed. You let a kind man die :(")
    print("The correct word is:", word)
    print("Better luck next time!")


def valid_guess(guess):  # function to check if entered word is valid or not
    if len(guess) != 5 or (not guess.islower()):
        return False
    try:
        api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        req_obj = requests.get(api_url+guess)  # api_url+guess is our endpoint

        # since an API call made to check for non-meaningful words would return a dictionary having three elements
        if len(req_obj.json()) == 3:
            return False
        return True
    except:
        return True  # in case API gets shut down, run the program for a possible non-meaningful word instead of throwing an error


def hangman(word, guess):  # main hangman function
    hangman_str = ""  # string to be printed
    occ = ""  # string containing letters occuring in hangman word but not at right index
    l = []  # list containing letters occuring in hangman word not occuring in hangman string and not at right index

    for i in range(5):
        if word[i] == guess[i]:
            hangman_str += word[i]
        else:
            hangman_str += '-'
            if word[i] not in l:
                l += [word[i]]

    for c in l:
        if word.count(c) > guess.count(c):
            occ += c*(guess.count(c) - hangman_str.count(c))
        elif word.count(c) < guess.count(c):
            occ += c*(word.count(c) - hangman_str.count(c))
        else:
            occ += c*(guess.count(c) - hangman_str.count(c))

    print(hangman_str)

    if len(occ) != 0:  # for printing the characters which are present in the hangman word but not at correct index
        print("other characters present: " + (', '.join(occ)))
        print()
    else:
        print()


l = ["abuse", "adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "board", "brain", "bread", "break", "brown", "buyer", "cause", "chain", "chair", "chest", "chief", "child", "china", "claim",
     "class", "clock", "coach", "coast", "court", "cover", "cream", "crime", "cross", "crowd", "crown", "cycle", "dance", "death", "depth", "doubt", "draft", "drama", "dream", "dress", "drink", "drive", "earth", "enemy", "entry"]

word = l[random.randint(0, len(l)-1)]

print()
print("Now you will be asked to guess the hangman word. You have six tries. Please add five-letter lowercase words.")
print()

tries = 0
while tries < 6:
    guess = input("Enter a guess: ")
    if not valid_guess(guess):
        print("Enter a valid word!")
        print()
        continue
    if guess == word:
        print("You got it right!")
        break
    hangman(word, guess)
    tries += 1
else:
    print("Failed. You let a kind man die :(")
    print("The correct word is:", word)
    print("Better luck next time!")
