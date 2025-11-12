from circleshape import CircleShape
from constants import *
from logger import log_event
import random
import pygame

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
			asteroid1.velocity = self.velocity.rotate(angle) * 1.2
			angle = random.uniform(20, 50)
			asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
			asteroid2.velocity = self.velocity.rotate(angle)
			log_event("asteroid_split")

