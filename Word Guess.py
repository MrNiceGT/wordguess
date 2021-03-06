# Import libraries
from random import shuffle
from data.words import words

def show_categorySelect(words):
    words_list = list()
    while True:
        keys = list(words.keys())
        print("Choose categories:")
        for i in range(len(keys)):
            print(f"[{i+1}] {keys[i].title()} ({len(words[keys[i]])} words)")
        print("[X] Exit")
        command = input("> ")

        if command == "X" or command == "x":
            break
        else:
            try:
                key = int(command) - 1
                words_list = words[keys[key]]
                break
            except ValueError:
                print("Error: Invalid input.")
            except KeyError:
                print("Error: Chosen category is non-existent.")

    return words_list

def show_gameScreen(words_list):
    score = 0
    ctr = 0
    hint_no = 0
    keys = list(words_list.keys())
    shuffle(keys)

    print("Welcome to the game. Good luck and try your best :)")
    print("Type '/hint' to get a hint.") 
    while ctr < len(words_list):
        the_word = keys[ctr]
        
        print(f"Question {ctr+1}. What {words_list[keys[ctr]]}?")
        answer = input("> ").lower().strip()

        if answer == "/hint":
            if hint_no < 3:
                show_hint(the_word, hint_no)
                print("You asked for a hint. (-0.5 points)")
                score -= 1
                hint_no += 0.5
            else:
                print("Looks like you're out of hints for this question.")
        elif answer == the_word:
            print("Good job, you got the correct answer! (+1 point)")
            score += 1
            ctr += 1
            hint_no = 0
            print()
        else:
            print(f"Sorry, but the correct answer was: {the_word} (-1 point)")
            score -=1
            ctr += 1
            hint_no = 0
            print()
            
    if score < 0:
        score = 0
        
    print(f"Your final score is: {score}")
    show_flavorText(score, len(words_list))

def show_hint(word, hint_no):
    hint = ""

    if hint_no == 0:
        print(f"Hint: It starts with the letter {word[0]}.")
    elif hint_no == 1:
        print(f"Hint: It ends with the letter {word[-1]}.")
    elif hint_no == 2:
        print(f"Hint: It has a length of {len(word)} letters.")

def show_flavorText(score, divisor):
    if score / divisor == 1:
        print("Perfect! Congratulations!")
    elif score / divisor == 0:
        print("Oof! That's okay, you can do better next time! :)")
    elif score / divisor > 0.5:
        print("That's more than half! Good work :D")
    elif score / divisor < 0.5:
        print("That's less than half. Better luck next time :)")
        
# Program loop
running = True

while running:
    print("===========================")
    print("Word Guess v2.0 by zyenapz")
    print("Website: zyenapz.github.io")
    print("[1] Play")
    #print("[2] Show Hi-Score")
    print("[X] Exit")
    command = input("> ")

    if command == "1":
        words_list = show_categorySelect(words)
        score = show_gameScreen(words_list)
    elif command == "2":
        print("Error: Invalid input.") # TODO
    elif command == "X" or command == "x":
        running = False
    else:
        print("Error: Invalid input.")
