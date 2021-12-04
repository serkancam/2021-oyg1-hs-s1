import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,hiz):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill(renk)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hiz=hiz
    def update(self):
        self.rect.x+=self.hiz
        if self.rect.left>360:
            self.rect.right=0
class Mob(pygame.sprite.Sprite):
    def __init__(self,x,y,renk,hiz):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill(renk)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.hiz=hiz
    def update(self):
        tus_bilgisi=pygame.key.get_pressed()

        if tus_bilgisi[pygame.K_LEFT]:
            self.rect.x-=5
        elif tus_bilgisi[pygame.K_RIGHT]:
            self.rect.x+=5
        
        
