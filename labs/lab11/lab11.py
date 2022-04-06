"""
Name: Brett Widholm
lab11.py

Problem: Imports and uses the classes 'Button' and 'Door' to make a game
where the user tries to find the secret door.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from door import Door
from button import Button
import random
from graphics import GraphWin, Point, Rectangle, Text

def three_door_game():
    wins = 0
    losses = 0

    win = GraphWin('Secret Door Game', 600, 700)
    door_shape_1 = Rectangle(Point(50, 300), Point(200, 600))
    door_shape_2 = Rectangle(Point(225, 300), Point(375, 600))
    door_shape_3 = Rectangle(Point(400, 300), Point(550, 600))

    button_rectangle = Rectangle(Point(400, 50), Point(550, 150))
    button = Button(button_rectangle, 'Quit')

    button.draw(win)

    door_1 = Door(door_shape_1, 'Door 1')
    door_2 = Door(door_shape_2, 'Door 2')
    door_3 = Door(door_shape_3, 'Door 3')

    wins_text = (Text(Point(50, 75), "Wins:"))
    losses_text = (Text(Point(50, 100), "Losses:"))

    loser = (Text(Point(300, 250), "Sorry, incorrect!"))
    winner = (Text(Point(300, 250), "Winner!"))
    top_text = (Text(Point(300, 250), "I have a secret door."))
    instruction_text = (Text(Point(300, 650), "Click to guess which is the secret door!"))
    play_again_text = (Text(Point(300, 650), "Click anywhere play again."))

    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    door_1.color_door('brown')
    door_2.color_door('brown')
    door_3.color_door('brown')

    starter = (Text(Point(300, 150), "Click to start!!"))

    starter.draw(win)

    wins_text.draw(win)
    losses_text.draw(win)
    top_text.draw(win)
    instruction_text.draw(win)

    clicker = win.getMouse()
    starter.undraw()
    while not button.is_clicked(clicker):
        wins_counter = (Text(Point(100, 75), wins))
        losses_counter = (Text(Point(100, 100), losses))
        door_1.color_door('brown')
        door_2.color_door('brown')
        door_3.color_door('brown')
        wins_counter.draw(win)
        losses_counter.draw(win)
        winner.undraw()
        loser.undraw()
        play_again_text.undraw()

        random_door = random.randint(1,3)

        if random_door == 1:
            door_1.set_secret(True)
        if random_door == 2:
            door_2.set_secret(True)
        if random_door == 3:
            door_3.set_secret(True)
        clicker = win.getMouse()
        if door_1.is_clicked(clicker) == True and door_1.is_secret() == True:
            wins += 1
            play_again_text.draw(win)
            winner.draw(win)
            top_text.undraw()
            instruction_text.undraw()
            wins_counter.undraw()
            losses_counter.undraw()
            door_1.set_secret(False)
            door_1.color_door('green')
        elif door_2.is_clicked(clicker) == True and door_2.is_secret() == True:
            wins += 1
            play_again_text.draw(win)
            winner.draw(win)
            top_text.undraw()
            instruction_text.undraw()
            wins_counter.undraw()
            losses_counter.undraw()
            door_2.set_secret(False)
            door_2.color_door('green')
        elif door_3.is_clicked(clicker) == True and door_3.is_secret() == True:
            wins += 1
            play_again_text.draw(win)
            winner.draw(win)
            top_text.undraw()
            instruction_text.undraw()
            wins_counter.undraw()
            losses_counter.undraw()
            door_3.set_secret(False)
            door_3.color_door('green')


        else:
            wins_counter.undraw()
            losses_counter.undraw()
            play_again_text.draw(win)
            loser.draw(win)
            top_text.undraw()
            instruction_text.undraw()
            losses += 1
            if door_1.is_secret() == True:
                door_1.color_door('green')
            elif door_2.is_secret() == True:
                door_2.color_door('green')
            elif door_3.is_secret() == True:
                door_3.color_door('green')
            if door_1.is_clicked(clicker) == True:
                door_1.color_door('red')
            elif door_2.is_clicked(clicker) == True:
                door_2.color_door('red')
            elif door_3.is_clicked(clicker) == True:
                door_3.color_door('red')

            door_1.set_secret(False)
            door_2.set_secret(False)
            door_3.set_secret(False)
        clicker = win.getMouse()

    win.close()





    #win.close()
    #print('fu')