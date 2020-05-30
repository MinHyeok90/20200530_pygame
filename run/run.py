import random
import pygame
import os

# Default Frame Setting
pygame.init()

screen_width = 480
screen_height = 320
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
character_to_y = 0
character_x_pos = 50
character_y_pos = screen_height - character_height - stage_height
character_jump_power = -1

gravity_speed = 0.05

#block
enemy = pygame.image.load(os.path.join(image_path, "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_to_x = -10
enemy_x_pos = screen_width
enemy_y_pos = random.randint(0, screen_height - enemy_height - stage_height)

# Env
game_font = pygame.font.Font(None, 40)
total_count = 0
start_ticks = pygame.time.get_ticks()
game_result = "GAME OVER"

canSpace = True


# Run
running = True
while running:
    dt = clock.tick(60)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_result = "EXIT"
                running = False
            elif event.key == pygame.K_SPACE and canSpace:
                canSpace = False
                character_to_y = character_jump_power

    
    # Position
    # character
    character_y_pos += character_to_y * dt

    if character_y_pos >= screen_height - character_height - stage_height:
        character_y_pos = screen_height - character_height - stage_height
        canSpace = True
        character_to_y = 0
    else:
        character_to_y += gravity_speed

    # enemy
    enemy_x_pos += enemy_to_x

    if enemy_x_pos < -enemy_width:
        enemy_x_pos = screen_width
        enemy_y_pos = random.randint(0, screen_height - enemy_height - stage_height)

    # Crash
    # character_rect = character.get_rect()
    # character_rect.left = character_x_pos
    # character_rect.top = character_y_pos

    # for ball_idx, ball_val in enumerate(balls):
    #     ball_pos_x = ball_val["pos_x"]
    #     ball_pos_y = ball_val["pos_y"]
    #     ball_img_idx = ball_val["img_idx"]

    #     ball_rect = ball_images[ball_img_idx].get_rect()
    #     ball_rect.left = ball_pos_x
    #     ball_rect.top = ball_pos_y

    #     if character_rect.colliderect(ball_rect):
    #         game_result = "GAME OVER!"
    #         running = False
    #         break
            
        
    # Display
    screen.blit(background, (0, 0))
    screen.blit(stage, (stage_x_pos, stage_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

msg = game_font.render(game_result, True, (255, 0, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# pygame.time.delay(2000)

pygame.display.quit()
pygame.quit()
exit()
