#Number Cruncher
import random



def playgame(x,y,answer):
    hints = ["Number is too high.", "Number is too low."]
    hint_counter = 0
    print(answer)

    

    while True:
        try:
            number = int(input("Pick a number between {} and {}, inclusive: ".format(x,y)))
        
        except ValueError:
            print("Must input an integer value!")
            continue
        else:
            break
    while x <= number <= y and number != answer:
        
        if number > answer:
            
            print(hints[0])
            hint_counter += 1
        elif number < answer:
            print(hints[1])
            hint_counter += 1
        print(f"Hint Count = {hint_counter}")
        if hint_counter > 5:
            print("Game Over!")
            break    
    
        while True:
            try:
                number = int(input("Guess Again! Pick a number between {} and {}, inclusive: ".format(x,y)))
        
            except ValueError:
                print("Must input an integer value!")
                continue
            else:
                break
    while x <= number <= y and number == answer:
        print("Congratulations! You have guessed the correct integer and have won the game!")
        break
    while number < x or number > y:
        while True:
            try:
                number = int(input("Must pick an integer within specified range. Pick a number between {} and {}, inclusive: ".format(x,y)))
            except ValueError:
                print("Must input an integer value!")
                continue
            else:
                break
        while x <= number <= y and number != answer:
        
            if number > answer:
            
                print(hints[0])
                hint_counter += 1
            elif number < answer:
                print(hints[1])
                hint_counter += 1
            print(f"Hint Count = {hint_counter}")
        
            if hint_counter > 5:
                print("Game Over!")
                break
            while True:
                try:
                    number = int(input("Guess Again! Pick a number between {} and {}, inclusive: ".format(x,y)))
                except ValueError:
                    print("Must input an integer value!")
                    continue
                else:
                    break
        while x <= number <= y and number == answer:
            print("Congratulations! You have guessed the correct integer and have won the game!")
            break
        
                

def easy():
    playgame(1,10,random.randint(1,10))
        
def medium():
    playgame(1,100,random.randint(1,100))
    
def hard():
    playgame(1,1000,random.randint(1,1000))


    
difficulty_levels = {"Easy": "1-10", "Medium": "1-100", "Hard" : "1-1000"}
for key in difficulty_levels:
    print(key + ":" + " " + difficulty_levels[key])

choose_level = ["Easy", "Medium", "Hard"]
x = input("Choose a level {}:".format(choose_level) + " ")
print("You chose: {}".format(x))

if x == "Easy":
    easy()
elif x == "Medium":
    medium()
elif x == "Hard":
    hard()


while x not in choose_level:
    print("Typo Error. You must type 'Easy', 'Medium', or 'Hard' to choose a level.")
    x = input("Choose a level {}:".format(choose_level) + " ")
    print("You chose: {}".format(x))
    if x == "Easy":
        easy()
    elif x == "Medium":
        medium()
    elif x == "Hard":
        hard()

