import pygame
from random import randint

#Creer une classe qui gère le projectile du monstre
class Projectile_Monster(pygame.sprite.Sprite):

    def __init__(self,monster):
        super().__init__()
        #definir l'image associé au projectile
        self.image = pygame.image.load("assets/Shoot/monster_shoot.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.velocity = randint(1,3)
        self.monster = monster

    def remove(self):
        self.monster.all_projectiles.remove(self)

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 900:
            #retire le projectile
            self.remove()

        #verifier si la boule de feu touche le joueur
        if self.monster.game.check_collision(self,self.monster.game.all_players):
            #Inflige des dégats
            self.monster.game.player.damage(1)
            #retire le projectile
            self.remove()




