import pygame


class Ball(pygame.sprite.Sprite):
    
    def __init__(self,Spotter) -> None:
        super().__init__()
        self.velocity = 20
        self.attaque =5
        self.spot = Spotter
        self.image = pygame.image.load("assete/principale/img/ball.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = self.spot.rect.x
        self.rect.y = self.spot.rect.y
        self.avancer = True
        self.origine_image = self.image

        self.angle = 0
        
    def forward(self):
        if self.avancer:
            self.rect.y += self.velocity
            self.rotatation()
        else:
            self.rect.y -= self.velocity
            self.rotatation()
        if  self.rect.y > 1000 or self.rect.x > 1080:
            self.remove_projectiles()
            
    def inverser_sense(self):
        self.avancer = not self.avancer
        print(self.avancer)
    
        
    def rotatation(self):
        
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origine_image,self.angle,1)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(center = self.rect.center)

        
    def remove_projectiles(self):
        print( self.spot.All_projectile)
        self.spot.All_projectile.remove(self)
        print( self.spot.All_projectile)