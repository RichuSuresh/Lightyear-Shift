import pygame #imports the pygame module
import csv #imports the csv module so I can read and write from files



congrats = pygame.image.load("congrats.png") #loads the image which contains the banner of the highscore screen
def leaderboard(player_name, score, mode): #function which reads leaderboard csv file
    if mode == "read":
        score_list = [] #will contain the scores of the players and the names of the players
        with open('leaderboard.csv', mode='r') as file: #opens the leaderboard.csv file in read mode
            reader = csv.reader(file)
            for row in reader: #adds each row from the csv file into list
                score_list.append(row)
        
        score_list.sort(key = lambda x:int(x[1]) , reverse=True) #sorts the list in descending order depending on scores
        
        return(score_list)
    if mode == "write":
        with open('leaderboard.csv', mode='a', newline='') as file: #opens leaderboard in write mode to write player name and score
            writer = csv.writer(file)
            writer.writerow([player_name, score]) #writes the player name and their score into a row


pygame.init()

#function which allows player to enter username when they achieve a highscore
def name_enter(screen):
    font = pygame.font.Font("font.TTF", 25) #loads font
    message_font = pygame.font.Font("font.TTF", 20)
    text_box = pygame.Rect(240, 150, 200, 40) #creates a text box to surround the name being entered
    text_box.centerx = 480/2 #places tetx box in the middle of x axis
    text= '' #string which will contain the username
    finished = False #flag indicating that the player has finished entering username

    while finished == False: #if the player hasn't finished
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1] #removes last character in string if backspace is pressed
                elif event.key == pygame.K_RETURN:
                    return(text) #returns the whole string if enter is pressed
                    finished = True
                elif len(text) < 9: #9 character limit
                    text += event.unicode #adds a character into the string depending on the key pressed on the keyboard
                

        screen.fill((0, 0, 0))
        screen.blit(congrats, (0, 0))
        surface = font.render(text, True, (255,248,108)) #creates a surface for the font to render onto
        screen.blit(surface, (text_box.left+5, text_box.top+5)) #displays the text being entered inside the text box
        pygame.draw.rect(screen, (255,248,108), text_box, 2) #draws the text box onto the screen

        #displays the congratulatory message line by line
        line2 = message_font.render('Enter your username', True, (255,248,108))    
        screen.blit(message_font.render('Congrats you broke the record!', True, (255,248,108)), (60, 300))
        screen.blit(message_font.render('Enter your username', True, (255,248,108)), (110, 330))
        pygame.display.update()

    
    
    
    

    
