import pygame
from random import randint, uniform
from pygame.sprite import Sprite


class Star(Sprite):
    """Class to define and randomize star appearance"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load star image
        self.image = pygame.image.load('images/star.bmp')

        # Scale down star size randomly and rotate randomly
        self.image = pygame.transform.scale(self.image, (

            ai_game.settings.screen_width // 36,
            ai_game.settings.screen_height // 20
        ))

        self.rect = self.image.get_rect()

        # Start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position
        self.x = float(self.rect.x)

    def randomize_star_specs(self, ai_game):
        """Change the scale of the star and rotate it"""
        x_proportion = randint(100,250)
        y_proportion = x_proportion // 1.8
        
        # Randomize size of star (proportionally)
        self.image = pygame.transform.scale(self.image, (

            ai_game.settings.screen_width // x_proportion,
            ai_game.settings.screen_height // y_proportion
        ))
        
        #self.image = pygame.transform.rotate(self.image, randint(0, 60))

    def blitme(self):
        """Draw star at its position"""
        self.screen.blit(self.image, self.rect)
