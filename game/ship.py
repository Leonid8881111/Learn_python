import pygame
class Ship():
             def __init__(self, ai_game):
               self.screen = ai_game.screen
               self.settings = ai_game.settings
               self.x = float(self.rect.x)
               self.screen_rect = ai_game.screen.get_rect()
               self.image = pygame.image.load('images/pixil-frame-0 (1).bmp')
               self.rect = self.image.get_rect()
               self.rect.midbottom = self.screen_rect.midbottom
               self.moving_right = False
               self.moving_left = False
               def update(self):
                 if self.moving_right and self.rect.right < self.screen_rect.right:
                    self.x += self.settings.ship_speed
                 if self.moving_left and self.rect.left > 0:
                    self.x -= self.settings.ship_speed
                    self.rect.x = self.x
                 if self.moving_right:
                   self.rect.x += 1
                   if self.moving_left:
                      self.rect.x -= 1
def blitme(self):
    self.screen.blit(self.image,self.rect)