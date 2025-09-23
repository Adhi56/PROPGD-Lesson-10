import pygame
import time
import random
 
pygame.init()

screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collect the Recycable Items")

def change_bg(img):
    background = pygame.image.load(img)
    background_image = pygame.transform.scale(background,(screen_width,screen_height))
    screen.blit(background_image,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('bin.png')
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()

class Recycable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()

class NonRecycable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('plastic.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group() # recycable
plastic_list = pygame.sprite.Group() # non recycable
allsprites = pygame.sprite.Group()

bin = Bin()
allsprites.add(bin)

images = ["item1.png", "item2.png", "item3.png"]

for i in range(50):
    item = Recycable(random.choice(images))

    item.rect.x = random.randrange(screen_width)
    item.rect.y = random.randrange(screen_height)

    item_list.add(item)
    allsprites.add(item)

for i in range(20):
    plastic = NonRecycable()

    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)

    plastic_list.add(plastic)
    allsprites.add(plastic)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

playing = True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman", 22)
text = myFont.render("Score = " + str(0), True, black)

while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    timeElapsed = time.time()-start_time

    if timeElapsed >= 60:
        if score >= 20:
            screen.fill(green)
            text1 = myFont.render("Bin Loot Successful", True, black)
        else:
            screen.fill(red)
            text1 = myFont.render("Bin Loot Failed", True, black)

        screen.blit(text1, (250,40))
    else:
        change_bg('bground.png')

        countDown = myFont.render("Time Left: "+ str(60 - int(timeElapsed)), True, black)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0:
                bin.rect.y -= 5

        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y += 5
        
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0:
                bin.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 830:
                bin.rect.x += 5

        
        


    











