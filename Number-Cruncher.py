#Number Cruncher
import random
import turtle

def playgame(number, text, answer, x, y, othertext):
    number = int(input(text))
    answer = random.randint(x,y)
    while 1<=number1<=10 and number1 != answer:
        number1= int(input("Guess Again! Pick a number between x and y, inclusive."))
        if 1<=number1<=10 and number1 == answer:
            print("Congratulations! You guessed the correct number and have won the game!")
            draw_winner()
    

def draw_winner():
    screen = turtle.Screen()
    screen.bgcolor("white")
    a = turtle.Turtle()
    a.forward(100)
    screen.exitonclick()
    
def easy():
    number1 = int(input("Pick a number between 1 and 10, inclusive."))
    answer = random.randint(1,10)
    while 1<=number1<=10 and number1 != answer:
        number1= int(input("Guess Again! Pick a number between 1 and 10, inclusive."))
        if 1<=number1<=10 and number1 == answer:
            print("Congratulations! You guessed the correct number and have won the game!")
            draw_winner()
        
def medium():
    number2 = int(input("Pick a number between 1 and 100, inclusive."))
    answer = random.randint(1,100)
    while 1<=number2<=100 and number2 != answer:
        number2= int(input("Guess Again! Pick a number between 1 and 100, inclusive."))
        if 1<=number2<=100 and number2 == answer:
            print("Congratulations! You guessed the correct number and have won the game!")
            draw_winner()

def hard():
    number3 = int(input("Pick a number between 1 and 1000, inclusive."))
    answer = random.randint(1,1000)
    while 1<=number3<=1000 and number3 != answer:
        number3= int(input("Guess Again! Pick a number between 1 and 1000, inclusive."))
        if 1<=number3<=1000 and number3 == answer:
            print("Congratulations! You guessed the correct number and have won the game!")
            draw_winner()

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


