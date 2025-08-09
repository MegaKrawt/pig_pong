import random
import time
import keyboard
import pygame
import mouse
pygame.init()

def appand_byst(i):
    if random.randint(1, 10) == 1:
        byst_tipe_random = random.randint(0, 1)
        if byst_tipe_random == 0: bysts.append(Byst_len(i.x, i.y))
        if byst_tipe_random == 1: bysts.append(Byst_bols(i.x, i.y))

screen_y = 600
screen_x = 700
screen = pygame.display.set_mode((screen_x, screen_y))
a = 0.85
colors = [(255*a, 0*a, 204*a), (0*a, 232*a, 39*a), (0*a, 139*a, 232*a), (255*a, 234*a, 0*a)]
stor = 0

class Boll(pygame.Rect):
    def __init__(self, x = 250, y = 400, size = 30, x_speed = 3):
        pygame.Rect.__init__(self, x, y, size, size)
        self.x_speed = x_speed
        self.y_speed = -3
        self.yy = self.y
        self.xx = self.x
    def do_it(self):
        if self.y + self.height > screen_y: bolls.remove(self)
        if self.yy < 0 or self.colliderect(platforma):
            if self.colliderect(platforma): self.yy = platforma.y - self.height
            if self.x_speed > 0:
                self.x_speed = random.randint(20, 40)/10
            else: self.x_speed = -random.randint(20, 40)/10
            self.y_speed = - self.y_speed
        if self.xx <= 0 or (self.xx + self.width) >= screen_x:
            self.x_speed = -self.x_speed

        self.yy -= self.y_speed
        self.xx += self.x_speed
        self.y = self.yy
        self.x = self.xx

        for i in bloks:
            if self.colliderect(i.rekt_up) or self.colliderect(i.rekt_down):
                self.y_speed = - self.y_speed
                if i in bloks:
                    bloks.remove(i)
                    appand_byst(i)
                    global stor
                    stor += 1

            if self.colliderect(i.rekt_left) or self.colliderect(i.rekt_right):
                self.x_speed = - self.x_speed
                if i in bloks:
                    bloks.remove(i)
                    appand_byst(i)
                    stor += 1


        pygame.draw.circle(screen, (250, 200, 0), (self.x + self.height/2, self.y + self.height/2), self.height/2)

class Platforma(pygame.Rect):
    def __init__(self, x = 200, y = (screen_y - 100)):
        pygame.Rect.__init__(self, x, y, 150, 30)
        self.andlee = 1
    def do_it(self):
        self.x = pygame.mouse.get_pos()[0] - self.width//2

        # if self.x <= 0 or (self.x + self.width) >= screen_x:
        #     self.andlee = -self.andlee
        #
        # self.x += 150*self.andlee

        pygame.draw.rect(screen, (0, 170, 170), self)

class Blok(pygame.Rect):
    def __init__(self, x, y):
        self.color = random.choice(colors)
        pygame.Rect.__init__(self, x, y, 50, 30)
        self.rekt_up =  pygame.Rect(self.x+5, self.y, 40, 5)
        self.rekt_down =  pygame.Rect(self.x+5, self.y+25, 40, 5)
        self.rekt_left =  pygame.Rect(self.x, self.y+5, 5, 20)
        self.rekt_right =  pygame.Rect(self.x+45, self.y+5, 5, 20)
    def do_it(self):
        pygame.draw.rect(screen, (self.color[0]*0.3, self.color[1]*0.3, self.color[2]*0.3), self)
        pygame.draw.rect(screen, self.color, self.rekt_up)
        pygame.draw.rect(screen, self.color, self.rekt_down)
        pygame.draw.rect(screen, self.color, self.rekt_left)
        pygame.draw.rect(screen, self.color, self.rekt_right)


byst_len_time_start = 0
byst_bols_time_start = 0
class Byst(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, 50, 30)
        self.image = pygame.transform.scale(image, (self.width, self.height))
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    def collide_platforma(self):
         return self.colliderect(platforma)

class Byst_len(Byst):
    def __init__(self, x, y):
        Byst.__init__(self, x, y, pygame.image.load("images/byst_len.png"))
    def do_it(self):
        self.draw()
        self.y += 1
        if self.y + self.height > screen_y: bysts.remove(self)
        if self.collide_platforma():
            bysts.remove(self)
            global byst_len_time_start
            byst_len_time_start = time.time()

class Byst_bols(Byst):
    def __init__(self, x, y):
        Byst.__init__(self, x, y, pygame.image.load("images/byst_bols.png"))
    def do_it(self):
        self.draw()
        self.y += 1
        if self.y + self.height > screen_y: bysts.remove(self)
        global byst_bols_time_start
        if self.collide_platforma() :
            bolls.append(Boll(100, 400, x_speed= 3))
            bolls.append(Boll(400, 300, x_speed= -3))
            bysts.remove(self)




platforma = Platforma()
bolls = []
bolls.append(Boll())
bloks = []
bysts = []
# for iy in range(1):
#     for ix in range(10):
#         bloks.append(Blok(ix*70 +10, iy*50 + 10))

for iy in range(3):
    for ix in range(10):
        bloks.append(Blok(ix * 70 + 10, 50*iy + 10))


clock = pygame.time.Clock()
ran = True
while ran:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ran = False

    screen.fill((0, 0 ,0))
    stor_text = pygame.font.Font(None, 300).render(str(stor), 1, (50, 50, 50))
    screen.blit(stor_text , ((screen_x//2 - stor_text.get_rect().width//2), 250))

    platforma.do_it()

    end_line = 1
    for i in bolls:
        i.do_it()
    for i in bloks:
        if end_line < (i.y-10)//50: end_line = (i.y-10)//50
        i.do_it()
    if  end_line < 3:
        for ix in range(10):
            bloks.append(Blok(ix * 70 + 10, -50 + 10))
        for i in range(50):
            screen.fill((0, 0, 0))
            screen.blit(stor_text, ((screen_x // 2 - stor_text.get_rect().width // 2), 250))

            for i in bloks:
                i.y += 1
                i.rekt_up.y += 1
                i.rekt_down.y += 1
                i.rekt_left.y += 1
                i.rekt_right.y += 1
                i.do_it()
            clock.tick(120)
            for event in pygame.event.get(): pass
            for i in bolls:
                i.do_it()
            platforma.do_it()



            for i in bysts:
                i.do_it()
            if byst_len_time_start != 0:
                if (round(time.time() - byst_len_time_start)) >= 10:
                    byst_len_time_start = 0
            if byst_len_time_start == 0 and platforma.width > 150:
                platforma.width -= 1



            pygame.display.flip()

    for i in bysts:
        i.do_it()
    if byst_len_time_start != 0:
        if platforma.width < 300: platforma.width += 1
        if (round(time.time() - byst_len_time_start)) >= 10:
            byst_len_time_start = 0
    if byst_len_time_start == 0 and platforma.width > 150:
        platforma.width -= 1




    if keyboard.is_pressed(" "):

        fff = pygame.font.Font(None, 200)
        pays = fff.render(('пауза'), 1, (150, 150, 150))
        screen.blit(pays, (150, 200))
        pygame.display.flip()

        while keyboard.is_pressed(" "): pass
        payza = True
        while payza:
            if keyboard.is_pressed(" "): break
            time.sleep(0.01)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ran = False
                    payza = False
        while keyboard.is_pressed(" "): pass


    pygame.display.flip()
    clock.tick(120)
