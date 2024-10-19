import pygame

from balle import Ball

class Spotter(pygame.sprite.Sprite):
    
    def __init__(self) -> None:
        super().__init__()
        self.velocity = 5
        self.attaque =5
        self.image = pygame.image.load("assete/principale/img/cercle.png")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 70
        self.avancer = True
        
        self.All_projectile = pygame.sprite.Group()
        
    def forward(self):
        if self.avancer:
            self.rect.x -= self.velocity
        else:
            self.rect.x += self.velocity
            
    def inverser_sense(self):
        self.avancer = not self.avancer
        print(self.avancer)
    
    def launch_projo(self):

        self.All_projectile.add(Ball(self))

    
        
