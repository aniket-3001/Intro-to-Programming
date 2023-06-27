import pygame

# Define the paddle class


class Paddle:
    # Set the paddle velocity and the color of the paddle
    vel = 10
    colour = "BLUE"

    def __init__(self, x, y, wd, ht):

        # Set the initial x and y position of the paddle to be the same as its original position
        self.orig_x = x
        self.x = self.orig_x  # x position of the paddle
        self.orig_y = y
        self.y = self.orig_y  # y position of the paddle
        self.ht = ht  # ht of the paddle
        self.wd = wd  # wd of the paddle

    # method to move the paddle up or down
    def move(self, dir):  # Moves the paddle up or down
        if dir == "up":
            self.y -= self.vel  # move the paddle up
        else:
            self.y += self.vel  # move the paddle down

    # method to draw the paddle on the disp
    def draw(self, disp):
        pygame.draw.rect(
            disp, self.colour, (self.x, self.y, self.wd, self.ht))

    # method to reset the paddle to its original position
    def reset(self):
        self.x = self.orig_x  # set x position to original position
        self.y = self.orig_y  # set y position to original position
