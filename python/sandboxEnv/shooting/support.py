import pygame

def draw_text(screen, text, x, y, size, color):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    #位置調整
    x = x - surface.get_width() / 2
    y = y - surface.get_height() / 2
    screen.blit(surface, (x,y))

    