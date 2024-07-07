import random
import pygame

pygame.init()

WIN_SIZE = 800
weiss = (255, 255, 255)
rot = (255, 0, 0)
gelb = (255, 255, 0)
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("coinbattle")



Randomsize = list(range(WIN_SIZE)) #Zufällige Koordinaten von Körpern und dem Coin
x_boddy_one = random.choice(Randomsize)
y_boddy_one = random.choice(Randomsize)
x_boddy_two = random.choice(Randomsize)
y_boddy_two = random.choice(Randomsize)
x_coin = random.choice(Randomsize)
y_coin = random.choice(Randomsize)
score_one = 0
score_two = 0
schriftart = pygame.font.SysFont("Arial", 45)


def steuerung(x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two):
    keys = pygame.key.get_pressed() #Steuerung von den Körpern
    if keys[pygame.K_w]:
        y_boddy_one -= 10
    if keys[pygame.K_s]:
        y_boddy_one += 10
    if keys[pygame.K_a]:
        x_boddy_one -= 10
    if keys[pygame.K_d]:
        x_boddy_one += 10
    if keys[pygame.K_UP]:
        y_boddy_two -= 10
    if keys[pygame.K_DOWN]:
        y_boddy_two += 10
    if keys[pygame.K_LEFT]:
        x_boddy_two -= 10
    if keys[pygame.K_RIGHT]:
        x_boddy_two += 10
    return x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two


def kollision(score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two):
    if boddy_one.colliderect(coin): # Nach einer Kollision werden die Koordinaten von den Körpern und dem Coin zufällig generiert
        score_one += 1
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
    elif boddy_two.colliderect(coin):
        score_two += 1
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)
    elif boddy_one.colliderect(boddy_two):
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)




    return score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two

def score(score_one):
    text_one = schriftart.render(f"Score:{score_one}", True, (weiss))
    screen.blit(text_one, (10, 10))
    text_two = schriftart.render(f"Score:{score_two}", True, (weiss))
    screen.blit(text_two, (600,10))




clock = pygame.time.Clock()





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(20)
    clock.tick(60)

    screen.fill((0, 0, 0))

    boddy_one = pygame.draw.rect(screen, (weiss), (x_boddy_one, y_boddy_one, 50, 50))
    boddy_two = pygame.draw.rect(screen, (rot), (x_boddy_two, y_boddy_two, 50, 50))
    coin = pygame.draw.rect(screen, (gelb), (x_coin, y_coin, 50, 50))

    x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two = steuerung(x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two)
    score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two = kollision(score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two)
    score(score_one)




    pygame.display.update()