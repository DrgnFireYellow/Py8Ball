#import modules
import random
from time import sleep
import turtle

def draw_8_ball(answer):
    #Draw 8 ball.
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.color('black')
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.color('white')
    turtle.fillcolor('white')
    turtle.up()
    turtle.left(90)
    turtle.fd(45)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(55)
    turtle.end_fill()
    turtle.left(90)
    turtle.forward(55)
    turtle.color('black')
    turtle.write(answer, align='center')

#Configure user input
while True:
    question = input('''Ask anything, or type "quit"... ''')
    if question != "quit":
        answers_file = open('answers.txt')
        answers = answers_file.readlines()
        answer = answers[random.randint(0, 7)]

        draw_8_ball(answer)
        #Print random answer.
        print(answer)

    #Quit program when user types "quit".
    else:
        print("Program ending in 3 seconds...")
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        print("Program ending.")
        sleep(0.5)
        quit()
