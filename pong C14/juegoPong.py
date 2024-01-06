import pygame
import sys

# INICIALIZACION DE PYGAME
pygame.init()

# DEFINICION DE VARIABLES
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 12
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
FPS = 60

#DEFINICION DE COLORes
BLACK = (0, 0, 0)
WHITE = (255 , 255, 255)
RED = (255, 0, 0)

# CONFIGURACION DE LA PANTALLA
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING PONG")
clock = pygame.time.Clock()

textSize = pygame.font.SysFont("Arial", 30)
textPoints = textSize.render("Palsa espacio para jugar",True, (200,200,200), WHITE)
rectTextPresent = textPoints.get_rect()
rectTextPresent.centerx = screen.get_rect().centerx
rectTextPresent.centery = 200

#INICIALIZACION DE POSICIONES Y VELOCIDAD
ball_x = WIDTH/2
ball_y = HEIGHT/2
ball_speed_x = 2
ball_speed_y = 2

paddle1_y = (HEIGHT - PADDLE_HEIGHT)/2
paddle2_y = (HEIGHT - PADDLE_HEIGHT)/2
paddle_speed = 4

# BUCLE PRINCIPAL DEL JUEGO (MIENTRAS)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed 
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed 

    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed 
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += paddle_speed 
        
    #MOVIMIENTO DE LA PELOTA
    ball_x -= ball_speed_x
    ball_y += ball_speed_y

    #REBOTE EN LAS PAREDES SUPERIOR E INFERIOR
    if ball_y <= 1 or ball_y >= 400:
        ball_speed_y = -ball_speed_y

    #REBOTE DE PELOTA
    if(paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT and
       ball_x - BALL_RADIUS <= PADDLE_WIDTH
       ) or (paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT and
       ball_x + BALL_RADIUS >= WIDTH-PADDLE_WIDTH):
        ball_speed_x = -ball_speed_x

    #PUNTUACION
    if (ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH):
        ball_x = WIDTH/2
        ball_y = WIDTH/2
    

    # DIBUJAR ELEMENTOS EN LA PANTALLA
    screen.fill(BLACK)
    pygame.draw.rect(screen,WHITE,(PADDLE_WIDTH, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen,WHITE,(WIDTH - PADDLE_WIDTH * 2, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen,WHITE, (ball_x,ball_y),BALL_RADIUS)

    #actualizar la pantalla
    pygame.display.flip()

    # CONTROLAR LA VELOCIDAD DEL JUEGO 
    clock.tick(FPS)