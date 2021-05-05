import pygame as pg
import sys
import random
ANCHO = 800
ALTO = 600
FPS = 60
class Marcador(pg.sprite.Sprite):
    def __init__(self, x, y, fontsize=25, color=(255,255,255)):
        super().__init__()
        self.fuente = pg.font.SysFont("Arial", fontsize)
        self.text = "0"
        self.color = color
        self.image = self.fuente.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        self.image = self.fuente.render(str(self.text), True, self.color)

class Raqueta(pg.sprite.Sprite):

    disfraces = ['electric00.png', 'electric01.png', 'electric02.png']

    def __init__(self, x, y):
        super().__init__()
        self.imagenes = self.cargaImagenes()
        self.imagen_actual = 0
        self.image = self.imagenes[self.imagen_actual]
        self.rect = self.image.get_rect(centerx = x, bottom = y)
        self.vx = 7

    def cargaImagenes(self):
        imagenes = []
        for fichero in self.disfraces:
            imagenes.append(pg.image.load("./images/{}".format(fichero)))
        return imagenes

    def update(self):
        teclas_pulsadas = pg.key.get_pressed()
        if teclas_pulsadas[pg.K_LEFT]:
            self.rect.x -= self.vx
        if teclas_pulsadas[pg.K_RIGHT]:
            self.rect.x += self.vx
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO
        self.imagen_actual += 1
        if self.imagen_actual >= len(self.disfraces):
            self.imagen_actual = 0
        self.image = self.imagenes[self.imagen_actual]

class Bola(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('./images/ball1.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.vx = random.randint(5, 10) * random.choice([-1, 1])
        self.vy = random.randint(5, 10) * random.choice([-1, 1])
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.vx *= -1 
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.vy *= -1

class Game():

    def __init__(self):
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.botes = 0
        self.todoGrupo = pg.sprite.Group()
        self.cuentaSegundos = Marcador(10,10)
        self.todoGrupo.add(self.cuentaSegundos)
        self.bola = Bola(random.randint(0, ANCHO), random.randint(0, ALTO))
        self.todoGrupo.add(self.bola)    
        self.raqueta = Raqueta(x = ANCHO//2, y = ALTO - 40)
        self.todoGrupo.add(self.raqueta)
        
    def bucle_principal(self):
        game_over = False
        reloj = pg.time.Clock()
        contador_milisegundos = 0
        segundero = 0
        while not game_over: 
            dt = reloj.tick(FPS)
            contador_milisegundos += dt
            if contador_milisegundos >= 1000:
                segundero += 1
                contador_milisegundos = 0
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            self.cuentaSegundos.text = segundero
            self.todoGrupo.update()
            self.pantalla.fill((0,0,0))
            self.todoGrupo.draw(self.pantalla)
            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()


