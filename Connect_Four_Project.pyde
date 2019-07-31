def setup():

    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5, Player_1
    size(601,500)

    y = 150
    
    column_0 = []
    column_1 = []
    column_2 = 0
    column_3 = 0
    column_4 = 0
    column_5 = 0
    
    Player_1 = True

    
def draw():
    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5, Player_1
    background(0)
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
    while i < column_2 :
        Y = 475 - 50 * (i)
        ellipse(250, Y, 50, 50)
        i = i + 1 
        print(column_2)  
    i = 0   
    while i < column_3 :
        Y = 475 - 50 * (i)
        ellipse(350, Y, 50, 50)
        i = i + 1 
        print(column_3) 
    i = 0   
    while i < column_4 :
        Y = 475 - 50 * (i)
        ellipse(450, Y, 50, 50)
        i = i + 1 
        print(column_4)  
    i = 0   
    while i < column_5 :
        Y = 475 - 50 * (i)
        ellipse(550, Y, 50, 50)
        i = i + 1 
        print(column_5)  
    i = 0   
 
 
 
 

        

        
def mouseClicked():
    global Player_1

        


    global column_0, column_1 , column_2 , column_3 , column_4, column_5
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
        Y = 475 - 50 * column_2
        ellipse(250, Y, 50, 50)
        if column_2 <= 6: 
            column_2 = column_2 + 1
        print(column_2)
    if mouseX > 301 and mouseX <= 400:
        Y = 475 - 50 * column_3
        ellipse(350, Y, 50, 50)
        if column_3 <= 6: 
            column_3 = column_3 + 1
        print(column_3)
    if mouseX > 401 and mouseX <= 500:
        Y = 475 - 50 * column_4
        ellipse(450, Y, 50, 50)
        if column_4 <= 6: 
            column_4= column_4 + 1
        print(column_4)
    if mouseX > 501 and mouseX <= 600:
        Y = 475 - 50 * column_5
        ellipse(550, Y, 50, 50)
        if column_5 <= 6: 
            column_5 = column_5 + 1
        print(column_5)
