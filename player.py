import pygame

class Player(pygame.rect.Rect):
	
	def __init__(self, window, score, left, top, width, height):
		self.__window = window
		self.__score = score
		super().__init__((left, top, width, height))
	
	def get_window(self):
		return self.__window
	
	def get_score_object(self):
		return self.__score
	
	
	
	def draw(self, color):
		pygame.draw.rect(self.get_window(), color, self)
		
	def __can_player_move_up(self, movement):
		if ( self.top + movement[1] <= self.get_score_object().get_line().bottom ):
			return False
		else:
			return True
	
	def how_much_can_player_move_up(self, movement):
		#if ( self.__can_player_move_up(movement) ):
		return (self.get_score_object().get_line().bottom - self.top)
			
	def __can_player_move_down(self, movement):
		if ( self.bottom + movement[1] >= (self.get_window()).get_height() ):
			return False
		else:
			return True
	
	def how_much_can_player_move_down(self, movement):
		#if ( self.__can_player_move_down(movement) ):
		return ((self.get_window()).get_height() - self.bottom)
