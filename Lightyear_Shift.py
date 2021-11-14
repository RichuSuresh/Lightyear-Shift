import pygame #imports the pygame module into python
import time #imports the time module into python
import random #imports the random module in python
from enemycode import * #imports code for boss fights (separate python file)
from sprite_groups import * #imports all sprite groups (separate file)
from Lives_code import * #imports code for lives (separate file)
from highscores import * #imports code for leaderboard system

FPS = 60 #constant for our frames per second (affects how fast the game window is updated)

#rgb values for colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

WIDTH = 480 #screen width
HEIGHT = 600 #screen height
pygame.init() #initializes pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #creates a game window, 480 is the width and 600 is the height
pygame.display.set_caption("Lightyear Shift") #caption for the game window
clock = pygame.time.Clock() #makes sure the game is running at correct fps

player_image = pygame.image.load("player.png") #loads player image

#loads different player skins
player_skin1 = pygame.image.load("pl_image1.png")
player_skin2 = pygame.image.load("pl_image2.png")
player_skin3 = pygame.image.load("pl_image3.png")
player_skin4 = pygame.image.load("pl_image4.png")
player_skin5 = pygame.image.load("pl_image5.png")

skins = [player_image, player_skin1, player_skin2, player_skin3, player_skin4, player_skin5] #list which will be used to cycle through the skin to be used as the player object surface

#images for menu navigation
a_sign = pygame.image.load("a_sign.png")
d_sign = pygame.image.load("d_sign.png")
lb_sign = pygame.image.load("lb_sign.png")
hlp_sign = pygame.image.load("hlp_sign.png")

help_page = pygame.image.load("help.png")#image for help screen

#loads in the images of the the different coloured bullets
redbullet_img = pygame.transform.scale(pygame.image.load("redbullet.png"), (10, 30))
greenbullet_img = pygame.transform.scale(pygame.image.load("greenbullet.png"), (10, 30))
bluebullet_img = pygame.transform.scale(pygame.image.load("bluebullet.png"), (10, 30))
whitebullet_img = pygame.transform.scale(pygame.image.load("whitebullet.png"), (10, 30))

title = pygame.image.load("title.png") #loads title image
hit_img = pygame.image.load("hit.png").convert()
        
#function to write text onto screen
def write_text(text, size, x, y):
    font = pygame.font.Font("font.TTF", size) #font that I'll use 
    surface = font.render(text, True, (255,248,108))
    rect = surface.get_rect()
    rect.center = (x, y)
    screen.blit(surface, rect)
    
class Player(pygame.sprite.Sprite): #creates the Player class as a sprite object
    def __init__(self, skin): #code that will be run whenever player object is created
        pygame.sprite.Sprite.__init__(self) #initializes the sprite functions from pygame
        self.image = skins[skin] #uses a skin from the skins list as the surface for the image
        self.rect = self.image.get_rect() #gets he surrounding border of the rectangle (hitbox)
        self.rect.centerx = WIDTH / 2 #uses the center of the image rect (above) to place surface in the center of x axis
        self.rect.bottom = HEIGHT - 10 #on y axis, the player will be slightly above the bottom of the screen
        self.speed = 5 #speed of the mob
        
    def update(self):
        self.vel = 0 #used to reset the character velocity. If no keys are pressed, velocity will always be 0
        keypresses = pygame.key.get_pressed() #returns a list of all keys being pressed down at this instant
        if keypresses[pygame.K_RIGHT] and self.rect.right < WIDTH and game_over == False: #checks if right key is pressed and also whether the rectangle is touching right edge
            self.vel += self.speed #makes the velocity positive
            
        if keypresses[pygame.K_LEFT] and self.rect.left > 0 and game_over == False: #checks if left key is pressed and also whether the rectangle is touching left edge
            self.vel -= self.speed #makes the velocity negative
            
        self.rect.x += self.vel #adds the velocity onto the x coordinate of player rect

    def shoot(self, colour): #function to allow player to shoot
        #the colour parameter will be used to determine which coloured bullet the player should shoot
        if colour == 'red':
            red_bullet = redbullet(self.rect.centerx, self.rect.top) #creates red bullet object
            all_sprites.add(red_bullet) #adds red bullet to group so it gets drawn onto the screen
            red_bullets.add(red_bullet) #adds red bullet to red bullet group
        elif colour == 'green':
            green_bullet = greenbullet(self.rect.centerx, self.rect.top)
            all_sprites.add(green_bullet)
            green_bullets.add(green_bullet) #adds green bullet to green bullet group
        elif colour == 'white':
            white_bullet = whitebullet(self.rect.centerx, self.rect.top)
            all_sprites.add(white_bullet)
            white_bullets.add(white_bullet) #adds white bullet to white bullet group
        elif colour == 'blue':
            blue_bullet = bluebullet(self.rect.centerx, self.rect.top)
            all_sprites.add(blue_bullet)
            blue_bullets.add(blue_bullet) #adds blue bullet to blue bullet group
            
class playerbullet(pygame.sprite.Sprite): #creates the player bullet class as a sprite object
    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y += self.speed #adds the speed value onto the y coordinate to make the bullet move upwards

        if self.rect.bottom < 0: #if the bottom of the bullet goes past the top of the screen...
            self.kill()          #...remove the bullet

class redbullet(playerbullet):
    def __init__(self, x_spawn, y_spawn):
        pygame.sprite.Sprite.__init__(self) #initializes bullet sprite with x and y coordinates of player
        self.image = redbullet_img #uses an image of a red bullet asthe surface
        self.rect = self.image.get_rect() #gets bullet hitbox
        self.rect.bottom = y_spawn #y coordinate of player will be used to position the bottom of the bullet 
        self.rect.centerx = x_spawn #x coordinate of player will be used to position the center of the bullet
        self.speed = -10 #bullet speed

class greenbullet(playerbullet):
    def __init__(self, x_spawn, y_spawn):
        pygame.sprite.Sprite.__init__(self) #initializes bullet sprite with x and y coordinates of player
        self.image = greenbullet_img #uses an image of a green bullet asthe surface
        self.rect = self.image.get_rect() #gets bullet hitbox
        self.rect.bottom = y_spawn #y coordinate of player will be used to position the bottom of the bullet 
        self.rect.centerx = x_spawn #x coordinate of player will be used to position the center of the bullet
        self.speed = -10 #bullet speed

class whitebullet(playerbullet):
    def __init__(self, x_spawn, y_spawn):
        pygame.sprite.Sprite.__init__(self) #initializes bullet sprite with x and y coordinates of player
        self.image = whitebullet_img #uses an image of a white bullet asthe surface
        self.rect = self.image.get_rect() #gets bullet hitbox
        self.rect.bottom = y_spawn #y coordinate of player will be used to position the bottom of the bullet 
        self.rect.centerx = x_spawn #x coordinate of player will be used to position the center of the bullet
        self.speed = -10 #bullet speed

class bluebullet(playerbullet):
    def __init__(self, x_spawn, y_spawn):
        pygame.sprite.Sprite.__init__(self) #initializes bullet sprite with x and y coordinates of player
        self.image = bluebullet_img #uses an image of a blue bullet asthe surface
        self.rect = self.image.get_rect() #gets bullet hitbox
        self.rect.bottom = y_spawn #y coordinate of player will be used to position the bottom of the bullet 
        self.rect.centerx = x_spawn #x coordinate of player will be used to position the center of the bullet
        self.speed = -10 #bullet speed
    


#function to create the screen displayed when the player starts the program and also when the player dies
def intro_screen():
    current_skin = 0 #counter for which skin the player is currently displaying                       
    current_screen = "main" #current screen the player is on (main screen is default)
    started = False #boolean value that determines if the game has started or not
    keypresses = pygame.key.get_pressed()
    while started == False:
        if current_screen == "main":
            screen.fill(black)
            screen.blit(title, (25, 10)) #draws the title for the game onto the screen
            write_text("Points: "+str(mob_points+boss_points)+"", 30, WIDTH/2, (HEIGHT/2)+10) #writes the amount of player got in their last run onto the intro screen
            write_text("Press Enter to start", 17, WIDTH/2, (HEIGHT/2)+100) #writes press enter to start onto the screen
            screen.blit(skins[current_skin], (208, 558)) #displays the player character with the skin
            #displays signs for menu navigation
            screen.blit(lb_sign, (420, 300))
            screen.blit(a_sign, (140, 565))
            screen.blit(d_sign, (300, 565))
            screen.blit(hlp_sign, (5, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if current_screen == "main":
                if event.type == pygame.KEYDOWN:
                    #if the player presses a, the program will display the previous skin in the skins list
                    if event.key == pygame.K_a:
                        if current_skin <= len(skins)-1 and current_skin > 0: #the current_skin integer will only decrease when it's 5 or below and greater than 0
                            current_skin -= 1 #goes to previous index in the list
                        elif current_skin == 0: #the list will wrap around to the last item in the list if the integer is 0 and A is pressed
                            current_skin = len(skins) - 1
                    #if the player presses d, the program will display the next skin the skins  list
                    if event.key == pygame.K_d:
                        if current_skin >= 0 and current_skin < len(skins)-1: #integer will only increase if the number is greater than or equal to 0 but less than 5
                            current_skin += 1
                        elif current_skin == len(skins)-1: #list will return to 0 if the player presses D and integer is 5
                            current_skin = 0
                    if event.key == pygame.K_RETURN:
                        started = True #starts the  game when player presses enter
                    if event.key == pygame.K_RIGHT:
                        current_screen = "leaderboard" #switches to the leaderboard screen
                    if event.key == pygame.K_LEFT:
                        current_screen = "help" #switches to the help page
                            
            #code for leaderboard screen             
            if current_screen == "leaderboard":
                score_list = leaderboard(None, None, 'read') #opens leaderboard in read mode
                screen.fill(black)
                write_text('Leaderboard', 40, WIDTH/2, 30)
                for i in range(5):
                    write_text(str(i+1)+".", 30, 50, 100+(50*i)) #displays player's position
                    write_text(str(score_list[i][0]), 30, WIDTH/2, 100+(50*i)) #displays the names of the player
                    write_text(str(score_list[i][1]), 30, 3*(WIDTH/4) + 80, 100+(50*i)) #displays their score
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_screen = "main" #switches to main screen

            #code for help screen
            if current_screen == "help":
                screen.fill(black)
                screen.blit(help_page, (0,0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        current_screen = "main"
                
    return(current_skin) #returns the skin integer to be used for player object

                               
boss = Boss()   #boss object
boss_shots = 0 #the amount of times the boss has shot
boss_hp = 20 #amount of hits it takes to defeat boss
boss_fight = False #determines whether a boss fight will take place or not
boss_points = 0 #total points from boss kills

mob_lbound = 1 #lower bound for mob speed
mob_ubound = 4 #upper bound for mob speed
comparison_points = 25 #amount of points the player should go up by to get a mob speed up
mob_points = 0 #total points from mob kills
mob_amount = 5 #amount of mobs that will appear on the screen
mob_colours = ['red', 'green', 'blue', 'white'] #list which contains the colours of the mobs, a random colour from this list is chosen

lives = 3 #player's lives

game_over = True #flag to determine when the game is in game over state

#adds enemies into the all_sprites group to be drawn onto screen
def mob_creation():
    #randomly chooses a colour from the mob colour to list to determine which coloured mobs should spawn in when the game starts
    if random.choice(mob_colours) == 'red':
        redmob = red_Mob(mob_lbound, mob_ubound) #creates a red coloured mob
        all_sprites.add(redmob) #adds mob into all sprites group
        redgroup.add(redmob) #adds red mob into group which contains red mobs

    elif random.choice(mob_colours) == 'green':
        greenmob = green_Mob(mob_lbound, mob_ubound)
        all_sprites.add(greenmob)
        greengroup.add(greenmob) #adds green mob into group which contains green mobs
        
    elif random.choice(mob_colours) == 'blue':
        bluemob = blue_Mob(mob_lbound, mob_ubound)
        all_sprites.add(bluemob)
        bluegroup.add(bluemob) #adds blue mob into group which contains blue mobs

    elif random.choice(mob_colours) == 'white':
        whitemob = white_Mob(mob_lbound, mob_ubound)
        all_sprites.add(whitemob)
        whitegroup.add(whitemob) #adds white mob into group which contains white mobs


counter =  0 #counter to determine when mob_creation should be called 
shoot_cooldown = pygame.USEREVENT +2 #cooldown for player bullets
hit_event = pygame.USEREVENT + 3
shot_delay = False #flag that determines when a cooldown should occur
running = True #value to determine whether the game is on or off
damaged = False #determines when the hit animation should play, shows that player has been damaged
fade = hit_img #image for the hit animation
fade_count = 0 #is incremented and subtracted from 255 to get the alpha value of the fade image
    
while running: #main loop for the game, will run as long as long as running = True
    #reset all of the base values when player dies 
    if game_over == True:
        pygame.time.set_timer(hit_event, 0) #stops the fade animation event
        score_list = leaderboard(None, None, 'read') #list of users on the leaderboard
        if mob_points + boss_points > int(score_list[0][1]):
            leaderboard(name_enter(screen), int(mob_points + boss_points), 'write') #if the player broke a record they'll be put on the leaderboard

        all_sprites.empty() #empties the all_sprites group in order to remove everything from the screen
        player = Player(intro_screen()) #creates player object using a skin from the skins (using current_skin as the index) as the image surface
        all_sprites.add(player) #I want the player to remain on the intro screen
        all_sprites.update()
        
        game_over = False
        
        lives = 3
        
        boss = Boss()   #boss object
        boss_shots = 0 #the amount of times the boss has shot
        boss_hp = 20 #amount of hits it takes to defeat boss
        boss_fight = False #determines whether a boss fight will take place or not
        boss_points = 0 #total points from boss kills

        #updates and empties each mob group, this part alos resets the points and the speed of the mobs
        redgroup.empty()
        greengroup.empty()
        bluegroup.empty()
        whitegroup.empty()
        redgroup.update()
        greengroup.update()
        bluegroup.update()
        whitegroup.update()
        mob_lbound = 1 #lower bound for mob speed
        mob_ubound = 7 #upper bound for mob speed
        comparison_points = 10 #amount of points the player should go up by to get a mob speed up
        mob_points = 0 #total points from mob kills

        for i in range(mob_amount):
            mob_creation()
            
        damaged = False
        
        
    clock.tick(FPS) #makes sure that the game is processed at a constant speed. 
    
    for event in pygame.event.get(): #processes events
        if event.type == pygame.QUIT: #checks if the player wants to close window
            running = False #breaks out of the while loop

        if event.type == shoot_cooldown: #resets cooldown and allows player to shoot again
            shot_delay = False
            
        if event.type == pygame.KEYDOWN: #checks if a key has been pressed down
            #these IF statements also checks to make sure there isn't a cooldown before the player can shoot
            if event.key == pygame.K_w and shot_delay == False: #if w is pressed then a red bullet will be fired
                pygame.time.set_timer(shoot_cooldown, 100) #activates cooldown timer
                shot_delay = True #changes flag to signify that a cooldown is needed
                player.shoot('red')             
            elif event.key == pygame.K_a and shot_delay == False: #if a is pressed then a green bullet will be fired
                pygame.time.set_timer(shoot_cooldown, 100)
                shot_delay = True
                player.shoot('green')
            elif event.key == pygame.K_s and shot_delay == False: #if s is pressed then a white bullet will be fired
                pygame.time.set_timer(shoot_cooldown, 100)
                shot_delay = True
                player.shoot('white')
            elif event.key == pygame.K_d and shot_delay == False: #if d is pressed a blue bullet ill be fired
                pygame.time.set_timer(shoot_cooldown, 100)
                shot_delay = True
                player.shoot('blue')

        if event.type == hit_event and fade_count < 255: #if the hit event occurs, constantly decrease the transparency of the fade image until it's fully transparent
            fade.set_alpha(255 - fade_count) #makes image more transparent by decreasing the alpha value
            fade_count += 1 #increments the fade counter to be subtracted

        if fade_count == 255: #255 is max alpha
            pygame.time.set_timer(hit_event, 0) #event stops at max alpha
            damaged = False #reste boolean value
            fade_count = 0 #resets fade count
            
        if boss_fight == True:
            all_sprites.add(boss)
            if event.type == boss_shoot_delay and boss.rect.y >= 30: #when boss shooting user event is detected and the boss is at y coordinate 80
                pygame.time.set_timer(boss_shoot_delay, 400) #create a delay everytime the boss fires one bullet
                boss.shoot() #make the boss shoot
                boss_shots += 1 #add one to the bullet counter for boss
                
                if boss_shots == 5: #if the boss has fired 5 times...
                    pygame.time.set_timer(boss_shoot_delay, 2000) #...pause for 2000ms
                    boss_shots = 0 #reset bullet counter
    #start a cooldown 
    if damaged == True:
        pygame.time.set_timer(hit_event, 1)
        
    if lives == 0: #if the player has no lives left
        game_over = True

    #if the mob count ever decreases, this part makes sure it returns to its normal amount
    if len(redgroup) + len(greengroup) +len(whitegroup) + len(bluegroup) < mob_amount:
        #chooses a random coloured mob to spawn on the screen
        mob_creation()
        
    all_sprites.update() #updates the all_sprites group

    #collision checks between mobs and wrong bullets, wrongly coloured bullets will disappear without killing rhe mob
    false_collision = pygame.sprite.groupcollide(bluegroup, red_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(bluegroup, white_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(bluegroup, green_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(redgroup, blue_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(redgroup, white_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(redgroup, green_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(greengroup, blue_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(greengroup, red_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(greengroup, white_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(whitegroup, red_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(whitegroup, blue_bullets, False, True)
    false_collision = pygame.sprite.groupcollide(whitegroup, green_bullets, False, True)
    
    #collision detection between coloured bullets and corresponding coloured mob
    blue_collisions = pygame.sprite.groupcollide(bluegroup, blue_bullets, True, True)
    white_collisions = pygame.sprite.groupcollide(whitegroup, white_bullets, True, True)
    green_collisions =  pygame.sprite.groupcollide(greengroup, green_bullets, True, True)
    red_collisions = pygame.sprite.groupcollide(redgroup, red_bullets, True, True) 

    if len(red_collisions) > 0 or len(green_collisions) > 0 or len(white_collisions) > 0 or len(blue_collisions) > 0: #list has to be greater than 0 for collisions to have occurred
        mob_creation() #creates a new mob
        mob_points += 1 #awards 1 point to the player
        if mob_points % comparison_points == 0: #if points have gone up by 10...
            mob_lbound += 1 #increase speed by an amount
            mob_ubound += 1
            player.speed += 1 #increases speed of the player to keep up with mobs
        if boss_fight == False: #if a boss fight is not taking place
            boss_spawn = random.randint(1, 10) #generates random integer to see if boss spawns
            if boss_spawn == 2 and mob_points >= 50: #if the number generated is 2 a boss fight will take place
                boss_fight = True

    #collision detection between boss bullet and player
    collisions = pygame.sprite.spritecollide(player, boss_bullets, True) #delete bullet
    if len(collisions) > 0:
        lives -= 1 #lose a life when player is hit
        damaged = True #flag that the player has been hit
        fade_count = 0 #resets fade counter in case player is hit again whent he first image is fading

    #collision detection between player bullet and boss
    red_boss_collisions = pygame.sprite.spritecollide(boss, red_bullets, True, pygame.sprite.collide_mask)  #delete bullet
    blue_boss_collisions = pygame.sprite.spritecollide(boss, blue_bullets, True, pygame.sprite.collide_mask) #delete bullet
    green_boss_collisions = pygame.sprite.spritecollide(boss, green_bullets, True, pygame.sprite.collide_mask)  #delete bullet
    white_boss_collisions = pygame.sprite.spritecollide(boss, white_bullets, True, pygame.sprite.collide_mask)  #delete bullet
    
    if len(red_boss_collisions) > 0  or len(blue_boss_collisions) > 0 or len(green_boss_collisions) > 0 or len(white_boss_collisions) > 0:
        boss_hp -= 1 #decrease boss' hp
        if boss_hp == 0: #kill boss once hp reaches 0
            boss_points += 20 #awards 20 points to player
            boss.kill()
            boss.rect.bottom = -80 #respawn boss away from the top edge of the screen
            boss_hp += 20 #reset boss' hp
            boss_fight = False #sets boss fight to false which allows another boss to spawn
            boss_shots = 0 #resets the counter for the amount of shots the boss takes        

            
    #collision check between coloured mobs and player    
    red_player_collisions = pygame.sprite.spritecollide(player, redgroup, True) #list of collisions between player and red mobs
    blue_player_collisions = pygame.sprite.spritecollide(player, bluegroup, True) #collisions between player and blue mobs
    green_player_collisions = pygame.sprite.spritecollide(player, greengroup, True) #collisions between player and green mob
    white_player_collisions = pygame.sprite.spritecollide(player, whitegroup, True) #collisions between player and white mob

    if len(red_player_collisions) > 0 or len(blue_player_collisions) > 0 or len(green_player_collisions) > 0 or len(white_player_collisions) > 0: #list has to be greater than 0 for collisions to have occurred
        mob_creation() #creates a new mob
        lives -= 1 #lose a life when player is hit
        damaged = True
        fade_count = 0
        
    screen.fill(black) #fills the screen with black
    #displays the fade animation when the player is hit
    if damaged == True:
        screen.blit(fade, (0,0))
    if game_over == False:
        draw_lives(lives, screen, player_image) #calls function to draw lives onto screen
        all_sprites.draw(screen) #draws all sprite objects onto the screen
        write_text(""+str(mob_points+boss_points)+"", 40, WIDTH/2, 10) #displays the amount of points the player currently has onto the screen
    pygame.display.update() #updates the game window display


pygame.quit() #quits pygame
