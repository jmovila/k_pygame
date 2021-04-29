import pygame as pg
import sys
from random import randint, choice





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
    def __init__(self, x, y, vx=5, vy=5, color= (255, 255, 255), radio=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radio = radio

    def actualizar(self):

        self.x += self.vx
        self.y += self.vy
        if self.y <=0 or self.y>=ALTO:
            self.vy = -self.vy
        
        if self.x <=0 or self.x>=ANCHO:
            self.vx = -self.vx


    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.radio)
        


bolas = []

for _ in range(10):
    bola = Bola(randint(0, ANCHO),
        randint(0, ALTO),
        randint(5,10)*choice([-1, 1]),
        randint(5, 10)*choice([-1, 1]),
        (randint(0, 255), randint(0, 255), randint(0, 255))
    )

    bolas.append(bola)


game_over = False
while not game_over:
    reloj.tick(60)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    # Modificación de estado
    for bola in bolas:
        bola.actualizar()
    


   
     
    
    pantalla.fill(NEGRO)
    for bola in bolas:
        bola.dibujar(pantalla)
     

    pg.display.flip()

pg.quit()
sys.exit()