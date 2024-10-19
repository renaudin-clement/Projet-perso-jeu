import pygame
from game import Game


# v1
def init():
    running =True
    pygame.init()
    pygame.display.set_caption("debut slm")
    screen = pygame.display.set_mode((1920,1080))
    background = pygame.image.load("assete/principale/img/fond.png")
    
    game = Game()
    
    while running:
        # mise en plage de larriere plan
        screen.blit(background,(0,0))
        
        # mise en place du joueur
        screen.blit(game.pj.image,game.pj.rect)
        
        screen.blit(game.spotter.image,game.spotter.rect)
        

        
        #ensemble des images des projectiles
        game.spotter.All_projectile.draw(screen)
        
         
        for ball in game.spotter.All_projectile:
            ball.forward()
        
        game.spotter.forward()
        
        if game.spotter.rect.x + game.spotter.rect.width > screen.get_width() -920 or  game.spotter.rect.x < 500:
            game.spotter.inverser_sense()
            
        
        

        #dessine les monstres
        game.all_monster.draw(screen)
        
        #fait avancer tout les monstres
        for monster in game.all_monster:
            monster.forward()
        
        #si le joueur veux aller a gauche ou droit
        if game.pressed.get(pygame.K_RIGHT)and game.pj.rect.x + game.pj.rect.width < (screen.get_width())  :
            game.pj.move_right()
            
        
        if game.pressed.get(pygame.K_LEFT) and  game.pj.rect.x > 0 :
            game.pj.move_left()
            

        
        # raffraichie l'affichage
        pygame.display.flip()
        

        #keydown =appuyer
        #keyup = relacher
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
                print("\n"+"fermeture du jeu"+"\n")
                
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] =True
                
                if event.key == pygame.K_a:
                    #fait avancer tout le spotter
                    game.spotter.launch_projo()
                     
                
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] =False
        
        
init()



