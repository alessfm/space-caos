# Libraries #

import os,pygame,random 

# x Libraries x #

pygame.init() # initialize pygame objects 

# Variables #

# define the colours
# they are rgb form --> 
# color_type = (r,g,b)
white = (255, 255, 255) 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255) 
black = (0, 0, 0) 
  
# set the Dimensions 
width = 650
height = 700
  
# size of a block 
pixel = 64
  
# x Variables x #


# Out_Functions #

# define a function for setting 
# the image at particular 
# coordinates 
def player(x, y): 
# paste image on screen object 
    screen.blit(playerImage, (x, y))


# define a function for setting 
# the image at particular 
# coordinates 
def block(x, y): 
# paste image on screen object 
    screen.blit(blockImage, 
			(x, y))

# x Out_Functions x #


# Load Game #

# set Screen 
screen = pygame.display.set_mode((width,  
                                  height)) 
  
# set caption 
pygame.display.set_caption(
    "Space Caos") 
  
# load the icon image
#gameIcon = pygame.image.load(os.path.join('Assets',''))
  
# set icon 
#pygame.display.set_icon(gameIcon) 
  
# load the background image 
#backgroundImg = pygame.image.load(os.path.join('Assets','background.png'))

# load the  player image 
playerImage = pygame.image.load('racecar.png') 


# Player #

# set the position of the player
playerXPosition = (width/2) - (pixel/2) 

# So that the player will be 
# at height of 20 above the base 
playerYPosition = height - pixel - 10	

# set initially 0 
playerXPositionChange = 0

# Player #


# Enemy #

# load the enemy image 
#blockImage = pygame.image.load(os.path.join('Assets',''))

# set the random position 
blockXPosition = random.randint(0, 
								(width - pixel)) 

blockYPosition = 0 - pixel 

# set the speed of 
# the enemy 
blockXPositionChange = 0
blockYPositionChange = 2	


# In_Functions #

# define a function for 
# collision detection 
def crash(): 
# take a global variable 
    global blockYPosition 

    # check conditions 
    if playerYPosition < (blockYPosition + pixel): 

        if ((playerXPosition > blockXPosition 
            and playerXPosition < (blockXPosition + pixel)) 
            or ((playerXPosition + pixel) > blockXPosition 
            and (playerXPosition + pixel) < (blockXPosition + pixel))): 

            blockYPosition = height + 1000

# x In-Functions x #


# Run Game #

running = True

while running: 
    # set the image on screen object 
    #screen.blit(backgroundImg, (0, 0))
    
    # loop through all events 
    for event in pygame.event.get(): 
            
        # check the quit condition 
        if event.type == pygame.QUIT: 
            # quit the game 
            pygame.quit() 

        # movement key control of player 
        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_RIGHT: 

                playerXPositionChange = 3

            if event.key == pygame.K_LEFT: 

                playerXPositionChange = -3

        if event.type == pygame.KEYUP: 

            if event.key == pygame.K_RIGHT or pygame.K_LEFT: 

                playerXPositionChange = 0


# Boundaries to the Player #  

    # if it comes at right end, 
    # stay at right end and 
    # does not exceed 
    if playerXPosition >= (width - pixel): 
        playerXPosition = (width - pixel) 
                
    # if it comes at left end, 
    # stay at left end and 
    # does not exceed 
    if playerXPosition <= 0: 
        playerXPosition = 0

# x Boundaries to the Player x #


# All moviment #

    # Multiple Blocks Movement after each other 
    # and condition used because of game over function 
        if (blockYPosition >= height - 0 and
            blockYPosition <= (height + 200)): 
                    
            blockYPosition = 0 - pixel 
                    
            # randomly assign value in range 
            blockXPosition = random.randint(0, (width - pixel))

        # movement of Player 
        playerXPosition += playerXPositionChange 

        # movement of Block 
        blockYPosition += blockYPositionChange

# x All moviment x #


# x Run Game x #


# Call Functions #

    #player(playerXPosition, playerYPosition)  
    #block(blockXPosition, blockYPosition) 
    crash() 

# x Call Functions x #

    # update screen 
    pygame.display.update()

# x Load Game x #