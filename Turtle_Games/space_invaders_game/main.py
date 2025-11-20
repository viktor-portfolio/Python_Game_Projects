from turtle import Turtle, Screen
import random as rnd
import time


PLAYER_MOVE_SPEED = 10
ENEMY_MOVE_SPEED = .3
BULLET_SPEED = 1

#SCREEN SETUP
def setup_window():
    window = Screen()
    window.setup(500,500)
    window.bgcolor("black")
    window.title("Space Invader Game With Turtles")
    window.tracer(0)

    return window

#PLAYER SETUP
def setup_player():
    space_turtle = Turtle("turtle")
    space_turtle.color("white")
    space_turtle.penup()
    space_turtle.setheading(90)
    space_turtle.teleport(0, -210)

    return space_turtle

def player_move_right():
    movement = player.xcor() + 10
    if movement > 230:
        movement = 230
    player.setx(movement)

def player_move_left():
    movement = player.xcor() - 10
    if movement < -230:
        movement = -230
    player.setx(movement)

#PROJECTILE
def create_bullet():
    player_bullet = Turtle("square")
    player_bullet.color("blue")
    player_bullet.shapesize(1, 0.2)
    player_bullet.penup()
    player_bullet.hideturtle()

    return player_bullet

def fire_bullet():
    if not projectile_bullet.isvisible():
        projectile_bullet.teleport(player.xcor(),player.ycor() + 20)
        projectile_bullet.showturtle()

def bullet_collision():
    global score
    for enemy in enemy_list:
        if enemy.isvisible() and projectile_bullet.isvisible():
            if projectile_bullet.distance(enemy) < 20:
                enemy.hideturtle()
                score += 10
                update_score()
                projectile_bullet.hideturtle()
                break

#ENEMIES
enemy_list = []
def create_enemy():
    spawn_x = -200
    spawn_y = 180
    gap_x = 40
    gap_y = 40

    for row in range(2):
        for col in range(8):
            enemy_space_turtle = Turtle("turtle")
            enemy_space_turtle.color("green")
            enemy_space_turtle.penup()
            enemy_space_turtle.setheading(-90)
            enemy_space_turtle.goto(spawn_x + col * gap_x, spawn_y - row * gap_y)
            enemy_list.append(enemy_space_turtle)

enemy_direction = 1
def enemy_movement():
    global enemy_direction

    for enemy_turtle in enemy_list:
        enemy_turtle.setx(enemy_turtle.xcor() + ENEMY_MOVE_SPEED * enemy_direction)
        if enemy_turtle.xcor() > 230 or enemy_turtle.xcor() < -230:
            enemy_direction *= -1

enemy_bullets = []

def create_enemy_bullet():
    enemy_bullet = Turtle("square")
    enemy_bullet.color("red")
    enemy_bullet.shapesize(1, 0.5)
    enemy_bullet.penup()
    enemy_bullet.hideturtle()
    enemy_bullets.append(enemy_bullet)
    return enemy_bullet

def enemy_fire():
    visible_enemies = [enemy for enemy in enemy_list if enemy.isvisible()]
    if visible_enemies:
        enemy_shooter = rnd.choice(visible_enemies)
        bullet_enemy = create_enemy_bullet()
        bullet_enemy.goto(enemy_shooter.xcor(), enemy_shooter.ycor() - 20)
        bullet_enemy.showturtle()

score = 0
def setup_scoreboard():
    global score_display
    score_display = Turtle()
    score_display.hideturtle()
    score_display.color("white")
    score_display.penup()
    score_display.goto(-220, 220)
    score_display.write(f"Score: 0", font=("Arial", 14, "normal"))

    return score_display

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

def game_over(message):
    global is_game_on
    is_game_on = False
    display = Turtle()
    display.hideturtle()
    display.color("yellow" if message == "YOU WIN!" else "red")
    display.write(message, align="center", font=("Arial", 24, "bold"))

screen = setup_window()
player = setup_player()
projectile_bullet = create_bullet()
create_enemy()
score_display = setup_scoreboard()

screen.listen()
screen.onkey(player_move_right, "Right")
screen.onkey(player_move_left, "Left")
screen.onkey(fire_bullet, "space")


is_game_on = True
last_shot_time = time.time()

while is_game_on:
    screen.update()
    enemy_movement()

    #PLAYER BULLET OUT OF BOUNDS
    if projectile_bullet.isvisible():
        projectile_bullet.sety(projectile_bullet.ycor() + BULLET_SPEED)
        if projectile_bullet.ycor() > 250:
             projectile_bullet.hideturtle()

    #ENEMY BULLET COLLISION
    for bullet in enemy_bullets:
        if bullet.isvisible():
            bullet.sety(bullet.ycor() - BULLET_SPEED)
            if bullet.ycor() < -250:
                bullet.hideturtle()
            if bullet.distance(player) < 20:
                bullet.hideturtle()
                player.hideturtle()
                game_over("GAME OVER")

    if int(time.time() - last_shot_time) > 1:
        enemy_fire()
        last_shot_time = time.time()

    #PLAYER BULLET COLLISION
    bullet_collision()

    if all(not enemy.isvisible() for enemy in enemy_list):
        game_over("YOU WIN!")



screen.exitonclick()