import random
import pygame

# Default Frame Setting
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Z_Game")

clock = pygame.time.Clock()

# Game Custom Setting
background = pygame.image.load("./background.png")
character = pygame.image.load("./character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 1

ddong = pygame.image.load("./ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0

to_y = 0

ddong_speed = 10

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
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # Character Position
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
        total_count += 1


    # Crash
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("CRASH!")
        running = False
        
    # Display
    screen.blit(background, (0, 0))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))

    counter = game_font.render(str(int(total_count)), True, (255, 255, 255))
    screen.blit(counter, (10, 10))
    pygame.display.update()

pygame.time.delay(2000)

pygame.display.quit()
pygame.quit()
exit()
