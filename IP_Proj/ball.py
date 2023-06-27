import pygame
import random

# Define the Ball class


class Ball:
    # Set the maximum velocity and the color of the ball
    max_vel = 8
    colour = "RED"

    def __init__(self, x, y, size):

        # Set the initial x and y position of the ball to be the same as its original position
        self.x = self.orig_x = x
        self.y = self.orig_y = y
        self.size = size  # set the size of the ball (radius)

        # Set the initial x and y velocity of the ball to a random value within the maximum velocity

        # either +7 or -7
        self.x_vel = random.choice(
            [-self.max_vel, self.max_vel])
        # random value between +7 and -7
        self.y_vel = random.uniform(-self.max_vel, self.max_vel)

    # Define the move method to update the position of the ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    # Define the draw method to draw the ball on the screen
    def draw(self, disp):
        pygame.draw.circle(disp, self.colour, (self.x, self.y), self.size)

    # Define the reset method to restart the game after a point has been scored
    def reset(self):
        # Reset the position of the ball to its original position
        self.x = self.orig_x
        self.y = self.orig_y

        # Set the new x and y velocity of the ball to a random value within the maximum velocity
        self.x_vel = random.choice([-self.max_vel, self.max_vel])
        self.y_vel = random.uniform(-self.max_vel, self.max_vel)
