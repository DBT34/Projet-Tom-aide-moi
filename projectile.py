import pygame


# definir la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur de cette classe
    def __init__(self, player, game):
        super().__init__()
        self.game = game
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('assets/dague.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 50
        self.rect.y = player.rect.y + 150
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner le projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x -= self.velocity
        self.rotate()

        # verifier si le projectile entre en collision avec un autre joueur
        if self.player.game.check_collision(self, self.game.player2):
            # supprimer le projectile
            self.remove()
            # infliger des dégats
            self.game.player2.damage(self.player.attack)


        #verifier si notre projectile n'est plus present sur l'écran
        if self.rect.x > 1080:
            # supprimer le pojectile (en dehors de l'ecran)
            self.remove()
