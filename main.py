import pygame, sys, random

# Basic Config #
pygame.init()

pygame.display.set_caption('Space Caos')

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode(
  (screen_width,screen_height)
)

clock = pygame.time.Clock()

game_over = False

score = 0
# Basic Config #

# Variables #
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
enemy_size = 50
bomb_size = 10
speed = 10

player_pos = [
  [screen_width/2, screen_height - 100],
  [screen_width/2 - 15, screen_height - 70],
  [screen_width/2 + 15, screen_height - 70]
]

enemy_pos = [
  random.randint(0,screen_width-enemy_size),
  0,
  enemy_size,
  enemy_size
]

bomb_pos = [
  screen_width/2 - 5,
  screen_height-110,
  bomb_size,
  bomb_size
]
# Variables #

# Functions #
def set_level(score, speed):
	pass

def move_enemy():
  pygame.draw.rect(screen, blue, enemy_pos)

  if screen_height > enemy_pos[1] >= 0:
    enemy_pos[1] += speed
  else:
    enemy_pos[0] = random.randint(0,screen_width-enemy_size)
    enemy_pos[1] = 1

def launch_bomb():
  pygame.draw.rect(screen, green, bomb_pos)

  if 0 < bomb_pos[1]:
    bomb_pos[1] -= speed
  else:
    bomb_pos[0] = player_pos[0][0] - 5
    bomb_pos[1] = player_pos[0][1]
  
def spawn_player():
  pygame.draw.polygon(screen, red, player_pos)

def hit():
  pass

def collide():
  pass

def functions():
  set_level()
  spawn_player()
  move_enemy()
  collide()
  launch_bomb()
  hit()
# Functions #

# Run Loop #
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
        player_pos[0][0] -= 30
        player_pos[1][0] -= 30
        player_pos[2][0] -= 30
      elif event.key == pygame.K_RIGHT:
        player_pos[0][0] += 30
        player_pos[1][0] += 30
        player_pos[2][0] += 30
      elif event.key == pygame.K_DOWN:
        player_pos[0][1] += 30
        player_pos[1][1] += 30
        player_pos[2][1] += 30
      elif event.key == pygame.K_UP:
        player_pos[0][1] -= 30
        player_pos[1][1] -= 30
        player_pos[2][1] -= 30

  screen.fill(black)

  functions()

  clock.tick(30)

  pygame.display.update()
# Run Loop #