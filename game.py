import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Z_Game")

background = pygame.image.load("./background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)

    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.display.quit()
pygame.quit()
exit()
