import pygame

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self,pj) -> None:
        super().__init__()
        self.playeur = pj
        self.velocity = 5
        self.image = pygame.image.load("slm/PygameAssets-main/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = pj.rect.x +120
        self.rect.y = pj.rect.y +80
        
        self.origine_image = self.image
        self.angle = 0
        
    def rotatation(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origine_image,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)
        
     
    def remove_projectiles(self):
        self.playeur.all_projectiles.remove(self)
       
            
    
    def move_projectile(self):
        self.rect.x += self.velocity
        self.rotatation()
        
        #condition si projectile tourche un monstre
        if self.playeur.game.check_colision(self,self.playeur.game.all_monster):
            self.remove_projectiles()
            
        
        #condition si notre projectile est en dehors de la zone
        if self.rect.x > 1060:
            self.remove_projectiles()
