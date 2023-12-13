import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
COOKIE_RADIUS = 50
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")
clock = pygame.time.Clock()

score = 0

while score < 50:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            distance = ((WIDTH // 2) - x)**2 + ((HEIGHT // 2) - y)**2
            if distance <= COOKIE_RADIUS**2:
                score += 1

    screen.fill(WHITE)

    pygame.draw.circle(screen, BROWN, (WIDTH // 2, HEIGHT // 2), COOKIE_RADIUS)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
