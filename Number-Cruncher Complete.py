#Number Cruncher
import random
print("Welcome to Number Cruncher!")
print("Objective: You must guess a number in a chosen range within 5 hints.\n")

difficulty_levels = {"Easy" : 1-10, "Medium" : 1-100, "Hard" : 1-1000}

print("\u0332".join("Levels "))
difficulty_levels = {"Easy": "1-10", "Medium": "1-100", "Hard" : "1-1000"}
for key in difficulty_levels:
    print(key + ":" + " " + difficulty_levels[key])

def playgame(x,y,answer):
    
    hints = ["Number is too high!", "Number is too low!"]
    hint_counter = 0

    while True:
        game_switch = [0, 1]
        try:
            number = int(input("\nPick a number between {} and {}, inclusive: ".format(x,y)))
        except ValueError:
            print("Must input an integer value!")
            continue
        if number < x:
            print("Must pick an integer within specified range.")
            continue
        if number > y:
            print("Must pick an integer within specified range.")
            continue
        else:
            while x <= number <= y and number != answer:
                if number > answer:
                    print(hints[0])
                    hint_counter += 1
                elif number < answer:
                    print(hints[1])
                    hint_counter += 1
                if hint_counter <= 5:
                    print(f"Hint Count = {hint_counter}")
                    print("Guess Again!")
                elif hint_counter > 5:
                    print(f"Answer was: {answer}")
                    print("Game Over!")
                    game_switch = 0
                break
                
            while x <= number <= y and number == answer:
                print("Congratulations! \nYou have guessed the correct integer and have won the game!")
                game_switch = 0
                break
        
        if game_switch == 0:
            break
        elif game_switch == 1:
            continue


def easy():
    playgame(1,10,random.randint(1,10))

def medium():
    playgame(1,100,random.randint(1,100))

def hard():
    playgame(1,1000,random.randint(1,1000))
    
 
def goto_level():
    if x == "Easy":
        easy()
    elif x == "Medium":
        medium()
    elif x == "Hard":
        hard()


    
decisions = ["Yes", "No"]    
choose_level = ["Easy", "Medium", "Hard"]
x = input("\nChoose a level {}:".format(choose_level) + " ")
print("The level you selected was: {}\n".format(x))

while True:

    loop_control = [0,1]
    while x not in choose_level:
        print("Typo Error! \nYou must type 'Easy', 'Medium', or 'Hard' to choose a level.\n")
        x = input("Choose a level {}:".format(choose_level) + " ")
        print("The level you selected was: {}\n".format(x))

    while x in choose_level:
        y = input("Are you sure you want to play this level?: ")
        if y == "Yes":
            goto_level()
            loop_control = 0
            break
        elif y == "No":
            x = input("\nChoose a level {}:".format(choose_level) + " ")
            print("The level you selected was: {}\n".format(x))
            loop_control = 1
            break
        elif y != "Yes" or "No":
            print('Typo Error! \nYou must type "Yes" or "No".\n')
            
     
    if loop_control == 0:
        break
    elif loop_control == 1:
        continue

while True:
    on_off = [0,1]
    possible = ["Yes", "No"]
    play = input("Do you want to play again?: ")
    if play == "No":
        break
    if play == "Yes":
        decisions = ["Yes", "No"]    
        choose_level = ["Easy", "Medium", "Hard"]
        x = input("\nChoose a level {}:".format(choose_level) + " ")
        print("The level you selected was: {}\n".format(x))

        while True:

            loop_control = [0,1]
            while x not in choose_level:
                print("Typo Error! \nYou must type 'Easy', 'Medium', or 'Hard' to choose a level.\n")
                x = input("Choose a level {}:".format(choose_level) + " ")
                print("The level you selected was: {}\n".format(x))

            while x in choose_level:
                y = input("Are you sure you want to play this level?: ")
                if y == "Yes":
                    goto_level()
                    loop_control = 0
                    break
                elif y == "No":
                    x = input("\nChoose a level {}:".format(choose_level) + " ")
                    print("The level you selected was: {}\n".format(x))
                    loop_control = 1
                    break
                elif y != "Yes" or "No":
                    print('Typo Error! \nYou must type "Yes" or "No".\n')
                    
             
            if loop_control == 0:
                break
            elif loop_control == 1:
                continue
        

        
    elif play not in possible:
        print('Typo Error! \nYou must type "Yes" or "No".')
        continue

       

        
