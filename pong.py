import pygame
import time
from left_player import LeftPlayer
from right_player import RightPlayer
from ball import Ball
from left_score import LeftScore
from right_score import RightScore



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 1072
WINDOW_HEIGHT_PLAYABLE = 604
WINDOW_HEIGHT_SCORE = 100
WINDOW_HEIGHT = WINDOW_HEIGHT_PLAYABLE + WINDOW_HEIGHT_SCORE
WINDOW_TITLE = 'Pong'

MAX_FRAMES = 100

PLAYER_WIDTH = 10
PLAYER_HEIGHT = 120
PLAYER_X_DISTANCE_TO_WINDOW = 20
PLAYER_STARTING_Y = WINDOW_HEIGHT_SCORE + (WINDOW_HEIGHT_PLAYABLE-PLAYER_HEIGHT)/2
LEFT_PLAYER_STARTING_X = PLAYER_X_DISTANCE_TO_WINDOW
RIGHT_PLAYER_STARTING_X = WINDOW_WIDTH - (PLAYER_WIDTH + PLAYER_X_DISTANCE_TO_WINDOW)
PLAYER_SPEED = 320 / MAX_FRAMES
PLAYER_MOVE_UP = (0, -PLAYER_SPEED) 
PLAYER_MOVE_DOWN = (-PLAYER_MOVE_UP[0], -PLAYER_MOVE_UP[1])

BALL_CENTER = (WINDOW_WIDTH/2, (WINDOW_HEIGHT + WINDOW_HEIGHT_SCORE)/2)
BALL_RADIUS = 20

FONT_NAME = 'arial'
FONT_SIZE = 40



def main():
	pygame.init()
	
	window_ = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption(WINDOW_TITLE)
	
	
	l_score_ = LeftScore(window_, FONT_NAME, FONT_SIZE, WINDOW_HEIGHT_SCORE)
	l_player_ = LeftPlayer(window_, l_score_, LEFT_PLAYER_STARTING_X, PLAYER_STARTING_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
	
	r_score_ = RightScore(window_, FONT_NAME, FONT_SIZE, WINDOW_HEIGHT_SCORE)
	r_player_ = RightPlayer(window_, r_score_, RIGHT_PLAYER_STARTING_X, PLAYER_STARTING_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
	
	ball_ = Ball(window_, MAX_FRAMES, BALL_CENTER, BALL_RADIUS)
	
	
	run_game = True
	clock_ = pygame.time.Clock()
	
	
	#first_time = True
	
	while run_game:
		
		clock_.tick(MAX_FRAMES)
		window_.fill(BLACK)
		
		
		l_player_.draw(WHITE)
		r_player_.draw(WHITE)
		ball_.draw(WHITE)
		l_score_.draw()
		r_score_.draw()
		
		#while ( first_time and (not pygame.key.get_focused()) ):
			
		
		#first_time = False
		
		key = pygame.key.get_pressed()
		l_player_.move_up(key, PLAYER_MOVE_UP)
		l_player_.move_down(key, PLAYER_MOVE_DOWN)
		r_player_.move_up(key, PLAYER_MOVE_UP)
		r_player_.move_down(key, PLAYER_MOVE_DOWN)
		
		ball_.check_collision(l_player_, r_player_, l_score_, r_score_)
		ball_.move()
		
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run_game = False
				
		pygame.display.update()
				
	pygame.quit()
	

if __name__ == "__main__":
	main()
