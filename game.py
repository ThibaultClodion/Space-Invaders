import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        #Definit si le jeu commence ou non
        self.is_playing = False
        #Genere le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #Genere le groupe de monstre
        self.monster = Monster(self)
        self.all_monsters = pygame.sprite.Group()
        #Recupere les touches pressées par le joueur
        self.pressed = {}

    def start(self):
        self.is_playing = True
        for _ in range(15):
            self.spawn_monster()

    def game_over(self):
        # remettre le jeu à zéro (retour au menu d'accueil)
        self.all_monsters = pygame.sprite.Group()
        self.player.health = 3
        self.player.rect.x = 650
        self.player.rect.y = 800
        self.is_playing = False

    def update(self, screen):

        # Apply the player
        screen.blit(self.player.image, (self.player.rect))

        # affiche la HealthBar
        screen.blit(pygame.image.load("assets/HUD/HealthBar.png"), (1200, 0))

        # actualise la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #recuperer les projectiles du monstre
        for projectile_monster in self.monster.all_projectiles:
            projectile_monster.fall()

        #actualise les pourcentages du tir des ennemis et tire si nécessaire
        # self.monster.shoot()

        #appliquer l'ensembles des images du proejctiles des monstres
        self.monster.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images du groupe de monstre
        self.all_monsters.draw(screen)

        # Verifie les deplacements du joueur
        if self.pressed.get(pygame.K_z) and not self.pressed.get(pygame.K_d) and not self.pressed.get(
                pygame.K_q) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_s) and not self.pressed.get(pygame.K_d) and not self.pressed.get(
                pygame.K_q) and self.player.rect.y < 825:
            self.player.move_down()
        elif self.pressed.get(pygame.K_d) and not self.pressed.get(pygame.K_s) and not self.pressed.get(
                pygame.K_z) and self.player.rect.x < 1225:
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and not self.pressed.get(pygame.K_z) and not self.pressed.get(
                pygame.K_s) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_d) and self.pressed.get(
                pygame.K_s) and self.player.rect.x < 1225 and self.player.rect.y < 825:
            self.player.move_right_down()
        elif self.pressed.get(pygame.K_z) and self.pressed.get(
                pygame.K_d) and self.player.rect.x < 1225 and self.player.rect.y > 0:
            self.player.move_right_up()
        elif self.pressed.get(pygame.K_z) and self.pressed.get(
                pygame.K_q) and self.player.rect.x > 0 and self.player.rect.y > 0:
            self.player.move_left_up()
        elif self.pressed.get(pygame.K_s) and self.pressed.get(
                pygame.K_q) and self.player.rect.x > 0 and self.player.rect.y < 825:
            self.player.move_left_down()

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

