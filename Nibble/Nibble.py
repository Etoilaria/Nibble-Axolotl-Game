import pygame
import random
from time import sleep
from pygame import mixer

pygame.init()

# Display the screen
screen = pygame.display.set_mode((450, 600))
pygame.display.set_caption("Nibble the Axolotl Game")
fx = []
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 20) 
number = 0
Slowness = 0

# Worm gets random x
for x in range(50, 451):
    number += 1
    fx.append(number)

# Create Axolotl / Player    
class Axolotl:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
    # Show the Axolotl
    def show(self, screen):
        # Load Axolotl image
        axie_img = pygame.image.load('axie.png')
        screen.blit(axie_img, (self.x, self.y))
    # Move the Axolotl    
    def move(self, screen):
        a, b = pygame.mouse.get_pos()
        # Slowness of player increases everytime a worm gets eaten
        if Slowness >= 5:
            if self.x > a:
                self.x -= 9
            if self.x < a:
                self.x += 9
        elif Slowness >= 6:
            if self.x > a:
                self.x -= 8.5
            if self.x < a:
                self.x += 8.5
        elif Slowness >= 7:
            if self.x > a:
                self.x -= 8
            if self.x < a:
                self.x += 8
        elif Slowness >= 8: 
            if self.x > a:
                self.x -= 7.5
            if self.x < a:
                self.x += 7.5
        elif Slowness >= 9:
            if self.x > a:
                self.x -= 7
            if self.x < a:
                self.x += 7
        elif Slowness >= 10:
            if self.x > a:
                self.x -= 6.5
            if self.x < a:
                self.x += 6.5
        elif Slowness >= 12:
            if self.x > a:
                self.x -= 5.5
            if self.x < a:
                self.x += 5.5
        elif Slowness >= 14:
            if self.x > a:
                self.x -= 4.5
            if self.x < a:
                self.x += 4.5
        elif Slowness > 15:
            if self.x > a:
                self.x -= 3.5
            if self.x < a:
                self.x += 3.5
        
        else:
            self.x = a
# Create food
class Food:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
    def show(self, screen):
        # Load food image
        food_img = pygame.image.load('food.png')
        screen.blit(food_img, (self.x, self.y))
    def move(self, screen):
        self.x = random.choice(fx)
# Create Gameover text        
def Gameover(screen, font2, font):
    global run
    
    # Gameover text
    gameover = font.render('GAMEOVER', True, (125,145,235))
    screen.blit(gameover, [143, 270, 50, 30])
# Show the score    
def show_score(screen, score, font):
    scoretext = font.render('Score: ' + str(score),True, (125,145,235))
    screen.blit(scoretext, [270, 0, 80, 80])
# Show how many worms are being held
def show_slow(screen, Slowness, font):
    slowtext = font.render('Worms held: ' + str(Slowness),True, (125,145,235))
    screen.blit(slowtext, [20, 0, 50, 30])
       
axie = Axolotl(225, 540, 1)
food = Food(225, -10, 9)

pygame.mixer.music.load("Purple Planet Music - Wobbly Weeble 2803A5629 86bpm.mp3")
pygame.mixer.music.play(-1)

run = True

moving = 1
score = 0
# Play the game
while run:
    axie.move(screen)

    if food.x >= axie.x -20 and food.x <= axie.x + 40 and food.y >= 520:
            food.move(screen)
            food.y -= 600
            Slowness += 1
            
    if food.y <= 600 and moving == 1:
        food.y += food.vel
    elif food.y >= 600:
        axie.x = 205
        run = False

    # If the X button is pressed, close the game without errors
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()

    # Make the screen purple
    screen.fill((150, 190, 250))

    # Show the score and slowness
    show_score(screen, score, font)
    show_slow(screen, Slowness, font)

    # If space key is pressed, reset the slowness and add to the score.
    if keys[pygame.K_SPACE]:
        if Slowness <= 4:
            score += Slowness
        if Slowness >= 5 and Slowness <= 10:
            score += Slowness * 2
        if Slowness >= 10 and Slowness <= 15:
            score += Slowness * 3
        if Slowness <= 16:
            score += Slowness * 4
        Slowness = 0

    # The slower the axolotl, the fatter the axoltol!
    if Slowness >= 0 and Slowness <=10:
        axie_img = pygame.image.load('axie3.png')
        screen.blit(axie_img, (axie.x, axie.y))
            
    if Slowness >= 10 and Slowness <= 15:
        axie_img = pygame.image.load('axie2.png')
        screen.blit(axie_img, (axie.x, axie.y))
            
    if Slowness >= 16:
        axie_img = pygame.image.load('axie.png')
        screen.blit(axie_img, (axie.x, axie.y))
        
    food.show(screen)
    
    pygame.display.update()
# Stop EVERYTHING.    
Gameover(screen, font2, font)
pygame.mixer.music.stop()
pygame.display.update()
moving = 0

