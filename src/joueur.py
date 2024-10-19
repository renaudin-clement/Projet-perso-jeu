import pygame
from projectile import Projectile

class Playeur(pygame.sprite.Sprite):
    
    def __init__(self,game) -> None:
        super().__init__()
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attaque =10
        self.velocity = 5
        self.image = pygame.image.load("assete/principale/img/player.png")  #image du perso

        
        self.rect = self.image.get_rect() #rectangle autour de l'image
        self.rect.x = 0 # coordonner du rectangle x
        self.rect.y = 970 # coordonner du rectangle Y
        

    def move_right(self):
        if not self.game.check_colision(self,self.game.all_monster):
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity