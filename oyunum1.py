#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
import random
import time
import locale
from karakterler1 import Bullet, Player
# locale.setlocale(locale.LC_ALL,'tr_TR.utf8')


# Renk tanımları
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE1 = (15, 69, 75)
BLUE2 = (106, 144, 147)

# Ekran değerleri ayarla
WIDTH = 360
HEIGHT = 480
FPS = 30
CAPTION = "Oyunum"
running = False
skorY = 0
skorK = 0
# Pygame başlangıç ayarları ve pencere oluşturma
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Classes/ oyunda kullanılacak sınıflar

# functions/Oyunda kullanılcak Fonksiyonlar

# Game loop/oyun döngüsü


def oyun():
    # oyunda kullanılacak nesnelerin ilk başlatılması oyunda kullanışacak değişkenler
    p1 = Player(int(WIDTH/2), HEIGHT-40, MAROON, 5)
    pg = pygame.sprite.Group()
    bg = pygame.sprite.Group()
    pg.add(p1)
    

    global running
    running = True
    while running:
        # keep loop running at the right speed
        # oyun hızının ayarlanması
        clock.tick(FPS)
        # Process inputs(events)--1
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                print("Oyun Kapatıldı")
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    blt = Bullet(p1.rect.centerx,p1.rect.top,YELLOW)
                    pg.add(blt)
                    bg.add(blt)
        # update
        # Oyunda kullanılan nesnelerin değerlerinin değiştirilmesi x,y ses, renk vb
        pg.update()
        ##draw / render--3
        
        # oyunda kullanılacak nesnelerin güncellenmiş değelere göre çizilmesi
        screen.fill(BLACK)
        pg.draw(screen)

        # ekranın tekrar yeni çizimler ile güncellenmesi
        pygame.display.update()  # pygame.display.flip()


    # pygame.quit()
if __name__ == "__main__":
    oyun()
    pygame.quit()
