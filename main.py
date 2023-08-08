import turtle
import time
import pygame
import random

ding = time.time()
xp = 0

pygame.init()

wn = turtle.Screen()

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 0)
pen.color("black")

def chill_m():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("cat_sleep.mp3"))
def sleep(sec):
    time.sleep(sec)
def script(word):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("fast_type.mp3"))
    wor = ""
    for i in word:
        wor += i
        time.sleep(0.06)
        pen.clear()
        pen.write(wor, align="center", font=("Courier", 17, "normal"))
    pygame.mixer.Channel(1).stop()
    sleep(1)

def slow_script(word):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("fast_type.mp3"))
    wor = ""
    for i in word:
        wor += i
        time.sleep(0.2)
        pen.clear()
        pen.write(wor, align="center", font=("Courier", 17, "normal"))
    pygame.mixer.Channel(1).stop()
    sleep(1)

def speed_script(word):
    pen.clear()
    pen.write(word, align="center", font=("Courier", 17, "normal"))

def two_sound(s1, s2):
    pygame.mixer.Channel(2).play(pygame.mixer.Sound(s1))
    pygame.mixer.Channel(3).play(pygame.mixer.Sound(s2))

script("This game is coded by Caleb Choe.")
script("Welcome to... T h e   G a m e.")

time.sleep(1)

chill_m()
time.sleep(1)
script("hi.")
script("This is a game.")
script("There is not much to do here, really.")
script("But if you want to play a game...")
script("I bet I can find something.")

bob = turtle.Turtle()
bob.speed(0)
bob.shape("circle")
bob.color("black")
bob.shapesize(stretch_wid=2, stretch_len=2)
bob.penup()
bob.goto(0, 0)
speed = 10

def up():
    y = bob.ycor()
    y += speed
    bob.sety(y)

def down():
    y = bob.ycor()
    y -= speed
    bob.sety(y)

def right():
    x = bob.xcor()
    x += speed
    bob.setx(x)

def left():
    x = bob.xcor()
    x -= speed
    bob.setx(x)

def die():
    script("you were too slow to kill it...")
    slow_script("You deserve death.")
    script(f"You died with {xp} xp.")
    print("ACHIEVEMENT! Garbage fighter")
    quit()

script("Here, play around with this dot. It's name is Bob.")

wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

script("Kinda boring...")

script("Let's play a new game.")
script("You think of a number, and I try to guess it.")
script("Check the interpreter.")

def guess():
    num = int(input("Type a number between 0 and 1000. "))

    if num > 1000 or num < 0:
        script("You nasty cheater. I quit.")
        print("Well, The End.")
        print("ACHIEVEMENT! Number Tracking Failure.")
        quit()

    idk = 500
    count = 1
    t = int(idk / 2)

    script(f"Is it {idk}?")

    while idk != num:
        if num > idk:
            idk += t
        else:
            idk -= t
        count += 1
        script(f"Is it {idk}?")

        if t == 3:
            t = 2
        else:
            t //= 2
        if t == 0:
            t = 1
    script("GOT IT!")
    script(f"It took me {count} tries to guess your number.")
    if count == 1:
        print("ACHIEVEMENT: Really Easy Number")
    script("Play again? Type in the interpreter.")
    play = input("Play again? Type Y or N. ")
    if play == "Y":
        guess()

guess()

script("Ok.")
script("I'm going to do something.")
script("Goodbye Bob.")
pygame.mixer.Channel(0).stop()

e = 0
wn.bgcolor("red")

while e < 100:
    bob.color("red")
    bob.color("black")
    e += 1

bob.hideturtle()

script("hehehehe")
script("your friend is gone")
script("die")

wn.bgcolor("green")

wn.register_shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\space_invader.gif")

class enemy:
    def __init__(self, hp):
        self.hp = hp

space_invader = turtle.Turtle()
space_invader.shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\space_invader.gif")
space_invader.speed(0)
space_invader.penup()
space_i = enemy(50)

pen.color("dark green")

script("I am actually a virus.")
script("I can only die if you can hit me enough.")

pygame.mixer.Channel(0).play(pygame.mixer.Sound("space_invaders_battle.mp3"))
lives = 50


def dmg_space(thing, name):
    name.goto(random.randint(-77, 77) * 5, random.randint(-55, 55) * 5)
    thing.hp -= 1
    speed_script(f"{thing.hp}")

start = time.time()

while space_i.hp > 0:
    space_invader.onclick(lambda x, y: dmg_space(space_i, space_invader))
    if space_i.hp == 0:
        end = time.time()
        result = end - start
        space_invader.hideturtle()
        script("ahh......")
        script("I think I'm dying...")
        script("hehe...")
        slow_script("hehe...")
        if result <= 30:
            print("\nACHIEVEMENT! 30 Second Space Killer")
            if result <= 25:
                print("ACHIEVEMENT! 25 Second Space Killer, fast!")
                if result <= 18:
                    print("ACHIEVEMENT! 18 Second Space Killer, legendary!")
        print(f"You took {result} seconds to kill the boss.")
        if result >= 60:
            die()

pygame.mixer.Channel(0).stop()

chill_m()
wn.bgcolor("white")
pen.color("blue")

slow_script("hi???")
script("Ok, you're not a monster.")
script("hi.")
script("Name's jeff.")
script("I haven't seen a human in a while.")
script("2746 days, 3 hours, 48 minutes, 24 seconds exactly.")
script("Well, that number just changed.")
script("Oh shoot, some things are coming...")

s_invader = enemy(20)
s_invader2 = enemy(20)

wn.register_shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\s_invader.gif")

s_i = turtle.Turtle()
s_i.shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\s_invader.gif")
s_i.speed(0)
s_i.penup()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("chill_8bit_rave.mp3"))

def battle(name, image, gain, limit):
    global xp
    script(f"{name.hp}")
    start2 = time.time()
    while name.hp > 0:
        image.onclick(lambda x, y: dmg_space(name, image))
        if name.hp == 0:
            end2 = time.time()
            result2 = end2 - start2
            image.hideturtle()
            if result2 >= limit:
                die()
            xp += gain
            script(f"Gained {gain} xp. You now have {xp} xp.")

battle(s_invader, s_i, 5, 20)
script("Another one!")
time.sleep(1)
s_i.showturtle()
battle(s_invader2, s_i, 5, 20)

script("Thanks for the help!")
script("Hm, you got some skill,\nmaybe you should become a fighter.")
script("I have 3 60 second tasks.")
script("They range in difficulty, and the harder, \nthe better reward you get.")
script("Check the interpreter.")

wn.register_shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_e.gif")
wn.register_shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_m.gif")
wn.register_shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_h.gif")

reaper = turtle.Turtle()
reaper.speed(0)
reaper.penup()

def reaper_choose():

    enemy_i = input("1 is easy, 2 is medium, and 3 is hard.\nWhich do you choose? You get 60 seconds to kill the enemy.")
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("reaper_chase.mp3"))
    reaper.showturtle()

    if enemy_i == "1":
        script("Easy.")
        reaper.shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_e.gif")
        reaper_i = enemy(50)
        add = 10
    elif enemy_i == "2":
        script("Medium.")
        reaper.shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_m.gif")
        reaper_i = enemy(75)
        add = 20
    else:
        script("Hard.")
        reaper.shape(r"C:\Users\pooki\PycharmProjects\pythonProject30\grim_h.gif")
        reaper_i = enemy(100)
        add = 30
    battle(reaper_i, reaper, add, 60)
    script("Check the interpreter.")
    yes = input("Battle again? Type Y or N. ")
    if yes == "Y":
        reaper_choose()

reaper_choose()

end = time.time()
lapsed = int(end - ding)
script(f"You took {lapsed} seconds to complete the game.")
script(f"You finished with {xp} xp. Nice!")
script("Thank you for playing! Continuing soon!")

wn.mainloop()
