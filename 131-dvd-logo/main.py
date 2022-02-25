import pygame, sys
from random import randrange
from debug import debug

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LOGO_WIDTH = 100
LOGO_HEIGHT = 60
FPS = 60


def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def rand_color():
    h = randrange(360)
    return color_hsva(h, 100, 100)


def rainbow(i):
    h = i % 360
    return color_hsva(h, 100, 100)


def color_hsva(h, s, v):
    color = pygame.Color(0, 0, 0)
    color.hsva = (h, s, v)
    return color


# Basic setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DVD Logo")
clock = pygame.time.Clock()

# DVD logo setup
dvd_surf = pygame.image.load("dvd_logo.png").convert_alpha()
fill(dvd_surf, rand_color())
x = randrange(SCREEN_WIDTH - LOGO_WIDTH)
y = randrange(SCREEN_HEIGHT - LOGO_HEIGHT)
dvd_rect = dvd_surf.get_rect(topleft=(x, y))
velx = vely = 1
speed = 2

i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("Black")

    dvd_rect.x += velx * speed
    dvd_rect.y += vely * speed

    hit_left = dvd_rect.left <= 0
    hit_right = dvd_rect.right >= SCREEN_WIDTH
    hit_top = dvd_rect.top <= 0
    hit_bottom = dvd_rect.bottom >= SCREEN_HEIGHT

    if any((hit_left, hit_right, hit_top, hit_bottom)):
        if any((hit_left, hit_right)):
            if hit_left:
                dvd_rect.left = 0
            if hit_right:
                dvd_rect.right = SCREEN_WIDTH
            velx = -velx
        if any((hit_top, hit_bottom)):
            if hit_top:
                dvd_rect.top = 0
            if hit_bottom:
                dvd_rect.bottom = SCREEN_HEIGHT
            vely = -vely
        fill(dvd_surf, rand_color())

    # fill(dvd_surf, rainbow(i))
    screen.blit(dvd_surf, dvd_rect)
    # debug(dvd_rect)

    pygame.display.update()
    clock.tick(FPS)
    i += 1
