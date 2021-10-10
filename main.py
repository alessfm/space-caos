import pygame, sys, random

# Basic Config #

pygame.init()

pygame.display.set_caption('Space Caos')

#icon = pygame.image.load('logo.png')

#pygame.display.set_icon(icon)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode(
  (screen_width,screen_height)
  )

# Basic Config #

# Variables #

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
enemy_size = 50
speed = 10

player_spawn = [
  [screen_width/2, screen_height - 100],
  [screen_width/2 - 15, screen_height - 70],
  [screen_width/2 + 15, screen_height - 70]
]

enemy_spawn = [
  random.randint(0,screen_width-enemy_size),
  0,
  enemy_size,
  enemy_size
]

# Variables #

# Run Loop #

game_over = False

clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():    
    
    if event.type == pygame.QUIT:
      sys.exit()
    
    if event.type == pygame.KEYDOWN:
      """
      for left/right, move only X
      for up/down, move only Y
      """
      if event.key == pygame.K_LEFT:
        player_spawn[0][0] -= 30
        player_spawn[1][0] -= 30
        player_spawn[2][0] -= 30
      elif event.key == pygame.K_RIGHT:
        player_spawn[0][0] += 30
        player_spawn[1][0] += 30
        player_spawn[2][0] += 30
      elif event.key == pygame.K_DOWN:
        player_spawn[0][1] += 30
        player_spawn[1][1] += 30
        player_spawn[2][1] += 30
      elif event.key == pygame.K_UP:
        player_spawn[0][1] -= 30
        player_spawn[1][1] -= 30
        player_spawn[2][1] -= 30
    
    screen.fill(black)
    
    if screen_height > enemy_spawn[1] >= 0:
      enemy_spawn[1] += speed
    else:
      enemy_spawn[0] = random.randint(0,screen_width-enemy_size)
      enemy_spawn[1] = 1

    pygame.draw.rect(screen, blue, enemy_spawn)
    pygame.draw.polygon(screen, red, player_spawn)
    
    clock.tick(30)

    pygame.display.update()
