import pygame


#function to draw lives onto screen
def draw_lives(lives, screen, image):
    for i in range(lives): #repeatedly draws depending on no. of lives
        img = pygame.transform.scale(image, (40, 20)) #loads image of lives        
        rect = img.get_rect()
        rect.x = 10 + 50*i  #separates the lives images along the x axis
        rect.y = 10
        screen.blit(img, rect) #blits lives onto screen                    



    
