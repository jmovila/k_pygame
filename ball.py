import pygame as pg
import sys
from random import randint

def rebotaX(x):
    if x <=0 or x>=ANCHO:
        return -1
    return 1

def rebotaY(y):
    if y <=0 or y>=ALTO:
        return -1
    return 1

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()

class Bola():
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color


    


bolas = []

for _ in range(10):
    bola = Bola(randint(0, ANCHO),
        randint(0, ALTO),
        randint(5,10),
        randint(5, 10),
        (randint(0, 255), randint(0, 255), randint(0, 255))
    )

    bolas.append(bola)


game_over = False
while not game_over:
    reloj.tick(60)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    
    for bola in bolas:
        bola.x += bola.vx
        bola.y += bola.vy
    
        bola.vy *= rebotaY(bola.y) 
        bola.vx *= rebotaX(bola.x)


   
     
    
    pantalla.fill(NEGRO)
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
     

    pg.display.flip()

pg.quit()
sys.exit()