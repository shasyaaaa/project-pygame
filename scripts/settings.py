import pygame

# Game Window Size
COLLUMNS = 10
ROWS = 19
CELL_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# Side Bar Size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# Color
LIGHT_SLATE_GRAY = "#778899"
WHITE = "#FFFFFF"
DARK_GRAY = "#696969"
YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204b9b'
GREEN = '#65b32e'
PURPLE = '#7b217f'
CYAN = '#6cc6d9'
ORANGE = '#f07e13'
GRAY = '#1C1C1C'

# shapes
TETROMINOS = {
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': YELLOW},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': BLUE},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': ORANGE},
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED}
}

# game behaviour
UPDATE_START_SPEED =200
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLLUMNS // 2, -1)

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}