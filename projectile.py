import pygame

#Defini la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/Shoot/6.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 29
        self.rect.y = player.rect.y - 15

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        #Verifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprime le projectile
            self.remove()
            # Infliger des dégats
            monster.damage(self.player.attack)

        #verifier si notre projectile n'est plus présent sur l'écran
        if self.rect.y < -50:
            self.remove()

