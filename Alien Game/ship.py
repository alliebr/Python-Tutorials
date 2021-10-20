import pygame
 
from pygame.sprite import Sprite
 
class Ship(Sprite):
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # LUCIEN, you can change the image of the ship in here. Try uploading different .bmp files and then changing to code to use them instead. 
        # You could do other files types, like .jpg, .png, or .gif, but that requires other Python libraries that we haven't installed yet
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        # LUCIEN, in order to use a png or jpg in the line above, you have to add the line below in order to scale it properly. I set it to (50,50), but you can change it
        self.image = pygame.transform.scale(self.image, (50, 50))
        # LUCIEN, we use get_rect() below to access the image's rectangle properties. Basically, it acts as through the image had a rectangle around it, which is fine for low detail
        # Once you treat a screen element as a rectangle, you can position it using the top, bottom, left, or right edges of the rectangle
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        # LUCIEN, here you're positioning the ship rectangle (rect) to position is at the middle bottom of the screen (midbottom)
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        # LUCIEN, below we're also using rectangle attributes (rect) to increase or decrease the speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
