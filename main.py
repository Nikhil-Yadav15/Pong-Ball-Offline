import pygame
import random
import time
main_loop = True
timer = 5
main_screen, run_game, help = True, False, False
level_define, level = 1, 0
screen_width, screen_height = 900, 600
heightObject, widthObject = 80, 25
xPlayer, yPlayer = 10, screen_height/2
xComp, yComp = screen_width-40, screen_height/2
xBall, yBall = screen_width/2 - 10, screen_height/2
vel, score = 5, 0
stop_attack, check_lose = True, True
stop_attack_list = [False, True, True, False, False,True, False, True, True]
global velBall
velBall = 3

velBall_list = [velBall, velBall - 2*velBall, velBall - 2*velBall, velBall - 2*velBall]
global began_motion, began_motion
began_motion = True
moveBall = False
class Player():
    def __init__(self, win, x, y):
        pygame.draw.rect(win, (150, 0, 255), (x,y, widthObject, heightObject))

class Comp():
    def __init__(self, win, x, y):
        pygame.draw.rect(win, (150, 0, 255), (x,y, widthObject, heightObject))

class Ball():
    def __init__(self, win, x, y):
        pygame.draw.circle(win, (243, 2, 21), (x,y), 20)

pygame.init()
font = pygame.font.SysFont("Arial.tff", 45, False, True)

class mn_images():
    def __init__(self, win):
        bg_img = pygame.image.load('mn_scrbg.jpg')
        bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
        win.blit(bg_img, (0,0))

class button():
    def __init__(self, win, pos):
        button = pygame.image.load('button_.png')
        button = pygame.transform.scale(button, (300, 150))
        win.blit(button, (screen_width- 800, screen_height- 400))
        win.blit(button, (screen_width - 400, screen_height-400))
        mn_font = pygame.font.SysFont("snapitc.tff", 50)
        text1 = mn_font.render("Play", True, (200, 0, 100))
        text2 = mn_font.render("Help", True, (200, 0, 100))
        win.blit(text1, (screen_width- 700, screen_height- 350))
        win.blit(text2, (screen_width - 300, screen_height- 350))
help_font = pygame.font.SysFont("snapitc.tff", 50)
help_text_font = pygame.font.SysFont('snapitic.tff', 40)
class Help():
    def __init__(self, win):
        bg_img = pygame.image.load('mn_scrbg.jpg')
        bg_img = pygame.transform.scale(bg_img,(screen_width, screen_height))
        win.blit(bg_img, (0,0))
    def inst(self, win):
        round = pygame.image.load('rect.png')
        round = pygame.transform.scale(round, (int(screen_width/2)+ 400, int(screen_height/2)+ 100))
        win.blit(round, (screen_width/2- 420, screen_height/2- 250))
        text = help_text_font.render("It is a single player game", True, (200, 200, 10))
        win.blit(text, (screen_width/2- 190, screen_height/2- 180))
        text1 = help_text_font.render("You can control it by UP & DOWN arrow", True, (200, 200, 10))
        win.blit(text1, (screen_width / 2 - 260, screen_height / 2 - 130))
        text2 = help_text_font.render("As you win, the score will increase as well as the level", True, (200, 200, 10))
        win.blit(text2, (screen_width / 2 - 360, screen_height / 2 - 80))
        text3 = help_text_font.render("and the speed of the ball too", True, (200, 200, 10))
        win.blit(text3, (screen_width / 2 - 200, screen_height / 2- 30))
        text4 = help_text_font.render("If you fail to hit the ball, the game will reset", True, (200, 200, 10))
        win.blit(text4, (screen_width / 2 - 300, screen_height /2 + 20))


    def help_button(self, win):
        but = pygame.image.load("button_.png")
        but = pygame.transform.scale(but, (200, 100))
        win.blit(but, (screen_width/2- 100, screen_height/2 + 150))
        text = help_font.render("Home", True, (200, 0, 100))
        win.blit(text,(screen_width/2- 50, screen_height/2 + 180))


class game():
    def __init__(self):
        super(game, self).__init__()
        global main_screen, run, run_game, timer, lose_text, lose_timer, help, main_loop
        xPlayer, yPlayer = 10, screen_height/2
        self.window = pygame.display.set_mode((screen_width, screen_height))
        ico = pygame.image.load("pong-ball-ico.png")
        pygame.display.set_caption("Pong Ball")
        pygame.display.set_icon(ico)
        run = False
        while main_loop:
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    main_loop = False
            while main_screen:
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        main_loop = False
                        main_screen = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mouse_pos[0] in range(120, 375) and mouse_pos[1] in range(225, 323):
                            main_screen = False
                            run = True
                        elif mouse_pos[0] in range(525, 775) and mouse_pos[1] in range(225, 322):
                            run = False

                            main_screen = False
                            help = True
                mn_images(self.window)
                button(self.window, mouse_pos)
                pygame.display.flip()
            while help:
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        help = False
                        main_loop = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mouse_pos[0] in range(364, 533) and mouse_pos[1] in range(466, 529):

                            main_screen = True
                            help = False


                Help(self.window)
                Help.inst(self, self.window)
                Help.help_button(self, self.window)
                pygame.display.update()
            ###########################################################################################################

            while run:
                global text_timer_text
                text_timer_text = "Match starts in {} sec".format(timer)
                pygame.time.delay(10)
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        run = False
                        main_loop = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mouse_pos[0] in range(11, 106) and mouse_pos[1] in range(17, 49):
                            run_game = False

                            #
                global velBall, vel
                if timer!=0:
                    timer-=1
                    time.sleep(1)
                elif timer<1:
                    run_game = True
                if run_game == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN] and yPlayer < screen_height - (heightObject + 10):
                        yPlayer+= vel
                    if keys[pygame.K_UP] and yPlayer > 10:
                        yPlayer-= vel



                    global began_motion, xBall, yBall, yComp, moveBall, check_lose, score, level_define, level
                    # Player hit ball
                    if xPlayer + 40 >= xBall and xPlayer + 10 <=xBall:
                        if yBall in range(int(yPlayer - 10), int(yPlayer + 80)):
                            xBall_random = velBall
                    if began_motion == True:
                        xBall_random = random.choice(velBall_list)
                        yBall_random = random.choice(velBall_list)
                        pygame.time.delay(100)
                        moveBall = True

                    if moveBall == True:
                        began_motion = False
                        if yBall < screen_height - 20 and yBall > 20:
                            xBall+= xBall_random
                            yBall+= yBall_random
                        else:
                            if yBall_random < 0:
                                yBall_random -= yBall_random * 2

                            elif yBall_random > 0:
                                yBall_random -= yBall_random * 2

                            yBall += yBall_random
                            xBall += xBall_random
                    ##########################################################################
                    if check_lose == True:
                        random_win_lose = random.choice(stop_attack_list)
                        check_lose = False
                    ##########################################################################
                    if xBall > screen_width/2:

                        if stop_attack == random_win_lose:
                            if yBall - 20 > yComp and xBall< screen_width - 30:
                                if yComp + heightObject + 10 <= screen_height:
                                    yComp+= vel
                            elif yBall < yComp:
                                yComp-= vel
                        else:
                            if yBall - 90 > yComp and xBall < screen_width - 30:
                                if yComp + heightObject + 10 <= screen_height:
                                    yComp += vel
                            elif yBall < yComp - 10:
                                yComp -= vel


                        if xBall >= xComp and xBall < xComp+ 30:
                            if yBall in range( int(yComp -2), int(yComp + 80)):
                                xBall_random = -velBall
                                check_lose = True

                    if xBall < -30:
                        score = 0
                        level_define = 1
                        vel = 5
                        velBall = 3
                        pygame.time.delay(100)
                        xBall, yBall = screen_width / 2 - 10, screen_height / 2
                        timer = 5
                        yPlayer, yComp = screen_height/2, screen_height/2
                        text_timer_text = "Match starts in {} sec".format(timer)
                        run_game = False

                    elif xBall > screen_width + 30:
                        check_lose = True
                        score+= 100
                        if score% 200== 0:
                            level_define+=1
                            vel+= 1
                            velBall+=1
                            stop_attack_list.append(True)
                        pygame.time.delay(1000)
                        xBall, yBall = screen_width / 2 - 10, screen_height / 2

                # self.window.blit()
                self.window.fill((0,0,0))
                pygame.draw.rect(self.window, (250,250,250), (screen_width/2-20, 0, 20, screen_height))
                #### Player ####
                Player(self.window, xPlayer, yPlayer)
                #### Comp ####
                Comp(self.window, xComp, yComp)
                #### Ball ####
                Ball(self.window, xBall, yBall)
                ####     Score     ####
                text = font.render('Score: {}'.format(score), True, (200, 0, 70))
                textRect = text.get_rect()
                textRect.center = (screen_width / 2 - 150, 18)
                self.window.blit(text, textRect)
                #### Level ####
                text_lvl = font.render('Level: {}'.format(level_define), True, (0,100, 250))
                self.window.blit(text_lvl, (screen_width/2 + 100, 3))
                #### Timer ####
                if timer==0:
                    text_timer_text = ""
                self.text_timer = font.render(text_timer_text, True, (51, 168, 52))
                self.window.blit(self.text_timer, (screen_width / 2- 150, screen_height - 50))

                pygame.display.update()

if __name__ == "__main__":
    game()
