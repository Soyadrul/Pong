import pygame
from player import Player

class RightPlayer(Player):

	
	
	def __init__(self, window, score, left, top, width, height):
		super().__init__(window, score, left, top, width, height)
		
	
		
	def move_up(self, key, movement):
		max_up_movement = self.how_much_can_player_move_up(movement)
		if(key[pygame.K_i] and max_up_movement < 0):
			#movement is less than maximum movement possible
			if(max_up_movement < movement[1] ):
				self.move_ip(movement)
			#maximum movement possible is less than or equal to the movement
			elif( max_up_movement >= movement[1] ):
				self.move_ip(0, max_up_movement)
			
	def move_down(self, key, movement):
		max_down_movement = self.how_much_can_player_move_down(movement)
		if(key[pygame.K_k] and max_down_movement > 0):
			#movement is less than maximum movement possible
			if( max_down_movement > movement[1]):
				self.move_ip(movement)
			#maximum movement possible is less than or equal to the movement
			elif( max_down_movement <= movement[1] ):
				self.move_ip(0, max_down_movement)
