import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
SANTA_SIZE = 50
PACKAGE_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Santa's Delivery Game")
clock = pygame.time.Clock()

santa_x = WIDTH // 2 - SANTA_SIZE // 2
santa_y = HEIGHT - SANTA_SIZE - 10

package_x = random.randint(0, WIDTH - PACKAGE_SIZE)
package_y = 0

santa_speed = 5
package_speed = 5

score = 0

while score < 15:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and santa_x > 0:
        santa_x -= santa_speed
    if keys[pygame.K_RIGHT] and santa_x < WIDTH - SANTA_SIZE:
        santa_x += santa_speed

    package_y += package_speed

    if package_y > HEIGHT:
        package_x = random.randint(0, WIDTH - PACKAGE_SIZE)
        package_y = 0

    if santa_x < package_x < santa_x + SANTA_SIZE and santa_y < package_y < santa_y + SANTA_SIZE:
        package_x = random.randint(0, WIDTH - PACKAGE_SIZE)
        package_y = 0
        score += 1

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (santa_x, santa_y, SANTA_SIZE, SANTA_SIZE))
    pygame.draw.rect(screen, (0, 255, 0), (package_x, package_y, PACKAGE_SIZE, PACKAGE_SIZE))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
