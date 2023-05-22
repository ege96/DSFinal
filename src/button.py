import pygame


class Button:
    """Button class using images

    Args:
        x (int): x coordinate of the button
        y (int): y coordinate of the button
        image (pygame.Surface): image of the button
        scale (float): scale of the button
    """

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def set_center(self, x, y):
        """Sets the center of the button"""
        self.rect.center = (x, y)

    def draw(self, surface) -> bool:
        """Draws the button on the screen and returns True if the button is clicked

        Args:
            surface (pygame.Surface): surface to draw the button on

        Returns:
            bool: True if the button is clicked, False otherwise
        """
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
