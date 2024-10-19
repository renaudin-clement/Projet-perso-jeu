from joueur import Playeur
from monster import Monster
from spotter import Spotter
import pygame

class Game:
    
    def __init__(self) -> None:
        self.all_player = pygame.sprite.Group()
        self.pj =Playeur(self)
        self.all_player.add(self.pj)
        
        self.spotter = Spotter()
        #definir un groupe de monstre
        self.all_monster = pygame.sprite.Group()
        #cree un dictionnaire des touche presser
        self.pressed = {            
        }
        
        
        
        self.spawn_mommie()
        
    def check_colision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
        
    def spawn_mommie(self):
        monster = Monster(self)
        self.all_monster.add(monster)