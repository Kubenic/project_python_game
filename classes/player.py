import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        self.position = position

        self.sheet = pygame.image.load('DawnLike/Commissions/Warrior.png');
        self.sheet.set_clip(0, 0, 16, 16)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (0, 16, 16, 16), 1: (16, 16, 16, 16), 2: (32, 16, 16, 16), 3: (48, 16, 16, 16)}
        self.right_states = {0: (0, 32, 16, 16), 1: (16, 32, 16, 16), 2: (32, 32, 16, 16), 3: (48, 32, 16, 16)}
        self.up_states = {0: (0, 48, 16, 16), 1: (16, 48, 16, 16), 2: (32, 48, 16, 16), 3: (48, 48, 16, 16)}
        self.down_states = {0: (0, 0, 16, 16), 1: (16, 0, 16, 16), 2: (32, 0, 16, 16), 3: (48, 0, 16, 16)}

        self.status = "standing"
        self.arm = pygame.image.load('DawnLike/Items/MedWep.png')
        self.arm.set_clip(0, 0, 16, 16)
        self.arm_img = self.arm.subsurface(self.arm.get_clip())
        self.arm_rect = self.image.get_rect()
        self.arm_rect.topleft = tuple(x-y for x, y in zip(position, (20, 0)))

        self.orientation = "left"
        self.monster_pos = ()

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
            self.arm_rect.x -= 5
            self.arm_rect.topleft = tuple(x - y for x, y in zip(self.rect.topleft, (16, 0)))
            self.arm_img = self.arm.subsurface(self.arm.get_clip())

        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
            self.arm_rect.x += 5
            self.arm_rect.topleft = tuple(x - y for x, y in zip(self.rect.topleft, (-16, 0)))
            self.arm_img = pygame.transform.flip(self.arm.subsurface(self.arm.get_clip()), 1, 0)

        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
            self.arm_rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5
            self.arm_rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def set_monster_pos(self, monster_position):
        self.monster_pos = monster_position

    def attack(self):
        self.status = "attacking"

        if self.orientation == "left":
            self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), 40)
        if self.orientation == "right":
            self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), -120)

        posx_width = self.monster_pos.x + self.monster_pos.width
        posy_height = self.monster_pos.y + self.monster_pos.height

        #if self.arm_rect.x > self.monster_pos.x and (self.arm_rect + self.arm_rect.width) < (self.monster_pos.x + self.monster_pos.width):
        print(self.monster_pos.x + self.monster_pos.width)
        print(self.arm_rect)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            # Deplacement
            if event.key == pygame.K_LEFT:
                self.update('left')
                self.orientation = 'left'
            if event.key == pygame.K_RIGHT:
                self.update('right')
                self.orientation = 'right'
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

            # Attack
            if event.key == pygame.K_SPACE:
                self.attack()

        if event.type == pygame.KEYUP:

            # Deplacement
            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')

            # Attack
            if event.key == pygame.K_SPACE:
                self.status = "standing"
                if self.orientation == "left":
                    self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), 0)
                if self.orientation == "right":
                    self.arm_img = pygame.transform.rotate(self.arm.subsurface(self.arm.get_clip()), -90)