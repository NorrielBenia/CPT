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
def setup():
    size(500,700)

def mouseClicked():
    #For play button
    global  button_x1, button_y1, button_width1, button_length1, button_x2, button_y2, button_width2, button_length2, screen, button_x3, button_y3, button_width3, button_length3
    if (mouseX > button_x1 and mouseX < button_x1+button_width1 and
        mouseY > button_y1 and mouseY < button_y1+button_length1):
        screen = 1
    #For How to Play button
    elif (mouseX > button_x2 and mouseX < button_x2+button_width2 and
        mouseY > button_y2 and mouseY < button_y2+button_length2):
        screen = 2
        
def keyPressed():
    global screen
    if screen == 1:
        if key == 'b':
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

def draw():
    global button_hover, button_x1, button_y1, button_width1, button_length1, button_x2, button_y2, button_width2, button_length2, screen, button_x3, button_y3, button_width3, button_length3
    
    if screen == 0:
        background(0)
        fill(button_normal)
        
        #Play button
        noStroke()
        if (mouseX > button_x1 and mouseX < button_x1+button_width1 and
        mouseY > button_y1 and mouseY < button_y1+button_length1):
            fill(button_hover)

        else:
            fill(button_normal)
        
        rect(button_x1,button_y1,button_width1,button_length1)
        fill(0)
        textSize(50)
        text("PLAY",190,370)
    
        #How to Play button
        noStroke()
        if (mouseX > button_x2 and mouseX < button_x2+button_width2 and
        mouseY > button_y2 and mouseY < button_y2+button_length2):
            fill(button_hover)

        else:
            fill(button_normal)
        
        rect(button_x2, button_y2 , button_width2 , button_length2)
        fill(0)
        textSize(24)
        text("How to Play", 182,535)
        
    if screen == 1:
        background(0)
        fill(155)
        textSize(14)
        text("press b to go back to main menu",250,690)

#instruction screen
    if screen == 2:
        background(0)
        fill(155)
        textSize(14)
        text("press b to go back to main menu",250,690)
    if screen == 3:
        background(155)
        fill(0)
        textSize(85)
        text("""           Game Over
             You Died""", -267, 180)
        textSize(20)
        text("press b to go back to main menu",CENTER+93,650)
        text("press r to play again", CENTER+155, 680)
