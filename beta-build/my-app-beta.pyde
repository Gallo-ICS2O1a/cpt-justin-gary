# Rename this file to include the name of your application
# Replace this code with your application's code
x = 250
y = 250
w = 50
h = 50
speedX = 5
speedY = 4
paddleW = 30
paddleH = 100
paddleS = 10
keyStatesL = []
keyStatesR = []
screen = 3
contSize = 40
score1, score2 = 0, 0
playSize = 30
htpSize = 30
backSize = 20
textY = 100
textS = 2
colour1 = color(0, 0, 0)
colour2 = color(0, 0, 0)
timeAccessed = None
for i in range(233):
    keyStatesR.append(False)
paddleR = PVector(485, 250)

for i in range(233):
    keyStatesL.append(False)
paddleL = PVector(15, 250)


def setup():
    size(500, 500)
    rectMode(CENTER)
    ellipseMode(CENTER)
    textMode(CENTER)


def draw():
    global keyStatesR
    global screen
    global htpSize
    global playSize

    if screen == 1:
        if keyStatesR[38]:  # up
            paddleR.y -= 5
        elif keyStatesR[40]:  # down
            paddleR.y += 5

        if keyStatesL[87]:
            paddleL.y -= 5
        elif keyStatesL[83]:
            paddleL.y += 5

        background(0)

        drawBall()
        drawPaddle()
        moveBall()
        bounceDirection()
        restrictPaddle()
        contactPaddle()
        drawScore()

def drawScore():
    textMode(CENTER)
    textSize(40)
    fill(255)
    text(score1, 150, 50)
    text(score2, 320, 50)


def drawBall():
    fill(255, 0, 0)
    ellipse(x, y, w, h)


def moveBall():
    global x
    global y

    x += speedX
    y += speedY


def bounceDirection():
    global speedX
    global speedY

    if x > width - w / 2:
        speedX = -speedX
    elif x < 0 + w / 2:
        speedX = -speedX

    if y > height - h / 2:
        speedY = -speedY
    elif y < 0 + h / 2:
        speedY = -speedY


def drawPaddle():
    fill(255, 238, 0)
    rect(paddleR.x, paddleR.y, paddleW, paddleH)

    fill(21, 255, 0)
    rect(paddleL.x, paddleL.y, paddleW, paddleH)


def restrictPaddle():
    global paddleS
    if paddleR.y - paddleH / 2 < 0:
        paddleR.y += 5
    if paddleR.y + paddleH / 2 > height:
        paddleR.y -= 5

    if paddleL.y - paddleH / 2 < 0:
        paddleL.y = paddleL.y + paddleS
    if paddleL.y + paddleH / 2 > height:
        paddleL.y = paddleL.y - paddleS


def contactPaddle():
    global speedX
    global screen
    global x
    global y
    global score1
    global score2

    # left paddle
    if x == 50 and y < paddleL.y + 70 and y > paddleL.y - 70:
        if speedX < 0:
            speedX = -speedX

    if x <= 25:
        screen = 4
        score2 += 1
        x = 250
        y = 250
        paddleL.y = 250
        paddleR.y = 250

    # right paddle
    if x == 450 and y < paddleR.y + 70 and y > paddleR.y - 70:
        if speedX > 0:
            speedX = -speedX

    if x >= 475:
        screen = 4
        score1 += 1
        x = 250
        y = 250
        paddleL.y = 250
        paddleR.y = 250


def keyPressed():
    global keyStatesR
    global keyStatesL
    keyStatesR[keyCode] = True
    keyStatesL[keyCode] = True


def keyReleased():
    global keyStatesR
    global keyStatesL
    keyStatesR[keyCode] = False
    keyStatesL[keyCode] = False
