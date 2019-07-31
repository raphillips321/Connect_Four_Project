def setup():

    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5
    size(601,500)

    y = 150
    
    column_0 = 0
    column_1 = 0
    column_2 = 0
    column_3 = 0
    column_4 = 0
    column_5 = 0
     
    

    
def draw():
    global   y,x , width, speedX , column_0 , column_1 , column_2 , column_3 , column_4, column_5
    background(0)

    ellipse(mouseX ,100, 50, 50)
    y = 150
    while y < 500:
        x = 0
        while x < 600:
            if x % 200 == 0:
            
                stroke(0)
                rect(x,y,100,90)
  
            else: 
            
                stroke(0)
                rect(x,y,100,90)
            x = x + 100
        y = y + 50
    i = 0
    while i < column_0 :
        Y = 475 - 50 * (i)
        ellipse(50, Y, 50, 50)
        i = i + 1
    i = 0
    while i < column_1 :
        Y = 475 - 50 * (i)
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

    
    global column_0, column_1 , column_2 , column_3 , column_4, column_5
    if mouseX < 100 :
        Y = 475 - 50 * column_0 
        fill(255)
        ellipse(50, Y, 50, 50)
        if column_0 <= 6: 
            column_0 = column_0 + 1 
        print(column_0)
    if mouseX >= 101 and mouseX <=200:
        Y = 475 - 50 * column_1
        fill(255)
        ellipse(150, Y, 50, 50)
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
