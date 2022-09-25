import pygame
import sys
import time
from threading import Thread

pygame.init()


clock = pygame.time.Clock() #fps

#Cookie Clicker Variables
ability_timer = 0
cooldown = 10
ability1 = False
ability1_unlocked = False
t_cookies = 0 # start cookies
cps = 0
cookies = 0 #start cookies
cost_1 = 5
cost_2 = cost_1 * 1.2 * 10
cost_3 = 5
cost_4 = cost_3 * 1.2 * 10
click_amount = 1 # start click amount
font = pygame.font.Font("C:/Tempo/Cookie Clicker/f/DePixelBreit.ttf", 30) #font
font1 = pygame.font.Font("C:/Tempo/Cookie Clicker/f/DePixelBreit.ttf", 15) #font
font2 = pygame.font.Font("C:/Tempo/Cookie Clicker/f/DePixelBreit.ttf", 25) #font

#Frame
bg_color = (88, 171, 202) #bg color
HEIGHT = 1000 #resolution
WIDTH = 800 #resolution

cookie_img = pygame.image.load("C:/Tempo/Cookie Clicker/img/cookie.png") #cookie img
upgrade1_img = pygame.image.load("C:/Tempo/Cookie Clicker/img/upgrade1.png") #upgrade1 img
supercookie_img = pygame.image.load("C:/Tempo/Cookie Clicker/img/super cookie.png") # First Ability


# Cookie
class Cookie: #cookie class
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.image.load("C:/Tempo/Cookie Clicker/img/cookie.png")
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pos_x = 100
        self.pos_y = 100
        self.pos_x = x
        self.pos_y = y
        self.clicked = False

class Upgrade: #Upgrade class
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.image.load("C:/Tempo/Cookie Clicker/img/upgrade1.png")
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pos_x = 100
        self.pos_y = 100
        self.pos_x = x
        self.pos_y = y
        self.clicked = False

upgrade1 = Upgrade(400, 400,upgrade1_img, 2)
upgrade2 = Upgrade(400, 400,upgrade1_img, 2)
upgrade3 = Upgrade(400, 400,upgrade1_img, 2)
cookie = Cookie(250, 400, cookie_img, 2)
    

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Cookie Clicker') #title


def text(x, y): #Cookie text render
    cookie_amount = font.render(f"Cookies: {int(cookies)}", True, (0, 0, 0))
    total_cookies = font2.render(f"Total Cookies: {int(t_cookies)}", True, (0, 0, 0))
    up1 = font1.render(f"+1 per click", True, (0, 0, 0))
    up1_price = font1.render(f"Price: {int(cost_1)}", True, (0, 0, 0))
    up2 = font1.render(f"+10 per click", True, (0, 0, 0))
    up2_price = font1.render(f"Price: {int(cost_2)}", True, (0, 0, 0))
    up3 = font1.render(f"+1 per second", True, (0, 0, 0))
    up3_price = font1.render(f"Price: {int(cost_3)}", True, (0, 0, 0))
    up4 = font1.render(f"+10 per second", True, (0, 0, 0))
    up4_price = font1.render(f"Price: {int(cost_4)}", True, (0, 0, 0))
    abilities = font2.render(f"Abilities", True, (0, 0, 0))
    screen.blit(cookie_amount, (50, 30))
    screen.blit(total_cookies, (50, 80))
    screen.blit(up1, (815, 250))
    screen.blit(up1_price, (817, 270))
    screen.blit(up2, (815, 300))
    screen.blit(up2_price, (817, 320))
    screen.blit(up3, (815, 350))
    screen.blit(up3_price, (817, 370))
    screen.blit(up4, (815, 400))
    screen.blit(up4_price, (815, 420))
    screen.blit(abilities, (815, 150))


def cookies_ps():
    global t_cookies
    global cookies # allow cookies to be modified in this thread
    while True: # loop forever to prevent memory being unnecessarily used on starting threads every second
        cookies = cookies + cps
        t_cookies = t_cookies + cps
        time.sleep(1)

thread = Thread(target=cookies_ps)


thread.start() # start the thread
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left = pygame.mouse.get_pressed() #Left click
            mouse_pos = pygame.mouse.get_pos()
            if 372 <= mouse_pos[0] <= 629 and 263 <= mouse_pos[1] <= 514:
                if (left[0]):
                    if ability1 == True:
                        cookies = cookies + click_amount * 10
                        t_cookies = t_cookies + click_amount * 10
                    elif ability1 == False:
                        cookies = cookies + click_amount
                        t_cookies = t_cookies + click_amount
                        if t_cookies >= 10000:
                            ability1_unlocked = True
            if 759 <= mouse_pos[0] <= 982 and 230 <= mouse_pos[1] <= 283:
                if (left[0]):
                    if cookies >= cost_1:
                        cookies = cookies - cost_1
                        cost_1 = cost_1 * 1.2
                        cost_2 = cost_1 * 1.2 * 10
                        click_amount = click_amount + 1
            if 765 <= mouse_pos[0] <= 981 and 292 <= mouse_pos[1] <= 337:
                if (left[0]):
                    if cookies >= cost_2:
                        cookies = cookies - cost_2
                        click_amount = click_amount + 10
                        cost_1 = cost_2 * 1.2
                        cost_2 = cost_1 * 1.2 * 10
            if 762 <= mouse_pos[0] <= 979 and 345 <= mouse_pos[1] <= 388:
                if (left[0]):
                    if cookies >= cost_3:
                        cookies = cookies - cost_3
                        cost_3 = cost_3 * 1.2
                        cost_4 = cost_3 * 1.2 * 10
                        cps = cps + 1
            if 762 <= mouse_pos[0] <= 977 and 389 <= mouse_pos[1] <= 435:
                if (left[0]):
                    if cookies >= cost_3 * 1.2 * 10:
                        cookies = cookies - cost_3 * 1.2 * 10
                        cost_3 = cost_3 * 1.2 * 10
                        cost_4 = cost_4 * 1.2 * 10
                        cps = cps + 10
            if 774 <= mouse_pos[0] <= 798 and 183 <= mouse_pos[1] <= 207:
                if (left[0]):
                    if ability1 == False:
                        if ability1_unlocked == True:
                            if cooldown < 0:
                                ability1 = True
                                ability_timer = 300
                            elif cooldown >= 0:
                                print("You can't use that yet!")
                        elif ability1_unlocked == False:
                            print("You haven't unlocked that yet")

    screen.fill(bg_color)
    screen.blit(cookie_img, (375, 275))   
    screen.blit(upgrade1_img, (750, 200))
    screen.blit(upgrade1_img, (750, 250))
    screen.blit(upgrade1_img, (750, 300))
    screen.blit(upgrade1_img, (750, 350))
    screen.blit(supercookie_img, (665, 130))
    text(10, 60) #Display Cookies
    pygame.display.update()
	
    if ability_timer > 0:
        ability_timer = ability_timer - 1
        if ability_timer <= 0:
            cooldown = 60
            if cooldown >= 0:
                cooldown = cooldown - 1
                if cooldown > 0:
                    ability1 = False

    clock.tick(60) #fps

pygame.quit()