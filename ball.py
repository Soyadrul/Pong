import pygame
import math
import random
from score import Score
from player import Player

class Ball:
	
	def __init__(self, window, max_frames, center, radius):
		self.__window = window
		self.__starting_center = center
		self.__center = center
		self.__radius = radius
		self.__color = None
		self.__move = False
		self.__player_collision_happened = False
		self.__x_velocity = None
		self.__y_velocity = None
		self.__max_frames_times_velocity = 280
		self.__velocity = self.__max_frames_times_velocity / max_frames
		
	def draw(self, color):
		self.__color = color
		pygame.draw.circle(self.get_window(), self.get_color(), self.get_center(), self.get_radius())
		
	def move(self):
		if (not self.is_moving()):
			self.__move = True
			
			
			self.set_x_velocity( int(random.choice(['-1', '+1']))*random.uniform(0.32*self.get_velocity(), 0.95*self.get_velocity()) )
			self.set_y_velocity( int(random.choice(['-1', '+1']))*math.sqrt( self.get_velocity()**2 - self.get_x_velocity()**2 ) )
			
			new_center = ( (self.get_center())[0]+self.get_x_velocity(), (self.get_center())[1]+self.get_y_velocity() )
			
			self.set_center(new_center)
		else:
			new_center = ( (self.get_center())[0]+self.get_x_velocity(), (self.get_center())[1]+self.get_y_velocity())
			self.set_center(new_center)
	
	#return True if there is a collision (and changes the trajectory of the ball), False otherwise
	def check_collision(self, left_player, right_player, left_score, right_score):
		x_center = (self.get_center())[0]
		y_center = (self.get_center())[1]
		
		#check if the ball is colliding with the right part of left player
		if ( left_player.collidepoint(x_center - self.get_radius(), y_center) ):
			self.set_x_velocity( - self.get_x_velocity() )
			if (not self.__player_collision_happened):
				self.__player_collision_happened = True
				self.set_x_velocity(2*self.get_x_velocity())
				self.set_y_velocity(2*self.get_y_velocity())
			return True
		
		#check if the ball is colliding with the left part of right player
		elif ( right_player.collidepoint(x_center + self.get_radius(), y_center) ):
			self.set_x_velocity( - self.get_x_velocity() )
			if (not self.__player_collision_happened):
				self.__player_collision_happened = True
				self.set_x_velocity(2*self.get_x_velocity())
				self.set_y_velocity(2*self.get_y_velocity())
			return True
				
		#check if the ball is colliding with the upper part of the window
		elif ( left_score.get_line().top + left_score.get_line().height >= y_center - self.get_radius() ):
			self.set_y_velocity( - self.get_y_velocity() )
			return True
			
		#check if the ball is colliding with the lower part of the window
		elif ( self.get_window().get_height() <= (y_center + self.get_radius()) ):
			self.set_y_velocity( - self.get_y_velocity() )
			return True
			
		#check if the right player has scored
		elif ( x_center - self.get_radius() < left_player.left ):
			self.__player_collision_happened = False
			self.__move = False
			self.set_center(self.__starting_center)
			self.__goal(right_score)
			return True
		
		#check if the left player has scored
		elif ( x_center + self.get_radius() > right_player.right ):
			self.__player_collision_happened = False
			self.__move = False
			self.set_center(self.__starting_center)
			self.__goal(left_score)
			return True
	
	#adds 1 to the score of the player that scored	
	def __goal(self, score):
		score.upgrade_score()
			
		
	
	
	def get_window(self):
		return self.__window
		
	def get_center(self):
		return self.__center
		
	def get_radius(self):
		return self.__radius
		
	def get_color(self):
		return self.__color
		
	def is_moving(self):
		return self.__move
		
	def get_x_velocity(self):
		return self.__x_velocity
		
	def get_y_velocity(self):
		return self.__y_velocity
	
	def get_velocity(self):
		return self.__velocity
		
	def calculate_velocity(self):
		self.__velocity = math.sqrt(self.get_x_velocity()**2 + self.get_y_velocity()**2)
		return self.__velocity
	
	
	def set_x_velocity(self, x):
		self.__x_velocity = x
		
	def set_y_velocity(self, y):
		self.__y_velocity = y
	
	def set_velocity(self, v):
		self.__velocity = v
	
	def set_center(self, center):
		self.__center = center
	
	
	
	
	
	
