import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('DawnLike/Characters/Undead0.png');
        self.sheet.set_clip(0, 0, 16, 16)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = {0: (0, 16, 16, 16), 1: (16, 16, 16, 16), 2: (32, 16, 16, 16), 3: (48, 16, 16, 16)}
        self.right_states = {0: (0, 32, 16, 16), 1: (16, 32, 16, 16), 2: (32, 32, 16, 16), 3: (48, 32, 16, 16)}
        self.up_states = {0: (0, 48, 16, 16), 1: (16, 48, 16, 16), 2: (32, 48, 16, 16), 3: (48, 48, 16, 16)}
        self.down_states = {0: (0, 0, 16, 16), 1: (16, 0, 16, 16), 2: (32, 0, 16, 16), 3: (48, 0, 16, 16)}

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

    def moove(self):
        # Before main loop
        human_files = ["human1.png", "human2.png"]
        human_sprites = [pygame.image.load(filename).convert_alpha() for filename in human_files]
        human1_index = 0

        ...

        # During main loop
        if (human1_position.left <= 555):
            human1_position = human1_position.move(2, 0)  # move first human
            human1_index = (human_index + 1) % len(human_sprites)  # change sprite
        else:
            move = STOP
            human1_index = 0
        human1 = human_sprites[human1_index]
        screen.blit(human1, human1_position)
        pygame.display.update()