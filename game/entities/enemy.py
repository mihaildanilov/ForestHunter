import pygame


class Enemy():
    MAX_HEALTH_BAR_WIDTH = 50

    def __init__(
            self,
            x,
            y,
            enemy_width,
            enemy_height,
            end,
            hitbox_width,
            hitbox_height,
            sprites,
            enemyType='first',
            health=10):
        self.x = x
        self.y = y
        self.width = enemy_width
        self.height = enemy_height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, hitbox_width, hitbox_height)
        self.health = health
        self.start_health = health
        self.visible = True
        self.enemyType = enemyType
        self.enemy_sprites = sprites[self.enemyType]
        self.walkRight = self.enemy_sprites['right']
        self.walkLeft = self.enemy_sprites['left']
        self.hitbox_width = hitbox_width
        self.hitbox_height = hitbox_height

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 24:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            # Calculate health bar position
            health_bar_x = self.x + self.width // 2 - Enemy.MAX_HEALTH_BAR_WIDTH // 2
            health_bar_y = self.y - 20  # 20 pixels above the enemy

            # Draw health bars
            pygame.draw.rect(
                win,
                (255,
                 0,
                 0),
                (health_bar_x,
                 health_bar_y,
                 Enemy.MAX_HEALTH_BAR_WIDTH,
                 10))  # Red bar
            pygame.draw.rect(win, (0, 128, 0), (health_bar_x, health_bar_y, int(
                Enemy.MAX_HEALTH_BAR_WIDTH * (self.health / self.start_health)), 10))  # Green bar

            self.hitbox = (self.x, self.y, self.hitbox_width,
                           self.hitbox_height)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # HITBOX

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        # print('hit')

    def hit(self, bullets):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            for bullet in bullets:
                bullets.remove(bullet)
        pass
