import random
screen = 0

button_normal = 255
button_hover = 200

button_x1 = 125
button_y1 = 300
button_width1 = 250
button_length1 = 100

button_x2 = 147
button_y2 = 500
button_width2 = 200
button_length2 = 50

button_x3 = 125
button_y3 = 300
button_width3 = 250
button_length3 = 100

button_x4 = 450
button_y4 = 5
button_width4 = 40
button_length4 = 50

wall_x1 = random.randint(100, 501)
wall_x2 = wall_x1 - 600
wall_x3 = random.randint(100, 501)
wall_x4 = wall_x3 - 600
wall_length = 500
wall_thickness = 20
wall_y = -55
wall_y2 = -375

score = 0

xCharacter = 0
yCharacter = 0
keys_pressed = [False for key_code in range(256)]


def setup():
    size(500, 700)


def mouseClicked():

    global button_x1, button_y1, button_width1
    global button_length1, button_x2, button_y2, button_width2, button_length2
    global screen, button_x3, button_y3, button_width3, button_length3
    global button_x4, button_y4, button_width4, button_length4, screen

    # For play button
    if (mouseX > button_x1 and mouseX < button_x1+button_width1 and
        mouseY > button_y1 and mouseY < button_y1+button_length1):
        screen = 1

    # For How to Play button
    elif (mouseX > button_x2 and mouseX < button_x2+button_width2 and
          mouseY > button_y2 and mouseY < button_y2+button_length2):
        screen = 2

    # For Pause button
    if (mouseX > button_x4 and mouseX < button_x4 + button_width4 and
        mouseY > button_y4 and mouseY < button_y4 + button_length4):
        screen = 4


def keyPressed():
    global screen
    global keys_pressed
    if screen == 1:
        if key == 'b':
            xCharacter = 0
            yCharacter = 0
            screen = 0
        if key == 't':
            screen = 3
    elif screen == 2:
        if key == 'b':
            screen = 0
    elif screen == 3:
        if key == 'r':
            screen = 1
        elif key == 'b':
            screen = 0
    elif screen == 4:
        if key == 'h':
            screen = 1

    keys_pressed[keyCode] = True


def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False


def main_screen():
    global button_hover, button_x1, button_y1, button_width1, button_length1
    global button_x2, button_y2, button_width2, button_length2, screen
    global button_x3, button_y3, button_width3, button_length3, wall_down

    background(0)
    fill(button_normal)

    # Play button
    noStroke()
    if (mouseX > button_x1 and mouseX < button_x1+button_width1 and
        mouseY > button_y1 and mouseY < button_y1+button_length1):
            fill(button_hover)

    else:
        fill(button_normal)

    rect(button_x1, button_y1, button_width1, button_length1)
    fill(0)
    textSize(50)
    text("PLAY", 190, 370)

    # How to Play button
    noStroke()
    if (mouseX > button_x2 and mouseX < button_x2+button_width2 and
        mouseY > button_y2 and mouseY < button_y2+button_length2):
            fill(button_hover)

    else:
        fill(button_normal)

    rect(button_x2, button_y2, button_width2, button_length2)
    fill(0)
    textSize(24)
    text("How to Play", 182, 535)

    # Title
    fill('#c7003c')
    rect(00, 20, 200, 20)
    rect(300, 20, 200, 20)
    rect(400, 100, 300, 20)
    rect(00, 100, 300, 20)
    rect(00, 200, 200, 20)
    rect(300, 200, 200, 20)

    fill(255)
    textSize(50)
    text("Slidey The SnowMan", 0, 170)


def Play_screen():
    global button_hover, button_x1, button_y1, button_width1, button_length1
    global button_x2, button_y2, button_width2, button_length2, button_x3
    global button_y3, button_width3, button_length3, screen, wall_x1, wall_x2
    global wall_x3, wall_x4, wall_y, wall_y2, score, xCharacter, yCharacter
    global wall_length, wall_thickness

    background(0)
    fill(155)
    textSize(14)
    text("press b to go back to main menu", 250, 690)
    
    # Spikes
    fill("#d1dede")
    triangle(xCharacter + 165, 670, xCharacter + 187, 590, xCharacter + 211,
             670)
    triangle(xCharacter + 190, 670, xCharacter + 215, 590, xCharacter + 236,
             670)
    triangle(xCharacter + 215, 670, xCharacter + 242, 590, xCharacter + 261,
             670)
    triangle(xCharacter + 240, 670, xCharacter + 270, 590, xCharacter + 286,
             670)
    triangle(xCharacter + 265, 670, xCharacter + 295, 590, xCharacter + 315,
             670)
    triangle(xCharacter + 290, 670, xCharacter + 323, 590, xCharacter + 340,
             670)

    # MOVEMTN AND KEYS
    if keys_pressed[38]:
        yCharacter -= 4
    if keys_pressed[37]:
        xCharacter -= 10
    if keys_pressed[40]:
        yCharacter += 7.5
    if keys_pressed[39]:
        xCharacter += 10

    if yCharacter >= 208:
        screen = 3
        yCharacter = 0
        xCharacter = 0
        wall_y = -55
        wall_y2 = -375
        score = 0

    if xCharacter <= -296:
        xCharacter = 295
    elif xCharacter >= 294:
        xCharacter = -295

    # BODY
    body = yCharacter + 350
    noStroke()
    fill(255)
    ellipse(xCharacter + 250, body, 80, 80)

    # FEATURES
    fill(0)
    ellipse(xCharacter + 230.58, yCharacter + 340.1, 20, 20)
    ellipse(xCharacter + 270.25, yCharacter + 340.1, 20, 20)

    fill("#FF8103")
    rect(xCharacter + 250.43, yCharacter + 350.95, 60, 13)

    # Wall
    fill("#c7003c")
    rect(wall_x1, wall_y, wall_length, wall_thickness)
    rect(wall_x2, wall_y, wall_length, wall_thickness)
    rect(wall_x3, wall_y2, wall_length, wall_thickness)
    rect(wall_x4, wall_y2, wall_length, wall_thickness)
    if wall_y >= 700:
        wall_y = 0
        wall_x1 = random.randint(100, 501)
        wall_x2 = wall_x1 - 600
    if wall_y2 >= 700:
        wall_y2 = 0
        wall_x3 = random.randint(100, 501)
        wall_x4 = wall_x3 - 600

    wall_y += 3
    wall_y2 += 3

    if (body > wall_y and body <= wall_y + wall_thickness and
    xCharacter + 60 >= wall_x1 - 250):
            yCharacter = 1000
    elif (body > wall_y and body <= wall_y + wall_thickness and
    xCharacter + 20 <= wall_x2 + 250):
            yCharacter = 1000
    elif (body > wall_y2 and body <= wall_y2 + wall_thickness and
    xCharacter + 60 >= wall_x3 - 250):
            yCharacter = 1000
    elif (body > wall_y2 and body <= wall_y2 + wall_thickness and
    xCharacter + 20 <= wall_x4 + 250):
            yCharacter = 1000
    # pause
    fill(255)
    rect(button_x4, button_y4, button_width4, button_length4)
    fill(0)
    rect(459, 13, 7, 35)
    rect(475, 13, 7, 35)

    print(body)

    # score
    score += 1
    fill(140, 225, 80)
    textSize(40)
    text(score, 0, 50)


def instruction_screen():
    background(0)
    fill(155)
    textSize(14)
    text("press b to go back to main menu", 250, 690)
    
    #Written instructions
    textSize(40)
    text("How to Play", CENTER + 135, 45)
    textSize(30)
    text("PROTECT HIS CARROT", CENTER + 90, 110)
    fill("#c7003c")
    rect(50, 185, 125, 20)
    fill(155)
    textSize(20)
    text(""" These are walls, if the touch
     your carrot you will die""", 195, 188)
    text("""These are spikes. They follow
          your every move. If
      touched, you will ... DIE""", 195, 290)
    noStroke()
    fill("#d1dede")
    triangle(65, 350, 87, 270, 111, 350)
    triangle(90, 350, 115, 270, 136, 350)
    triangle(95+20, 350, 120+22, 270, 141+20, 350)

    # movement keys
    text("UP", CENTER+225, 400)
    text("DOWN", 210, 615)
    text("LEFT", 50, 550)
    text("RIGHT", 380, 550)
    rect(200, 415, 80, 80)
    rect(200, 505, 80, 80)
    rect(110, 505, 80, 80)
    rect(290, 505, 80, 80)
    fill(100)
    
    # Spikes
    triangle(213, 486, 241, 430, 269, 486)
    triangle(213, 515, 241, 571, 269, 515)
    triangle(121, 540, 177, 571, 177, 515)
    triangle(357, 540, 301, 571, 301, 515)


def Death_screen():
    background(155)
    fill(0)
    textSize(85)
    text("""           Game Over
            You Died""", -267, 145)
    textSize(20)
    text("press b to go back to main menu", CENTER + 93, 650)
    text("press r to play again", CENTER + 155, 680)

    noStroke()
    fill(255, 0, 0)
    ellipse(260, 450, 250, 250)

    # FEATURES
    fill(0)
    rect(220.58, 370.1, 40, 40)
    rect(280.25, 370.1, 40, 40)

    fill("#FF8103")
    rect(260.43, 390.95, 160, 35)


def pause_screen():
    fill(0)
    background(255)
    textSize(50)
    text("PAUSED", 160, 370)
    textSize(14)
    text("press h to resume", 270, 670)


def draw():
    global screen

    if screen == 0:
        main_screen()
    elif screen == 1:
        Play_screen()
    elif screen == 2:
        instruction_screen()
    elif screen == 3:
        Death_screen()
    elif screen == 4:
        pause_screen()
