import pygame

# constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 155)


# initialize pygame
class Visualizer:

    def __init__(self, width=1280, height=960, agent_name="default"):
        # screen
        self.window_size = (width, height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("MAZE GAME")

        # font
        pygame.font.init()
        self.font_name = "comicsans"

        # name
        self.agent_name = agent_name

    # draw the lines + numbers
    def draw(self, grid, height, width, position):
        self.screen.fill(WHITE)

        window_width, window_height = self.window_size
        
        square_size = min(window_width // width, window_height // height)
        
        offset_x = (window_width - (square_size * width)) // 2
        offset_y = (window_height - (square_size * height)) // 2
    
        thickness = 2
    
        # dinamico muajajajja
        font = pygame.font.SysFont(self.font_name, square_size // 2)

        for i in range(height):
            for j in range(width):
                x = offset_x + (j * square_size)
                y = offset_y + (i * square_size)
    
                pygame.draw.rect(self.screen, BLACK, (x, y, square_size, square_size))
    
                color = WHITE
                if grid[i][j] == 0:
                    color = RED
                    if (i, j) == position:
                        color = BLUE
                
                pygame.draw.rect(self.screen, color,
                                 (x + thickness, y + thickness,
                                  square_size - (2 * thickness), square_size - (2 * thickness)))
    
                # draw agent
                if position == (i, j):
                    pygame.draw.circle(self.screen, BLUE,
                                       (x + square_size // 2, y + square_size // 2),
                                       (square_size // 2) - thickness - 2)
    
                if grid[i][j] != 0:
                    text = font.render(str(grid[i][j]), True, BLACK)
                    text_rect = text.get_rect(center=(x + square_size // 2, y + square_size // 2))
                    self.screen.blit(text, text_rect)

        # agent_name_text
        agent_font = pygame.font.SysFont(self.font_name, 40)
        agent_text = agent_font.render(f"agent: {self.agent_name}", True, DARK_BLUE)
        self.screen.blit(agent_text,
                         (20, 20))

        pygame.display.flip()
