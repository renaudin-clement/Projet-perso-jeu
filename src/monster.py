import pygame

class Monster(pygame.sprite.Sprite):
    
    def __init__(self,game) -> None:
        super().__init__()
        self.gamee = game
        
        self.healt = 100
        self.healt_max =100
        self.velocity = 2
        self.attaque =5
        self.image = pygame.image.load("assete/principale/img/enemie.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1900
        self.rect.y = 970
        
    def forward(self):
        if not self.gamee.check_colision(self,self.gamee.all_player):
            self.rect.x -= self.velocity
        
        if  self.gamee.check_colision(self,self.gamee.all_player):
            self.rect.x += self.velocity