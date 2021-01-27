import pygame
from pygame import mixer
import random
import sys

pygame.init()
pygame.font.init()
mixer.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
GRAY = pygame.Color(31, 31, 31)
display_width, display_height = display.get_size()
pygame.display.set_caption('Block dodge')
player_color = (0, 120, 250)
score = 0
lives = 3

orange = (247, 113, 64)
green = (161, 235, 52)
peach = (245, 158, 66)
red = (255, 0, 0)
purple = (99, 20, 255)
grey12 = 'grey12'

air_color = (195, 196, 181)

x = 400
y = 220
x_change = 0
accel_x = 0

accel_y = 0
y_change = 0
max_speed = 7

# bullet 1
x_enemy = 0
rand = -19.9
color = 'grey12'
enemy_accel = 3.6

# bullet2
x_enemy2 = -25
x_enemy21 = 500
rand2 = 599.99
rand21 = 599.99
color2 = 'grey12'
color21 = 'grey12'
enemy_accel2 = 2.5

# bullet3
x_enemy3 = -20
rand3 = 0
color3 = 'grey12'
enemy_accel3 = 15

timer = 0
color4 = 'grey12'
x_warn = -28
Warn_goto = -24

bulletH = 20
bulletW = 40

count = 0

end_timer = 0
cont = True
final_score = "GAME OVER"

bullet_types = "Bullets: Normal"
death = 3

heart1 = pygame.image.load('heart.png')
heart2 = pygame.image.load('heart.png')
heart3 = pygame.image.load('heart.png')
Killer_bullet = pygame.image.load('Bullet.png')
Killer_bullet2 = pygame.image.load('Bullet.png')

x_sprite_bullet = 0
y_sprite_bullet = 0
x_sprite_bullet2 = 0
y_sprite_bullet2 = 0

fire = 0
fire2 = 0
count_b = 0

fade_in = 0
Back_music = mixer.music.load("BackgroundMusic.mp3")

ricochet = pygame.mixer.Sound('Ricochet_sound.mp3')
bounce = pygame.mixer.Sound('Bounce.mp3')
bullet_fire_SFX = pygame.mixer.Sound('BulletSFX.mp3')
bullet_hit = pygame.mixer.Sound('Explode sound effect.mp3')
Countdown = pygame.mixer.Sound('Count_down.mp3')
Countdown.play()
outro = pygame.mixer.Sound('Game_over.mp3')

movement_y = 0
movement_x = 0

intro_timer = 0

count_init = 0

new_x = 0
new_y = 0
new_x2 = 0
new_y2 = 0

const1 = 0
const2 = 0

fast = 0

hits = False
collision_det = False
collision_det2 = False


crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                accel_x = -.2
            if event.key == pygame.K_RIGHT:
                accel_x = .2
            if event.key == pygame.K_UP:
                accel_y = -.2
            if event.key == pygame.K_DOWN:
                accel_y = .2

            if event.key == pygame.K_f:
                count_b += 1
                if x_sprite_bullet == new_x:
                    bullet_fire_SFX.play()
                    const1 = y + 50 + y_change

                if x_sprite_bullet2 == new_x2:
                    bullet_fire_SFX.play()
                    const2 = y - 15 + y_change

                if collision_det == True:
                    count_b = 2
                if collision_det2 == True:
                    fire2 = True

                if count_b % 1 == 0:
                    fire = True
                if count_b % 2 == 0:
                    fire2 = True

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                accel_x = 0
                accel_y = 0

    if fire == True:
        x_sprite_bullet -= 13
        y_sprite_bullet = const1
    if fire == False:
        new_x = x + 10
        new_y = y + 50
        x_sprite_bullet = new_x
        y_sprite_bullet = new_y

    if fire2 == True:
        x_sprite_bullet2 -= 13
        y_sprite_bullet2 = const2
    if fire2 == False:
        new_x2 = x + 10
        new_y2 = y - 15
        x_sprite_bullet2 = new_x2
        y_sprite_bullet2 = new_y2

    mixer.music.set_volume(fade_in)
    fade_in += 0.0017
    timer += 0.02
    levels = round(timer)

    x_round = round(x_change)

    display.fill(grey12)

    if cont == True:
       font = pygame.font.SysFont('Times New Roman', 30)
       text = font.render("Score: " + str(score), True, green)
       textRect = text.get_rect()
       textRect.center = (700, 20)
       display.blit(text, textRect)

       life_font = pygame.font.SysFont('MS Sans Serif', 38)
       lifes = life_font.render("Live's ", True, orange)
       lifeRect = lifes.get_rect()
       lifeRect.center = (455, 22.5)
       display.blit(lifes, lifeRect)

       bullet_combos = pygame.font.SysFont('Verdana', 20)
       bullets = bullet_combos.render(bullet_types, True, purple)
       bulletRect = bullets.get_rect()
       bulletRect.center = (190, 19.8)
       display.blit(bullets, bulletRect)

    if levels <= 7:
        if levels >= 1:
            intro_timer += 0.006
            intro_queue = round(intro_timer)
            intro_font = pygame.font.SysFont('Comic Sans MS', 37)
            text2 = intro_font.render("Game starting in: " + str(3 - intro_queue), True, peach)
            textRect2 = text2.get_rect()
            textRect2.center = (400, 160)
            display.blit(text2, textRect2)

    if levels <= 4:
        mixer.music.play()

    x_change += accel_x
    y_change += accel_y

    if abs(x_change) >= max_speed:
        x_change = x_change / abs(x_change) * max_speed
    if abs(y_change) >= max_speed:
        y_change = y_change / abs(y_change) * max_speed
    if enemy_accel >= 14:
        enemy_accel = enemy_accel / enemy_accel * 14
    if enemy_accel2 >= 12:
        enemy_accel2 = enemy_accel2 / enemy_accel2 * 12
    if enemy_accel3 >= 18:
        enemy_accel3 = enemy_accel3 / enemy_accel3 * 18
    if fade_in >= 1.3:
        fade_in = fade_in / fade_in * 1.3

    if accel_x == 0:
        x_change *= 0.92
    if accel_y == 0:
        y_change *= 0.92

    x += x_change
    y += y_change

    wall1 = pygame.draw.rect(display, grey12, (-13, -100, 15, 800))
    wall2 = pygame.draw.rect(display, grey12, (799, -20, 35, 800))
    wall3 = pygame.draw.rect(display, grey12, (0, 35, 850, 2))
    wall4 = pygame.draw.rect(display, grey12, (0, 595, 830, 35))

    if x_change <= -1:
        movement_x = "right"
    if x_round == 0:
        movement_x = 0

    if movement_x == "right":
        air_11 = pygame.draw.rect(display, air_color, (x + 43, y - 7, 40, 2))
        air_12 = pygame.draw.rect(display, air_color, (x + 43, y + 54, 38, 2))
        air_13 = pygame.draw.rect(display, air_color, (x + 56, y + 40, 40, 2))
        air_14 = pygame.draw.rect(display, air_color, (x + 68, y + 25, 25, 2))
        air_15 = pygame.draw.rect(display, air_color, (x + 56, y + 7, 45, 2))

    sprite = pygame.draw.rect(display, player_color, (x, y, 50, 50))
    if collision_det == False:
        sprite_bullet = pygame.draw.rect(display, (255, 223, 0), (x_sprite_bullet, y_sprite_bullet, 3, 15))
    if collision_det == True:
        sprite_bullet = pygame.draw.rect(display, (255, 223, 0), (0, 0, 3, 15))

    if collision_det2 == False:
        sprite_bullet2 = pygame.draw.rect(display, grey12, (x_sprite_bullet2, y_sprite_bullet2, 3, 15))
    if collision_det2 == True:
        sprite_bullet2 = pygame.draw.rect(display, grey12, (0, 0, 3, 15))

    bullet = pygame.draw.rect(display, color, (x_enemy, rand, bulletW, bulletH))
    bullet2 = pygame.draw.rect(display, color2, (x_enemy2, rand2, 20, 15))
    bullet21 = pygame.draw.rect(display, color21, (x_enemy21, rand21, 20, 15))
    bullet3 = pygame.draw.rect(display, color3, (x_enemy3, rand3, 20, 7))
    warning = pygame.draw.rect(display, color4, (Warn_goto, x_warn, 30, 30))

    if sprite.colliderect(wall1):
        x_change += 400
        bounce.play()
    if sprite.colliderect(wall2):
        x_change -= 400
        bounce.play()

    if sprite.colliderect(wall3):
        y_change += 400
        bounce.play()
    if sprite.colliderect(wall4):
        y_change -= 400
        bounce.play()

    enemy_accel += 0.001
    x_enemy += enemy_accel

    x_enemy3 += 0.01

    if bullet.colliderect(wall2):
        x_enemy = 0
        count_init += 1

    if bullet.colliderect(wall2) and count_init >= 2 and cont == True:
        x_enemy = 0
        count += 1
        color = 'white'
        bulletW = 40
        bulletH = 20

        if True:
            gen = random.randrange(-50, 50)
            rand = y + gen
        if y >= 520:
            rand -= 30
        if y <= 60:
            rand += 30

        if count >= 2:
            score += 1
    if bullet.colliderect(sprite) and cont == True:
        x_enemy = 0
        x_change += 40
        lives -= 1
        rand = random.randint(30, 540)
        ricochet.play()
        hits = True
    if bullet.colliderect(sprite_bullet) and cont == True:
        if True:
            gen = random.randrange(-50, 50)
            rand = y + gen
        if y >= 520:
            rand -= 30
        if y <= 60:
            rand += 30
        bullet_hit.play()
        x_enemy = 0
        score += 2
        collision_det = True
    if bullet.colliderect(sprite_bullet2) and cont == True:
        if True:
            gen = random.randrange(-50, 50)
            rand = y + gen
        if y >= 520:
            rand -= 30
        if y <= 60:
            rand += 30
        bullet_hit.play()
        score += 2
        x_enemy = 0
        collision_det2 = True

    if levels >= 30 and cont == True:
        enemy_accel2 += 0.0001
        x_enemy2 += enemy_accel2
        x_enemy21 -= enemy_accel2
        bullet_types = "Bullets: Normal, Shotgun"

        if bullet2.colliderect(wall2):
            x_enemy2 = 0
            rand2 = random.randint(30, 540)
            color2 = 'yellow'
            score += 1
        if bullet2.colliderect(sprite):
            x_enemy2 = 0
            x_change += 40
            lives -= 1
            rand2 = random.randint(30, 540)
            ricochet.play()
            hits = True
        if bullet2.colliderect(sprite_bullet):
            x_enemy2 = 0
            x_change += 40
            rand2 = random.randint(30, 540)
            bullet_hit.play()
            collision_det = True
        if bullet2.colliderect(sprite_bullet2):
            x_enemy2 = 0
            x_change += 40
            rand2 = random.randint(30, 540)
            bullet_hit.play()
            collision_det2 = True

        if bullet21.colliderect(wall1):
            x_enemy21 = 780
            rand21 = random.randint(30, 540)
            color21 = 'yellow'
            score += 1
        if bullet21.colliderect(sprite):
            x_enemy21 = 780
            x_change -= 40
            lives -= 1
            rand21 = random.randint(30, 540)
            ricochet.play()
            hits = True
        if bullet21.colliderect(sprite_bullet):
            x_enemy21 = 780
            rand21 = random.randint(30, 540)
            bullet_hit.play()
            collision_det = True
        if bullet21.colliderect(sprite_bullet2):
            x_enemy21 = 780
            rand21 = random.randint(30, 540)
            bullet_hit.play()
            collision_det2 = True

    if levels >= 59 and cont == True:
        enemy_accel3 += 0.07
        x_enemy3 += enemy_accel3
        Warn_goto = 0
        bullet_types = "Bullets: Normal, Shotgun, Sniper"

        if bullet3.colliderect(wall2):
            x_enemy3 = 0
            x_warn = y
            rand3 = x_warn + 11
            color3 = 'red'
            color4 = 'red'
            score += 1

        if bullet3.colliderect(sprite):
            x_change += 40
            lives -= 1
            rand3 = x_warn + 11
            x_enemy3 = 0
            ricochet.play()
            hits = True
        if bullet3.colliderect(sprite_bullet):
            rand3 = x_warn + 11
            x_enemy3 = 0
            bullet_hit.play()
            collision_det = True
        if bullet3.colliderect(sprite_bullet2):
            rand3 = x_warn + 11
            x_enemy3 = 0
            bullet_hit.play()
            collision_det2 = True

    death = int(round(lives))

    if death <= 0:
        cont = False

    if cont == False:
        mixer.music.stop()
        rand = 0
        x_enemy = 0
        x_enemy2 = 0
        x_enemy21 = 0
        x_enemy3 = 0
        color = 'grey12'
        color2 = 'grey12'
        color21 = 'grey12'
        color3 = 'grey12'
        color4 = 'grey12'
        x_warn = 0
        Warn_goto = 0
        end_timer += 0.02
        END = round(end_timer)
        if end_timer == 0.02:
            outro.play()

        if END >= 6:
            final_score = "GAME OVER"
        if True:
            END_font = pygame.font.SysFont('CourierBold', 100)
            text3 = END_font.render(str(final_score), True, red)
            textRect3 = text3.get_rect()
            textRect3.center = (410, 200)
            display.blit(text3, textRect3)
        if END >= 15:
            sys.exit()

        final_score = "Final score: " + str(int(score))

    if death == 3:
        display.blit(heart1, (500, 2))
        display.blit(heart2, (545, 2))
        display.blit(heart3, (590, 2))
    elif death == 2:
        display.blit(heart1, (500, 2))
        display.blit(heart2, (545, 2))
    elif death == 1:
        display.blit(heart1, (500, 2))

    if collision_det == False:
        display.blit(Killer_bullet, (x_sprite_bullet - 5, y_sprite_bullet - 1))
    if collision_det2 == False:
        display.blit(Killer_bullet, (x_sprite_bullet2 - 5, y_sprite_bullet2 - 1))

    if hits == True:
        fast += 1
        if fast % 5 == 0:
            player_color = 'grey12'
        if fast % 10 == 0:
            player_color = (0, 120, 250)

        if fast >= 69:
            hits = False
            player_color = (0, 120, 250)
            fast = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
