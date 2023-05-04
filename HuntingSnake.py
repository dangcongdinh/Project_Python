import pygame as pg
import random

pg.init()
WIDTH = 800
HEIGHT = 600

bg = (3, 252, 240)

black = (0,0,0)
white = (255,255,255)
pink = (237, 135, 128)
yellow = (235, 202, 16)
blue = (7, 11, 247)
puple = (25, 1, 59)
orange = (255, 86, 8)
green = (34,199,56)


font = pg.font.SysFont(None,50)
font_1 = pg.font.SysFont(None,100)
start_game = True

screen = pg.display.set_mode((WIDTH,HEIGHT))
icon = pg.image.load(r"image\icon_snake.png")
pg.display.set_icon(icon)
pg.display.set_caption("Hunting Snake")

speed = 15
check_level = "easy"
check_snake_color = 1
check_food_color = 5
score_font = pg.font.SysFont("comicsansms", 35)

snake_color = green
food_color = black

flag = 0
flag_move = -1
font = pg.font.SysFont(None,50)
font_message = pg.font.SysFont('couriernew',31)

def message(msg):
    mes = font_message.render(msg,True,(255,0,0))
    screen.blit(mes,[WIDTH*(1/10),HEIGHT*(1/3)])
def score_of_game(score):
    string = score_font.render("Your score: "+str(score),True,(247, 143, 7))
    screen.blit(string,[10,0])
def create_snake(snake_size,pos_list):
    for pos in pos_list:
        pg.draw.rect(screen,snake_color,[pos[0],pos[1],snake_size,snake_size])

def run_game():
    global speed,start_game,food_color,flag_move
    clock = pg.time.Clock()

    x_snake=300
    y_snake=300

    x_change = 0
    y_change =0

    snake_size = 10

    x_food = round(random.randrange(0,WIDTH - snake_size)/10)*10
    y_food = round(random.randrange(0,HEIGHT - snake_size)/10)*10

    pos_list =[]
    len_snake = 1

    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(bg)
            score_of_game(len_snake - 1)
            message("Press Space to return Main Display")
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        running = False
                        game_over = False
                        start_game = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if flag_move == 1:
                        x_change = snake_size
                        y_change =0
                    else:
                        x_change = -snake_size
                        y_change =0
                        flag_move = 0
                elif event.key == pg.K_RIGHT:
                    if flag_move == 0:
                        x_change = -snake_size
                        y_change =0
                    else:
                        x_change = snake_size
                        y_change =0
                        flag_move = 1
                elif event.key == pg.K_UP:
                    if flag_move == 3:
                        x_change = 0
                        y_change = snake_size
                    else:
                        x_change = 0
                        y_change = -snake_size
                        flag_move = 2
                     
                elif event.key == pg.K_DOWN:
                    if flag_move == 2:
                        x_change = 0
                        y_change = -snake_size
                    else:
                        x_change = 0
                        y_change = snake_size
                        flag_move = 3
        screen.fill(bg)

        x_snake += x_change
        y_snake += y_change

        pg.draw.rect(screen,food_color,[x_food,y_food,snake_size,snake_size])
        head_snake = []
        head_snake.append(x_snake)
        head_snake.append(y_snake)
        pos_list.append(head_snake)
        create_snake(snake_size,pos_list)

        if len(pos_list) > len_snake:
            del pos_list[0]
        if x_snake >= WIDTH or x_snake <0 or y_snake <0 or y_snake >=HEIGHT:
            game_over = True
        
        for pos in pos_list[:-1]:
            if pos == head_snake:
                game_over = True
        score_of_game(len_snake - 1)
        pg.display.update()
        if x_snake == x_food and y_snake == y_food:
            x_food = round(random.randrange(0,WIDTH - snake_size)/10)*10
            y_food = round(random.randrange(0,HEIGHT - snake_size)/10)*10
            len_snake +=1
        clock.tick(speed)
    pg.display.update()
    display()

def display():

    global flag,start_game

    def align_center_block(btn,lbl):
        return (btn.x + btn.width/2 - lbl.get_width()/2, btn.y + btn.height/2 - lbl.get_height()/2)

    def draw_tick_level(check):
        icon_tick = pg.image.load(r"C:\Users\Administrator\Documents\PYTHON\Project_HuntingSnake\image\tick.png")
        icon_tick = pg.transform.scale(icon_tick,(30,30))
        if check == "easy":
            screen.blit(icon_tick,(525,190))
        if check == "medium":
            screen.blit(icon_tick,(525,260))
        if check == "hard":
            screen.blit(icon_tick,(525,330))

    def draw_tick_snake_color(check):
        icon_tick = pg.image.load(r"C:\Users\Administrator\Documents\PYTHON\Project_HuntingSnake\image\tick.png")
        icon_tick = pg.transform.scale(icon_tick,(20,20))
        if check == 1:
            screen.blit(icon_tick,(390,220))
        if check == 2:
            screen.blit(icon_tick,(490,220))
        if check == 3:
            screen.blit(icon_tick,(590,220))
        if check == 4:
            screen.blit(icon_tick,(690,220))

    def draw_tick_food_color(check):
        icon_tick = pg.image.load(r"C:\Users\Administrator\Documents\PYTHON\Project_HuntingSnake\image\tick.png")
        icon_tick = pg.transform.scale(icon_tick,(20,20))
        if check == 5:
            screen.blit(icon_tick,(390,320))
        if check == 6:
            screen.blit(icon_tick,(490,320))
        if check == 7:
            screen.blit(icon_tick,(590,320))
        if check == 8:
            screen.blit(icon_tick,(690,320))

    def main_display():
        global flag,start_game
        screen.fill(bg)
        btn_start = pg.Rect(300,180,200,50)
        label_btn_start = font.render("Start Game",True,white)

        btn_level = pg.Rect(300,250,200,50)
        label_btn_level = font.render("Level",True,white)

        btn_setting = pg.Rect(300,320,200,50)
        label_btn_setting = font.render("Setting",True,white)
        screen.fill(bg)

        pg.draw.rect(screen,(255,0,0),btn_start)
        screen.blit(label_btn_start,align_center_block(btn_start,label_btn_start))
        pg.draw.rect(screen,(255,0,0),btn_level)
        screen.blit(label_btn_level,align_center_block(btn_level,label_btn_level))
        pg.draw.rect(screen,(255,0,0),btn_setting)
        screen.blit(label_btn_setting,align_center_block(btn_setting,label_btn_setting))
        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if btn_start.collidepoint(event.pos):
                    start_game = False
                    run_game()
                if btn_level.collidepoint(event.pos):
                    flag = 1
                if btn_setting.collidepoint(event.pos):
                    flag = 2

    def level_display():
        screen.fill(bg)
        global speed,check_level,flag

        btn_easy = pg.Rect(300,180,200,50)
        label_btn_easy = font.render("Easy",True,white)  

        btn_medium = pg.Rect(300,250,200,50)
        label_btn_medium = font.render("Medium",True,white)

        btn_hard = pg.Rect(300,320,200,50)
        label_btn_hard = font.render("Hard",True,white)

        pg.draw.rect(screen,(255,0,0),btn_easy)
        screen.blit(label_btn_easy,align_center_block(btn_easy,label_btn_easy))
        pg.draw.rect(screen,(255,0,0),btn_medium)
        screen.blit(label_btn_medium,align_center_block(btn_medium,label_btn_medium))
        pg.draw.rect(screen,(255,0,0),btn_hard)
        screen.blit(label_btn_hard,align_center_block(btn_hard,label_btn_hard))

        btn_level = pg.Rect(300,80,200,50)
        label_btn_level = font_1.render("LEVEL",True,(23, 138, 150))
        pg.draw.rect(screen,bg,btn_level)
        screen.blit(label_btn_level,align_center_block(btn_level,label_btn_level))
        
        contain_icon_back = pg.Rect(10,540,60,60)
        pg.draw.rect(screen,bg,contain_icon_back)
        icon_back = pg.image.load(r"C:\Users\Administrator\Documents\PYTHON\Project_HuntingSnake\image\icon_back.png")
        icon_back = pg.transform.scale(icon_back,(60,60)) 
        screen.blit(icon_back,(10,540))
        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if contain_icon_back.collidepoint(event.pos):
                    flag = 0
                if btn_easy.collidepoint(event.pos):
                    check_level = "easy"
                    speed = 15
                if btn_medium.collidepoint(event.pos):
                    check_level = "medium"
                    speed = 22
                if btn_hard.collidepoint(event.pos):
                    check_level = "hard"
                    speed = 30
                
        draw_tick_level(check_level)
        pg.display.update()

    def setting_display():
        screen.fill(bg)
        global flag,check_snake_color,check_food_color,snake_color,food_color
        
        font = pg.font.SysFont(None,40)

        btn_setting = pg.Rect(300,80,200,50)
        label_btn_setting = font_1.render("SETTING",True,(23, 138, 150))
        pg.draw.rect(screen,bg,btn_setting)
        screen.blit(label_btn_setting,align_center_block(btn_setting,label_btn_setting))

        btn_snake_color = pg.Rect(110,210,180,40)
        label_snake_color = font.render("Snake Color",True,(255,255,255))
        pg.draw.rect(screen,(255,0,0),btn_snake_color)
        screen.blit(label_snake_color,align_center_block(btn_snake_color,label_snake_color))

        btn_food_color = pg.Rect(110,310,180,40)
        label_food_color = font.render("Food Color",True,(255,255,255))
        pg.draw.rect(screen,(255,0,0),btn_food_color)
        screen.blit(label_food_color,align_center_block(btn_food_color,label_food_color))

        color1 = pg.Rect(350,220,20,20)
        pg.draw.rect(screen,green,color1)
        color2 = pg.Rect(450,220,20,20)
        pg.draw.rect(screen,yellow,color2)
        color3 = pg.Rect(550,220,20,20)
        pg.draw.rect(screen,pink,color3)
        color4 = pg.Rect(650,220,20,20)
        pg.draw.rect(screen,puple,color4)

        color5 = pg.Rect(350,320,20,20)
        pg.draw.rect(screen,black,color5)
        color6 = pg.Rect(450,320,20,20)
        pg.draw.rect(screen,white,color6)
        color7 = pg.Rect(550,320,20,20)
        pg.draw.rect(screen,blue,color7)
        color8 = pg.Rect(650,320,20,20)
        pg.draw.rect(screen,orange,color8)

        contain_icon_back = pg.Rect(10,540,60,60)
        pg.draw.rect(screen,bg,contain_icon_back)
        icon_back = pg.image.load(r"C:\Users\Administrator\Documents\PYTHON\Project_HuntingSnake\image\icon_back.png")
        icon_back = pg.transform.scale(icon_back,(60,60)) 
        screen.blit(icon_back,(10,540))

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if contain_icon_back.collidepoint(event.pos):
                    flag = 0
                if color1.collidepoint(event.pos):
                    check_snake_color = 1
                    snake_color = green
                if color2.collidepoint(event.pos):
                    check_snake_color = 2
                    snake_color = yellow
                if color3.collidepoint(event.pos):
                    check_snake_color = 3
                    snake_color = pink
                if color4.collidepoint(event.pos):
                    check_snake_color = 4
                    snake_color = puple  
                if color5.collidepoint(event.pos):
                    check_food_color = 5
                    food_color = black
                if color6.collidepoint(event.pos):
                    check_food_color = 6
                    food_color = white
                if color7.collidepoint(event.pos):
                    check_food_color = 7
                    food_color = blue
                if color8.collidepoint(event.pos):
                    check_food_color = 8
                    food_color = orange   
        draw_tick_snake_color(check_snake_color)
        draw_tick_food_color(check_food_color)
        pg.display.update()


    while start_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                start_game = False
        if flag == 0:
            main_display()
        if flag == 1:
            level_display() 
        if flag == 2:
            setting_display() 
        pg.display.update()
display()