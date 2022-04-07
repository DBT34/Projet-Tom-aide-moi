import pygame

# definir la classe qui va gerer le projectile de notre joueur
class Projectile2(pygame.sprite.Sprite):

    def __init__(self, player2, game):
        super().__init__()
        self.game = game
        self.velocity = 3
        self.player2 = player2
        self.image = pygame.image.load('assets/hache.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player2.rect.x + 200
        self.rect.y = player2.rect.y + 150
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += -3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player2.all_projectiles2.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        if self.player2.game.check_collision(self, self.game.player):
            # supprimer le projectile
            self.remove()
            self.game.player.damage(self.player2.attack)

        # verifier si notre projectile n'est plus present sur l'écran
        if self.rect.x > 1080:
            # supprimer le pojectile (en dehors de l'ecran)
            self.remove()