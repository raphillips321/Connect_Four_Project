def setup():

    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5, Player_1 ,Player_2
    size(601,500)

    y = 150

    column_0 = []
    column_1 = []
    column_2 = []
    column_3 = []
    column_4 = []
    column_5 = []
    GameOver = False


    Player_1 = True
    Player_2 = False
    
    Player_1_counter = 0
    Player_2_counter = 0



def draw():
    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5, Player_1, Player_2
    background(0)
    textSize(20)
    fill(255,0,0)
    text("Player 1 ",10 , 30)
    fill(5,13,255)
    text("Player 2 " ,500 ,30)



    if Player_1 is True:
        fill(0, 0, 255)
    else: fill(255, 0, 0)
    ellipse(mouseX ,100, 50, 50)
    
    
    
    y = 150
    while y < 500:
        x = 0
        while x < 600:
            if x % 200 == 0:
                fill(0)
                stroke(255)
                rect(x,y,100,90)

            else:
                fill(0)
                stroke(255)
                rect(x,y,100,90)
            x = x + 100
        y = y + 50
    i = 0
    while i < len(column_0):
        Y = 475 - 50 * (i)
        if column_0[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0, 0)
        ellipse(50, Y, 50, 50)
        i = i + 1
    i = 0
    while i < len(column_1):
        Y = 475 - 50 * (i)
        if column_1[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0, 0)
        ellipse(150, Y, 50, 50)
        i = i + 1
        print(column_1)
    i = 0
    while i < len(column_2):
        Y = 475 - 50 * (i)
        if column_2[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0, 0)
        ellipse(250, Y, 50, 50)
        i = i + 1
        print(column_2)
    i = 0
    while i < len(column_3):
        Y = 475 - 50 * (i)
        if column_3[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0, 0)
        ellipse(350, Y, 50, 50)
        i = i + 1
        print(column_3)
    i = 0
    while i < len(column_4) :
        Y = 475 - 50 * (i)
        if column_4[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0, 0)
        ellipse(450, Y, 50, 50)
        i = i + 1
        print(column_4)
    i = 0
    while i < len(column_5) :
        Y = 475 - 50 * (i)
        if column_5[i] == True:
            fill(0, 0, 255)
        else: fill(255, 0 ,0)
        ellipse(550, Y, 50, 50)
        print(column_5)
        i = i + 1
    



    # i = i + 1

    for c in [column_0, column_1, column_2, column_3, column_4, column_5]:
        if len(c) >= 4 and c[0] == c[1] and c[1] == c[2] and c[2] == c[3]:
        #Winner
            if c[0] == True:
                print("Player 1 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
          
                
                
            else:
                print("PLayer 2 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
            
    
        if len(c) >= 5  and c[1] == c[2] and c[2] == c[3] and c[3] == c[4]:
        #Winner
            if c[1] == True:
                print("Player 1 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
                
            else:
                print("PLayer 2 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
    
        if len(c) >= 6 and c[2] == c[3] and c[3] == c[4] and c[4] == c[5]:
        #Winner
            if c[2] == True:
                print("Player  1 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
                
            else:
                print("Player 2 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
            
        if len(c) >= 7 and c[3] == c[4] and c[4] == c[5] and c[5] == c[6]:
        #Winner
            if c[3] == True:
                print("Player  1 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
                
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
            
            else:
                print("Player 2 won")
                print("GameOver")
                GameOver = True
                
                fill(0)
                stroke(0)
                ellipse(mouseX ,100, 50, 50)
            
                img = loadImage("game.png")
                image(img ,180,0,250,150)
                
                
      
                
                















def mouseClicked():
    global Player_1




    global y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5, Player_1 ,Player_2, Player_1_counter,Player_2_counter
    if mouseX < 100 :

        Y = 475 - 50 * len(column_0)
        ellipse(50, Y, 50, 50)
        if len(column_0) <= 6:
            column_0.append(Player_1)
            Player_1 = not Player_1
        print(column_0)
    if mouseX >= 101 and mouseX <=200:

        Y = 475 - 50 * len(column_1)
        ellipse(150, Y, 50, 50)
        if len(column_1) <= 6:
            column_1.append(Player_1)
            Player_1 = not Player_1
        if column_1 <= 6:
            column_1 = column_1 + 1
        print(column_1)
    if mouseX >=201 and mouseX <= 300:

        Y = 475 - 50 * len(column_2)
        ellipse(250, Y, 50, 50)
        if len(column_2) <= 6:
            column_2.append(Player_1)
            Player_1 = not Player_1
        print(column_2)
    if mouseX > 301 and mouseX <= 400:

        Y = 475 - 50 * len(column_3)
        ellipse(350, Y, 50, 50)
        if len(column_3) <= 6:
            column_3.append(Player_1)
            Player_1 = not Player_1
        print(column_3)
    if mouseX > 401 and mouseX <= 500:
        Y = 475 - 50 * len(column_4)
        ellipse(450, Y, 50, 50)
        if len(column_4) <= 6:
            column_4.append(Player_1)
            Player_1 = not Player_1
        print(column_4)
    if mouseX > 501 and mouseX <= 600:
        Y = 475 - 50 * len(column_5)
        ellipse(550, Y, 50, 50)
        if len(column_5) <= 6:
            column_5.append(Player_1)
            Player_1 = not Player_1
        print
