import pygame
from player import Player

class Score:
	
	
	#r_l variable is a String storing 'left' or 'right' and is used to know if the Score object is a LeftSCore or a RightScore object
	def __init__(self, window, font_name, font_size, height, r_l):
		
		self.__BLACK = (0, 0, 0)
		self.__WHITE = (255, 255, 255)
		
		self.__window = window
		self.__score = 0
		self.__font_size = font_size
		self.__font_name = font_name
		self.__height = height
		self.__line = None
		self.__r_l = r_l
		
		self.__SCORE_FONT = pygame.font.SysFont(self.get_font_name(), self.get_font_size())
		
		self.set_score_text( self.get_SCORE_FONT().render(f'{self.get_score()}', 1, self.__WHITE) )
		
		
		self.__top = self.get_height()//2 -self.get_score_text().get_height()//2
		
		if (r_l == 'left'):
			self.__left = ( (self.get_window()).get_width() )//4 - (self.get_score_text()).get_width()//2
		else:
			self.__left = ( (self.get_window()).get_width() * 3 )//4 -(self.get_score_text()).get_width()//2
	
	
	def draw(self):
		(self.get_window()).blit( self.get_score_text(), (self.get_left(), self.get_top()) )
		
		line_width = 1
		self.__line = pygame.draw.line(self.get_window(), self.__WHITE, (0,self.get_height()-1), (self.get_window().get_width(), self.get_height()-1), line_width)
		pygame.draw.line(self.get_window(), self.__WHITE, (self.get_window().get_width()//2, 0), (self.get_window().get_width()//2, self.get_height()-1), line_width)
		
	
		
	
	
	def set_score_text(self, text):
		self.__score_text = text
	
	def set_left(self, left):
		self.__left = left
		
	def set_top(self, top):
		self.__top = top
	
	def upgrade_score(self):
		self.__score = self.__score + 1
		self.set_score_text( self.get_SCORE_FONT().render(f'{self.get_score()}', 1, self.__WHITE) )
	
	
	def get_window(self):
		return self.__window
	
	def get_score(self):
		return self.__score
		
	def get_score_text(self):
		return self.__score_text
	
	#left position of self.__score_text
	def get_left(self):
		return self.__left
	
	#top position of self.__score_text
	def get_top(self):
		return self.__top
	
	def get_font_size(self):
		return self.__font_size
	
	def get_font_name(self):
		return self.__font_name
		
	def get_SCORE_FONT(self):
		return self.__SCORE_FONT
	
	#height of the part of the window in which is displaed the score
	def get_height(self):
		return self.__height
	
	#returns a Rect object that divides the score part from the playable part of the window
	def get_line(self):
		return self.__line
	
