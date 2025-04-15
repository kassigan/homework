import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# ФПС (количество кадров в секунду)
clock = pygame.time.Clock()
fps = 60

# Used colores
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0) # color of the ball
GREEN = (127, 255, 212) # color Player 2 paddle
DARKORCHID = (153, 50, 204) # color Player 1 paddle
BLACK = (0, 0, 0) # color of the background

# Game window and name of the game
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Ping Pong")

# Класс Ракетки
class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, keys, left_key, right_key):
        if keys[left_key] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[right_key] and self.rect.right < screen_width:
            self.rect.x += self.speed

# Класс Мяча
class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отскок от стен
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def check_collision(self, paddle):
        if paddle.rect.collidepoint(self.x, self.y - self.radius) or paddle.rect.collidepoint(self.x,
                                                                                              self.y + self.radius):
            self.speed_y *= -1


# Создание объектов
paddle1 = Paddle(screen_width // 2 - 50, screen_height - 30, 100, 10, DARKORCHID, 6)
paddle2 = Paddle(screen_width // 2 - 50, 20, 100, 10, GREEN, 6)
ball = Ball(screen_width // 2, screen_height // 2, 8, ORANGE, 4, -4)

# Игровой цикл
run = True
while run:
    clock.tick(fps)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Управление игроками
    paddle1.move(keys, pygame.K_LEFT, pygame.K_RIGHT)  # Игрок 1
    paddle2.move(keys, pygame.K_a, pygame.K_d)         # Игрок 2

    ball.move()
    ball.check_collision(paddle1)
    ball.check_collision(paddle2)

    paddle1.draw(screen)
    paddle2.draw(screen)
    ball.draw(screen)

    # Если мяч улетел за пределы экрана — перезапуск по центру
    if ball.y < 0 or ball.y > screen_height:
        ball.x, ball.y = screen_width // 2, screen_height // 2
        ball.speed_y *= -1

    pygame.display.flip()

pygame.quit()