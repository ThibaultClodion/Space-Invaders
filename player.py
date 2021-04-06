import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 3
        self.max_health = 3
        self.attack = 1
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/Ship/2.png')
        self.image = pygame.transform.scale(self.image, (75,75))
        self.rect = self.image.get_rect()
        self.rect.x = 650
        self.rect.y = 800

    def damage(self, amount):
        if self.health >= 1:
            self.health -= amount
        elif self.health <= 0:
            #si le joueur n'as plus de point de vie
            self.game.game_over()

    def update_health_bar(self,surface):
        if self.health == 3:
            self.health_bar = pygame.image.load('assets/HUD/HealthBarColor.png')
        elif self.health == 2:
            self.health_bar = pygame.transform.scale(self.health_bar,(53,18))
        elif self.health == 1:
            self.health_bar = pygame.transform.scale(self.health_bar,(26, 18))
        elif self.health == 0:
            self.health_bar = pygame.transform.scale(self.health_bar,(0, 18))
        surface.blit(self.health_bar,(1209,8))

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))


    def move_up(self):
        #si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.rect.y -= self.velocity

    def move_down(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.rect.y += self.velocity

    def move_left(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.rect.x -= self.velocity

    def move_right(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.rect.x += self.velocity

    def move_right_down(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.move_down()
            self.move_right()

    def move_right_up(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.move_right()
            self.move_up()

    def move_left_up(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.move_left()
            self.move_up()

    def move_left_down(self):
        # si le joueur entre en collision avec une entité monstre
        if self.game.check_collision(self, self.game.all_monsters):
            self.damage(1)
            self.rect.y += 20
        else:
            self.move_down()
            self.move_left()