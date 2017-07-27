import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, position):
        self.position = position
        self.pos = 0
        self.arrayPosition = ['left', 'right', 'up', 'down']
        self.sheet = pygame.image.load('DawnLike/Commissions/Paladin.png');
        self.sheet.set_clip(0, 0, 16, 16)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (0, 16, 16, 16), 1: (16, 16, 16, 16), 2: (32, 16, 16, 16), 3: (48, 16, 16, 16)}
        self.right_states = {0: (0, 32, 16, 16), 1: (16, 32, 16, 16), 2: (32, 32, 16, 16), 3: (48, 32, 16, 16)}
        self.up_states = {0: (0, 48, 16, 16), 1: (16, 48, 16, 16), 2: (32, 48, 16, 16), 3: (48, 48, 16, 16)}
        self.down_states = {0: (0, 0, 16, 16), 1: (16, 0, 16, 16), 2: (32, 0, 16, 16), 3: (48, 0, 16, 16)}

        self.lifepoint = 20

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def attack(self):
        self.status = "attacking"

        if self.orientation == "left":
            self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), 40)
        if self.orientation == "right":
            self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), -120)

    def move(self):
        if (random.randrange(0, 10, 1) > 6):
            self.pos = random.randrange(0, 3, 1)

        self.update(self.arrayPosition[self.pos])
        self.orientation = self.arrayPosition[self.pos]
        self.update(self.arrayPosition[self.pos]+'_left')