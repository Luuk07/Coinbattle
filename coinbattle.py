import random
import pygame

pygame.init()

WIN_SIZE = 800
weiss = (255, 255, 255)
rot = (255, 0, 0)
gelb = (255, 255, 0)
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
pygame.display.set_caption("coinbattle")
speed_one_x = 10
speed_one_y = 10
speed_two_x = 10
speed_two_y = 10
keys = pygame.key.get_pressed() #Steuerung von den Körpern




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
schriftart_two = pygame.font.SysFont("Arial", 25)


def steuerung(x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two):
    keys = pygame.key.get_pressed()  # Steuerung von den Körpern
    if keys[pygame.K_w]:
        y_boddy_one -= speed_one_y
    if keys[pygame.K_s]:
        y_boddy_one += speed_one_y
    if keys[pygame.K_a]:
        x_boddy_one -= speed_one_x
    if keys[pygame.K_d]:
        x_boddy_one += speed_one_x
    if keys[pygame.K_UP]:
        y_boddy_two -= speed_two_y
    if keys[pygame.K_DOWN]:
        y_boddy_two += speed_two_y
    if keys[pygame.K_LEFT]:
        x_boddy_two -= speed_two_x
    if keys[pygame.K_RIGHT]:
        x_boddy_two += speed_two_x
    return x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two


def kollision(score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y):
    if boddy_one.colliderect(coin): # Nach einer Kollision werden die Koordinaten von den Körpern und dem Coin zufällig generiert
        score_one += 1
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
        speed_two_x -= 1
        speed_two_y -= 1
        speed_one_x += 1
        speed_one_y += 1


    elif boddy_two.colliderect(coin):
        score_two += 1
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)
        speed_two_x += 1
        speed_two_y += 1
        speed_one_x -= 1
        speed_one_y -= 1

    elif boddy_one.colliderect(boddy_two):
        x_coin = random.choice(Randomsize)
        y_coin = random.choice(Randomsize)
        x_boddy_two = random.choice(Randomsize)
        y_boddy_two = random.choice(Randomsize)
        x_boddy_one = random.choice(Randomsize)
        y_boddy_one = random.choice(Randomsize)




    return score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y

def score():
    text_one = schriftart.render(f"Score:{score_one}", True, (weiss))
    screen.blit(text_one, (10, 10))
    text_two = schriftart.render(f"Score:{score_two}", True, (weiss))
    screen.blit(text_two, (600,10))

def check_win(score_one, score_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y):
    keys = pygame.key.get_pressed()  # Steuerung von den Körpern
    if score_one == score_two + 10:
        speed_one_x = 0
        speed_one_y = 0
        speed_two_x = 0
        speed_two_y = 0
        win_text_one = schriftart_two.render("Spieler 1 hat gewonnen! 1 = Abbrechen, 2 = weiter spielen", True, (0, 255, 0))
        screen.blit(win_text_one, (50, 300))
        if keys[pygame.K_1]:
            run = False
        elif keys[pygame.K_2]:
            speed_one_x = 10
            speed_one_y = 10
            speed_two_x = 10
            speed_two_y = 10
            score_one = 0
            score_two = 0


    if score_two == score_one + 10:
        speed_one_x = 0
        speed_one_y = 0
        speed_two_x = 0
        speed_two_y = 0
        win_text_two = schriftart_two.render("Spieler 2 hat gewonnen! 1 = Abbrechen, 2 = weiter spielen", True, (0, 255, 0))
        screen.blit(win_text_two, (50, 300))
        if keys[pygame.K_1]:
            run = False
        elif keys[pygame.K_2]:
            speed_one_x = 10
            speed_one_y = 10
            speed_two_x = 10
            speed_two_y = 10
            score_one = 0
            score_two = 0

    return speed_one_x, speed_one_y, speed_two_x, speed_two_y, score_one, score_two





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
    score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y = kollision(score_one, score_two, x_coin, y_coin, x_boddy_one, y_boddy_one, x_boddy_two, y_boddy_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y)
    score()
    speed_one_x, speed_one_y, speed_two_x, speed_two_y, score_one, score_two = check_win(score_one, score_two, speed_one_x, speed_one_y, speed_two_x, speed_two_y)




    pygame.display.update()
