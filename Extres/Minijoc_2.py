import pygame
import random

# Inicialitzar pygame
pygame.init()

# Configurar la finestra
ample_finestra = 800
alt_finestra = 600
finestra = pygame.display.set_mode((ample_finestra, alt_finestra))
pygame.display.set_caption("Minijoc: Evita les boles!")

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERD = (0, 255, 0)
GROC = (255, 255, 0)

# Configuració del jugador
player_width = 50
player_height = 50
player_x = ample_finestra // 2 - player_width // 2
player_y = alt_finestra - player_height - 10
player_speed = 10

# Configuració de les boles
bola_width = 30
boles = []
bola_speed = 5
for _ in range(5):
    bola_x = random.randint(0, ample_finestra - bola_width)
    bola_y = random.randint(-150, -30)
    boles.append([bola_x, bola_y])

# Joc
joc_en_curs = True
while joc_en_curs:
    for esdeveniment in pygame.event.get():
        if esdeveniment.type == pygame.QUIT:
            joc_en_curs = False

    # Control del jugador
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if tecles[pygame.K_RIGHT] and player_x < ample_finestra - player_width:
        player_x += player_speed

    # Actualitzar la posició de les boles
    for bola in boles:
        bola[1] += bola_speed
        if bola[1] > alt_finestra:
            bola[0] = random.randint(0, ample_finestra - bola_width)
            bola[1] = random.randint(-150, -30)

    # Comprovar col·lisions
    for bola in boles:
        if (player_x < bola[0] + bola_width and
            player_x + player_width > bola[0] and
            player_y < bola[1] + bola_width and
            player_y + player_height > bola[1]):
            print("Has perdut!")
            joc_en_curs = False

    # Dibuixar
    finestra.fill(BLANC)
    pygame.draw.rect(finestra, VERD, (player_x, player_y, player_width, player_height))
    for bola in boles:
        pygame.draw.circle(finestra, GROC, (bola[0] + bola_width // 2, bola[1] + bola_width // 2), bola_width // 2)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
