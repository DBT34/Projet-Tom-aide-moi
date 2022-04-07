import pygame
import math
from game import Game
from player import Player
from player2 import Player2

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer charger l'arrière plan
background = pygame.image.load('assets/bg.jpg')


# importer notre bannière
banner = pygame.image.load('assets/banner.png')

banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer notre bouton pour lancer la partie
play_button = pygame.image.load('assets/buttonplay.png')
play_button = pygame.transform.scale(play_button, (275, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.80)
play_button_rect.y = math.ceil(screen.get_height() / 1.78)

# importer notre bouton pour changer de classe
play_button2 = pygame.image.load('assets/buttonclasse.png')
play_button2 = pygame.transform.scale(play_button2, (275, 100))
play_button2_rect = play_button2.get_rect()
play_button2_rect.x = math.ceil(screen.get_width() / 2.80)
play_button2_rect.y = math.ceil(screen.get_height() / 1.40)

# charger notre jeu
game = Game()

# charger notre joueur
player = Player(game)

player2 = Player2(game)

running = True

#boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    for projectile2 in game.player2.all_projectiles2:
        projectile2.move()

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    game.player2.all_projectiles2.draw(screen)

    # verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)

        # actualiser la barre de vie du joueur
        game.player.update_health_bar(screen)
        game.player.update_mana_bar(screen)
        game.player2.update_health_bar(screen)
        game.player2.update_mana_bar(screen)


    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        screen.blit(play_button2, play_button2_rect)


    # mettre a jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche 1 est enclenchée pour lancer notre projectile

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile(game)
                game.player.cout()

            if event.key == pygame.K_a:
                game.player2.launch_projectile2(game)
                game.player2.cout()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
             # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode"lancé"
                game.is_playing = True







