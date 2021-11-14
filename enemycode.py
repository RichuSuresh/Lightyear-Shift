import pygame #imports the pygame module
from sprite_groups import * #imports the sprite_groups file as a module
import random #imports random module

boss_image = pygame.transform.scale(pygame.image.load("bosship.png"), (200, 150)) #loads boss image and makes the image bigger
boss_bullet_image = pygame.transform.scale(pygame.image.load("boss_bullet.png"), (25, 45)) #loads boss bullet image

#loads in images of different coloured mobs
greenmob_img = pygame.image.load("greenmob.png")
redmob_img = pygame.image.load("redmob.png")
whitemob_img = pygame.image.load("whitemob.png")
bluemob_img = pygame.image.load("bluemob.png")

class Boss(pygame.sprite.Sprite):  #creates the boss class as a sprite object
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_image 
        self.rect = self.image.get_rect()
        self.rect.centerx = 480 / 2 #boss spawns in the middle of the x axis
        self.rect.bottom = -80 #the bottom part of the boss rect will spawn y-coord -80    
        
    def update(self):
        self.mask = pygame.mask.from_surface(self.image) #creates a collision mask for boss
        if self.rect.y != 30: #y-coord 80 is the stopping point of the boss
            self.rect.y += 1 #increases y coordinate so boss moves down screen

    def shoot(self):
        bossbullet = Bossbullet(self.rect.centerx, (self.rect.bottom)-40) #takes the bottom of the boss and the middle of the boss as spawn points
        all_sprites.add(bossbullet) #adds boss bullets to all sprite group
        boss_bullets.add(bossbullet) #adds boss bullets to its own group

class Bossbullet(pygame.sprite.Sprite): #class for boss' bullets
    def __init__(self, x_spawn, y_spawn):
        pygame.sprite.Sprite.__init__(self) #initializes bullet sprite with x and y coordinates of the boss
        self.image = boss_bullet_image
        self.rect = self.image.get_rect() #gets bullet hitbox
        self.rect.top = y_spawn #y coordinate of the boss will be used to position the bottom of the bullet 
        self.rect.centerx = x_spawn #x coordinate of the boss will be used to position the center of the bullet
        self.speed = 10 #bullet speed

    def update(self):
        self.rect.y += self.speed #adds the speed value onto the y coordinate to make the bullet move downwards 

        if self.rect.top > 600: #if the top of the bullet goes past the bottom of the screen...
            self.kill()          #...remove the bullet

def boss_shoot(): #functions which makes boss shoot
    
    pygame.time.set_timer(boss_shoot_delay, 400) #create a delay everytime the boss fires one bullet
    boss.shoot() #make the boss shoot
    boss_shots += 1 #add one to the bullet counter for boss
    
       
    if boss_shots == 5: #if the boss has fired 5 times...
        pygame.time.set_timer(boss_shoot_delay, 2000) #...pause for 2000ms
        boss_shots = 0 #reset bullet counter

class Mob(pygame.sprite.Sprite): #mob class
    def update(self):
        self.rect.y += self.speed #adds speed value to rect.y to make enemy move down screen
        if self.rect.top > 600: #checks if top of mob hits bottom of the screen
            self.rect.x = random.randrange(480 - 50) #spawns mob randomly along x axis
            self.rect.y = random.randrange(-100, -20) #spawns mobs randomly above the top of the screen
            self.speed = random.uniform(self.l_bound, self.u_bound) #sets random speed for a mob  
            
class green_Mob(Mob): #green mob class which inherits from mob class
    def __init__(self, l_bound, u_bound):
        pygame.sprite.Sprite.__init__(self)
        self.image = greenmob_img
        self.rect = self.image.get_rect() #creates mob hitbox
        self.rect.x = random.randrange(480 - 50) #spawns mob randomly along x axis
        self.rect.y = random.randrange(-100, -20) #spawns mobs randomly above the top of the screen
        self.l_bound = l_bound
        self.u_bound = u_bound
        self.speed = random.uniform(l_bound, u_bound) #sets random speed for a mob using variable bounds
        
class white_Mob(Mob): #white mob class which inherits from mob class
    def __init__(self, l_bound, u_bound):
        pygame.sprite.Sprite.__init__(self)
        self.image = whitemob_img
        self.rect = self.image.get_rect() #creates mob hitbox
        self.rect.x = random.randrange(480 - self.rect.width) #spawns mob randomly along x axis
        self.rect.y = random.randrange(-100, -20) #spawns mobs randomly above the top of the screen
        self.l_bound = l_bound
        self.u_bound = u_bound
        self.speed = random.uniform(l_bound, u_bound) #sets random speed for a mob using variable bounds
        
class blue_Mob(Mob): #blue mob class which inherits from mob class
    def __init__(self, l_bound, u_bound):
        pygame.sprite.Sprite.__init__(self)
        self.image = bluemob_img
        self.rect = self.image.get_rect() #creates mob hitbox
        self.rect.x = random.randrange(480 - self.rect.width) #spawns mob randomly along x axis
        self.rect.y = random.randrange(-100, -20) #spawns mobs randomly above the top of the screen
        self.l_bound = l_bound
        self.u_bound = u_bound
        self.speed = random.uniform(l_bound, u_bound) #sets random speed for a mob using variable bounds
       
class red_Mob(Mob): #red mob class which inherits from mob class
    def __init__(self, l_bound, u_bound):
        pygame.sprite.Sprite.__init__(self)
        self.image = redmob_img
        self.rect = self.image.get_rect() #creates mob hitbox
        self.rect.x = random.randrange(480 - self.rect.width) #spawns mob randomly along x axis
        self.rect.y = random.randrange(-100, -20) #spawns mobs randomly above the top of the screen
        self.l_bound = l_bound
        self.u_bound = u_bound
        self.speed = random.uniform(l_bound, u_bound) #sets random speed for a mob using variable bounds
       

    
boss_shoot_delay = pygame.USEREVENT + 1 #custom event for when boss shoots
pygame.time.set_timer(boss_shoot_delay, 400) #creates a 400 millisecond delay for when the boss should be able to shoot






        





        

    
