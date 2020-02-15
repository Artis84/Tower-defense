# pylint:disable=access-member-before-definition
import pygame
import math

class Enemy:
    imgs = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(25, 334), (116, 335), (226, 339), (302, 337), (299, 256), (305, 196), (383, 197), (434, 193), (439, 125), (524, 118), (637, 117), (710, 116), (711, 208), (712, 258), (778, 266), (842, 
        270), (838, 206), (890, 198), (970, 195), (1048, 195), (1145, 190)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0

    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
    
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y- self.img.get_height()/2 - 35))
        self.move()

    def collide(self, x, y):
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False
    def move(self):
        x1,y1 = self.path[self.path_pos]
        if self.path_pos >= len(self.path):
            x2, y2 = (-10, 355)
        else:
            x2,y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x2) ** 2 + (y2 - y1) ** 2)
        
        self.move_count += 1
        dirn = (x2-x1, y2-y1)

        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((x2-x1)**2 + (y2-y1)**2)

        # Go to next point
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1

        self.x = move_x
        self.y = move_y


    def hit (self):
        self.health -= 1
        if self.health <= 0:
            return True