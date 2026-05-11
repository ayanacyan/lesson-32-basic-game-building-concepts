import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My first game screen")

BACKGROUND_COLOR = ('aqua')  
RECT_COLOR = (0, 0, 0)   
TEXT_COLOR = ('darkblue')  

font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Aqua game", True, TEXT_COLOR)
text_rect = text_surface.get_rect(center=(screen_width // 2, 100))

rect_width, rect_height = 200, 100
my_rect = pygame.Rect(0, 0, rect_width, rect_height)
my_rect.center = (screen_width // 2, screen_height // 2)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, RECT_COLOR, my_rect)

    screen.blit(text_surface, text_rect)

    
    pygame.display.flip()


pygame.quit()