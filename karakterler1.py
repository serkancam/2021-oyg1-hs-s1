import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,hiz):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,20))
        self.image.fill(renk)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.speed=hiz
    
    def update(self):
        self.speed=0
        tuslar=pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT]:
            self.speed=-5
        elif tuslar[pygame.K_RIGHT]:
            self.speed=5
        
        self.rect.x+=self.speed
        if self.rect.left>360:
            self.rect.right=0
        elif self.rect.right<0:
            self.rect.left=360

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,renk):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((10,20))
        self.image.fill(renk)
        self.rect = self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speed=-10
    def update(self):
        self.rect.y+=self.speed
        if self.rect.bottom<0:
            self.kill()




        

