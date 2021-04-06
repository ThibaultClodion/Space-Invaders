import pygame
from game import Game

#---Pygame---
pygame.init()

#--Music--
pygame.mixer.music.load("assets/music_theme/C_I_theme.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0)

#---Fenêtre de jeu----
pygame.display.set_caption("Space Invader")
screen = pygame.display.set_mode((1300, 900))

#--Image--
#Background
background = pygame.image.load('assets/Background/3b.png')
background = pygame.transform.scale(background, (1300, 900))

#Importer notre bannière
play_button = pygame.image.load('assets/PNG/Main_Menu/Start_BTN.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() // 3
play_button_rect.y = screen.get_width() // 3

#Charger notre jeu
game = Game()


#--Start the Game--
running = True

#Game's loop

while running:

    #Apply the background
    screen.blit(background,(0,0))

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        #Declenche les instructions de la partie
        game.update(screen)
    else:
        #Ajoute l'écran de bienvenue
        screen.blit(play_button,(play_button_rect))


    #Update the window
    pygame.display.flip()

    #close the window
    for event in pygame.event.get():
        #vérifier que l'on ferme la fenetre:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Jeu fini")
        #detecter si le joueur utilise une touche du clavier
        elif event.type == pygame.KEYDOWN:
            #Verifie si une touche du clavier pressé
            game.pressed[event.key] = True
            # Genere le tir du joueur si espace est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            #Verifie si une touche n'est plus pressé
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Vérifie si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #Lance le jeu
                game.start()



