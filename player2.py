import pygame
from projectile2 import Projectile2
import animation

class Player2(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__("player2")
        self.game = game
        self.health = 300
        self.max_health = 300
        self.max_mana = 300
        self.mana = 300
        self.sort = 25
        self.attack = 10
        self.velocity = 1
        self.all_projectiles2 = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200

    def damage(self, amount):
        # infliger les dégats
        self.health -= amount

        # Verifier si son nouveau nombre de points de vie est inferieur ou egal a 0
        if self.health <=0:
            # Supprimer
            self.image = pygame.image.load('assets/hache.png')

    def cout(self):
        # Retirer du mana a chaque attaque utilisé
        self.mana -= self.sort

    def update_animation(self):
        self.animate()

    def launch_projectile2(self, game):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles2.add(Projectile2(self, game))
        #self demarrer l'animation du lancer
        self.start_animation()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 40, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 40, self.health, 10])

    def update_mana_bar(self, surface):
        # dessiner notre barre de mana
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_mana, 10])
        pygame.draw.rect(surface, (55, 96, 224), [self.rect.x + 10, self.rect.y - 20, self.mana, 10])



    def move_right(self):
        # si le joueur n'est pas en collision avec l'autre joueur
        if not self.game.check_collision(self, self.game.player):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity