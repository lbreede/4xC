import colorsys
import random
import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


def fill(surface: pygame.Surface, rgb: tuple[float, float, float]) -> None:
    """Fill the surface with the given RGB color, preserving the alpha value.

    Args:
        surface: The surface to fill.
        rgb: The RGB color to fill the surface with.

    """
    width, height = surface.get_size()
    red, green, blue = [int(value * 255) for value in rgb]
    for x in range(width):
        for y in range(height):
            alpha = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(red, green, blue, alpha))


def rand_color() -> tuple[float, float, float]:
    """Return a random RGB color."""
    return colorsys.hsv_to_rgb(random.random(), 1, 1)


def main():
    # Basic setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DVD Logo")
    clock = pygame.time.Clock()

    # DVD logo setup
    dvd_surf = pygame.image.load("dvd_logo.png").convert_alpha()
    logo_width = dvd_surf.get_width()
    logo_height = dvd_surf.get_height()
    fill(dvd_surf, rand_color())
    x = random.randrange(SCREEN_WIDTH - logo_width)
    y = random.randrange(SCREEN_HEIGHT - logo_height)
    dvd_rect = dvd_surf.get_rect(topleft=(x, y))
    velx = vely = 1
    speed = 2

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

        if hit_left:
            dvd_rect.left = 0
            velx = -velx
            fill(dvd_surf, rand_color())

        if hit_right:
            dvd_rect.right = SCREEN_WIDTH
            velx = -velx
            fill(dvd_surf, rand_color())

        if hit_top:
            dvd_rect.top = 0
            vely = -vely
            fill(dvd_surf, rand_color())

        if hit_bottom:
            dvd_rect.bottom = SCREEN_HEIGHT
            vely = -vely
            fill(dvd_surf, rand_color())

        screen.blit(dvd_surf, dvd_rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
