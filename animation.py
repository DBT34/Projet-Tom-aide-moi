import pygame
import pygame.time

# definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la création du joueur
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations["playerr"] #.get(sprite_name)
        self.animation = False

    # definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:

            # passer à l'image suivante
            self.current_image += 0.07

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image de l'animation précedente par la suivante
            self.image = self.images[int(self.current_image)]


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images de ce sprite dnas le dossier correspondant
    images = []
    # recuperer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image dans ce dossier
    for num in range(1, 7):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# playerr -> [...playerr1.png, ...playerr2.png, ...]
animations = {
    'playerr': load_animation_images('playerr')
}

