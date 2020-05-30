import random
import pygame
import os

# Default Frame Setting
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Z_Game")

clock = pygame.time.Clock()

# Game Custom Setting
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]
stage_x_pos = 0
stage_y_pos = screen_height - stage_height

#Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
character_to_x = 0
character_speed = 1

#Weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

weapons = []
weapon_speed = 10

# Env
game_font = pygame.font.Font(None, 40)

total_count = 0

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(60)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
                print("shoot!")


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        print(event)

    # Position
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons if w[1] > 0]

    # Crash
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # if character_rect.colliderect(ddong_rect):
    #     print("CRASH!")
    #     running = False
        
    # Display
    screen.blit(background, (0, 0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))

    counter = game_font.render(str(int(total_count)), True, (255, 255, 255))
    screen.blit(counter, (10, 10))
    pygame.display.update()

# pygame.time.delay(2000)

pygame.display.quit()
pygame.quit()
exit()
