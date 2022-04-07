import pygame
from player import Player
from player2 import Player2



# creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        # definir si notre jeu a commencer ou non
        self.is_playing = False
        #generer notre joueur
        self.player = Player(self)
        self.player2 = Player2(self)
        self.pressed = {}

    def check_collision(self, sprite1, sprite2):
        return pygame.sprite.collide_mask(sprite1, sprite2)


    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.player2.image, self.player2.rect)

        # actualiser l'animation du joueur
        self.player2.update_animation()
        self.player.update_animation()

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        if self.pressed.get(pygame.K_d) and self.player2.rect.x + self.player2.rect.width < screen.get_width():
            self.player2.move_right()
        elif self.pressed.get(pygame.K_q) and self.player2.rect.x > 0:
            self.player2.move_left()



