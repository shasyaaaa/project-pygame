from settings import *
from os.path import join

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING))
        self.rectangle = self.surface.get_rect(bottomright = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        self.display_surface = pygame.display.get_surface()

        # font
        self.font = pygame.font.Font(join('PROJECT PYGAME', 'graphics', 'Russo_One.ttf'), 30) 

        # increment
        self.increment_height = self.surface.get_height() / 3

        # data
        self.scores = 0
        self.levels = 1
        self.lines = 0

    
    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]}: {text[1]}', True, WHITE)
        text_rect = text_surface.get_rect(center = pos)

        self.surface.blit(text_surface, text_rect)

    def run(self):
        self.surface.fill(LIGHT_SLATE_GRAY)
        for i, text in enumerate([('Score', self.scores), ('Level', self.levels), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x, y), text)
        
        self.display_surface.blit(self.surface, self.rectangle)
        pygame.draw.rect(self.display_surface, WHITE, self.rectangle, 2, 2)