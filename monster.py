import pygame
from projectile_monster import Projectile_Monster
from random import randint


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.image = pygame.image.load('assets/Ship/jelly.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, 1300)
        self.rect.y = randint(10, 700)
        self.all_monsters = pygame.sprite.Group()
        # ----Attaque du monstre----
        self.percent = 0
        self.percent_speed = 5
        # Defini un groupe de sprite contentant les projectiles
        self.all_projectiles = pygame.sprite.Group()

    def remove(self):
        self.all_monsters.remove(self)

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount
        # verifier si son nouveau nombre de pv est inferieur ou egal à 0
        if self.health <= 0:
            # Reapparaitre l'entité comme un nouveau monstre
            self.game.all_monsters.remove(self)

    def add_percent(self):
        self.percent += 15 / 100

    def launch_projectile(self):
        # Fait apparaitre un projectile
        self.all_projectiles.add(Projectile_Monster(self))

    def shoot(self):
        # Si le pourcentage est supérieur à 100 alors le monstre tire
        if self.percent >= 100:
            self.launch_projectile()
            self.percent = 0
        else:
            self.percent += 15 / 100
