import pygame
from projectile import Projectile
import animation2

# creer une premiere classe qui va représenter notre joueur
class Player(animation2.AnimateSprite):

    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 300
        self.mana = 300
        self.max_health = 300
        self.max_mana = 300
        self.sort = 25
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 760
        self.rect.y = 200

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount

    def cout(self):
        # Retirer du mana a chaque attaque utilisé
        self.mana -= self.sort


    def launch_projectile(self, game):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self, game))

        self.start_animation()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 40, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 40, self.health, 10])


    def update_mana_bar(self, surface):
        # dessiner notre barre de mana
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_mana, 10])
        pygame.draw.rect(surface, (55, 96, 224), [self.rect.x + 10, self.rect.y - 20, self.mana, 10])



    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        if not self.game.check_collision(self, self.game.player2):
            self.rect.x -= self.velocity

