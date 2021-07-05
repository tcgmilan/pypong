class PyPong:
    global pygame, random, players, sprite_list, Paddle, Colors, w_width, w_height
    import pygame
    import random
    sprite_list = pygame.sprite.Group()

    class Colors:
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

    class Paddle(pygame.sprite.Sprite):
        def __init__(self, color : tuple, width : int, height : int):
            super().__init__()
            self.pygame = pygame
            self.color = color
            self.width = width
            self.height = height
            self.BLACK = Colors.BLACK
            self.WHITE = Colors.WHITE
            self.image = self.pygame.Surface([self.width, self.height])
            self.image.fill(self.BLACK)
            self.image.set_colorkey(self.BLACK)
            self.pygame.draw.rect(self.image, self.color, [0, 0, width, height])
            self.rect = self.image.get_rect()
        def move_up(self, pixels : int):
            self.rect.y -= pixels
            if self.rect.y < 0:
                self.rect.y = 0
        def move_down(self, pixels : int):
            h = self.pygame.display.get_surface().get_height() - self.height
            self.rect.y += pixels
            if self.rect.y > h:
                self.rect.y = h

    class Ball(pygame.sprite.Sprite):
        def __init__(self, color : tuple, width : int, height : int):
            super().__init__()
            self.pygame = pygame
            self.color = color
            self.BLACK = Colors.BLACK
            self.WHITE = Colors.WHITE
            self.width = width
            self.height = height
            self.sprite_list = sprite_list
            self.image = self.pygame.Surface([self.width, self.height])
            self.image.fill(self.WHITE)
            self.image.set_colorkey(self.BLACK)
            self.pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
            self.velocity = [random.randint(4,8), random.randint(-8, 8)]
            self.rect = self.image.get_rect()
            self.sprite_list.add(self)

        def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
        
        def bounce(self):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = random.randint(-8,8)
            

    class PlayerOne:
        def __init__(self, name : str):
            self.score = 0
            self.name = name
            self.WHITE = Colors.WHITE
            self.sprite_list = sprite_list
            self.player = Paddle(self.WHITE, 10, 100)
            self.player.rect.x = 20
            self.player.rect.y = 200
            self.sprite_list.add(self.player)

    class PlayerTwo:
        def __init__(self, name : str):
            self.score = 0
            self.name = name
            self.WHITE = Colors.WHITE
            self.sprite_list = sprite_list
            self.player = Paddle(self.WHITE, 10, 100)
            self.player.rect.x = 670
            self.player.rect.y = 200
            self.sprite_list.add(self.player)

    def __init__(self):
        self.pygame = pygame
        self.w_width = 700
        self.w_height = 500
        self.title = "PyPong"
        self.pygame.init()

    def play(self, player_one, player_two):
        self.carry_on = True
        self.WHITE = Colors.WHITE
        self.sprite_list = sprite_list
        self.clock = self.pygame.time.Clock()
        self.size = (self.w_width, self.w_height)
        self.screen = self.pygame.display.set_mode(self.size)
        self.pygame.display.set_caption(self.title)
        self.ball = self.Ball(Colors.WHITE, 10, 10)
        while self.carry_on:
            for self.event in self.pygame.event.get():
                if self.event.type == self.pygame.QUIT:
                    self.carry_on = False
            self.sprite_list.update()

            self.keys = self.pygame.key.get_pressed()
            if self.keys[self.pygame.K_w]:
                player_one.player.move_up(5)
            if self.keys[self.pygame.K_s]:
                player_one.player.move_down(5)
            if self.keys[self.pygame.K_UP]:
                player_two.player.move_up(5)
            if self.keys[self.pygame.K_DOWN]:
                player_two.player.move_down(5)

            if self.ball.rect.x >= self.w_width-10:
                self.ball.velocity[0] = -self.ball.velocity[0]
                player_one.score += 1
            if self.ball.rect.x <= 0:
                self.ball.velocity[0] = -self.ball.velocity[0]
                player_two.score += 1
            if self.ball.rect.y >= self.w_height-10:
                self.ball.velocity[1] = -self.ball.velocity[1]
            if self.ball.rect.y <= 0:
                self.ball.velocity[1] = -self.ball.velocity[1]   
            
            if self.pygame.sprite.collide_mask(self.ball, player_one.player) or self.pygame.sprite.collide_mask(self.ball, player_two.player):
                self.ball.bounce()

            self.screen.fill(Colors.BLACK)
            self.pygame.draw.line(self.screen, Colors.WHITE, [round(self.w_width / 2), 0], [round(self.w_width / 2), 500], 5)
            self.sprite_list.draw(self.screen)
            self.font = self.pygame.font.Font(None, 74)
            self.text = self.font.render(str(player_one.score), 1, self.WHITE)
            self.screen.blit(self.text, (round(250), 20))
            self.text = self.font.render(str(player_two.score), 1, self.WHITE)
            self.screen.blit(self.text, (round(420), 20))

            self.font = self.pygame.font.Font(None, 74)
            self.text = self.font.render(str(player_one.name), 1, self.WHITE)
            self.screen.blit(self.text, (round(0), 10))
            self.text = self.font.render(str(player_two.name), 1, self.WHITE)
            self.screen.blit(self.text, (round(self.w_width - len(player_two.name) * 30), 10))
            self.pygame.display.flip()
            self.clock.tick(60)
        self.pygame.quit()