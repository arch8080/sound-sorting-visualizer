"""
Visualizer for rendering the sorting process
"""
import pygame
from constants import (WIDTH, HEIGHT, BACKGROUND, BAR_COLOR, COMPARING_COLOR, 
                      SWAPPING_COLOR, SORTED_COLOR, TEXT_COLOR, HEADER_COLOR, 
                      BAR_SPACING, MIN_VALUE, MAX_VALUE)


class Visualizer:
    """Handles all visual rendering for the sorting visualizer"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sound Sorting Visualizer")
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
    
    def draw_array(self, array, comparing=None, swapping=None, sorted_indices=None):
        """
        Draw the array as bars on the screen
        
        Args:
            array: List of values to visualize
            comparing: Indices being compared (highlighted in red)
            swapping: Indices being swapped (highlighted in yellow)
            sorted_indices: Set of sorted indices (highlighted in green)
        """
        self.screen.fill(BACKGROUND)
        
        if comparing is None:
            comparing = []
        if swapping is None:
            swapping = []
        if sorted_indices is None:
            sorted_indices = set()
        
        # Calculate bar dimensions
        num_bars = len(array)
        bar_width = (WIDTH - (num_bars + 1) * BAR_SPACING) / num_bars
        max_bar_height = HEIGHT - 200  # Leave space for text
        
        # Draw each bar
        for i, value in enumerate(array):
            # Calculate bar dimensions
            x = BAR_SPACING + i * (bar_width + BAR_SPACING)
            bar_height = (value - MIN_VALUE) / (MAX_VALUE - MIN_VALUE) * max_bar_height
            y = HEIGHT - 100 - bar_height
            
            # Choose color based on state
            if i in sorted_indices:
                color = SORTED_COLOR
            elif i in swapping:
                color = SWAPPING_COLOR
            elif i in comparing:
                color = COMPARING_COLOR
            else:
                color = BAR_COLOR
            
            # Draw the bar
            pygame.draw.rect(self.screen, color, (x, y, bar_width, bar_height))
    
    def draw_header(self, algorithm_name, time_complexity, space_complexity, is_sorting):
        """Draw algorithm information at the top"""
        y_offset = 20
        
        # Algorithm name
        title = self.font.render(algorithm_name, True, TEXT_COLOR)
        self.screen.blit(title, (20, y_offset))
        
        # Status
        status = "Sorting..." if is_sorting else "Press SPACE to start"
        status_text = self.small_font.render(status, True, HEADER_COLOR)
        self.screen.blit(status_text, (WIDTH - 250, y_offset))
        
        # Complexity information
        y_offset += 50
        time_text = self.small_font.render(f"Time: {time_complexity}", True, HEADER_COLOR)
        space_text = self.small_font.render(f"Space: {space_complexity}", True, HEADER_COLOR)
        
        self.screen.blit(time_text, (20, y_offset))
        self.screen.blit(space_text, (20, y_offset + 30))
    
    def draw_instructions(self):
        """Draw control instructions at the bottom"""
        instructions = [
            "SPACE - Start/Resume  |  R - Reset  |  ESC - Quit",
            "1 - Bubble  |  2 - Insertion  |  3 - Selection  |  4 - Merge  |  5 - Quick"
        ]
        
        y = HEIGHT - 80
        for instruction in instructions:
            text = self.small_font.render(instruction, True, HEADER_COLOR)
            text_rect = text.get_rect(center=(WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 30
    
    def update_display(self):
        """Update the display"""
        pygame.display.flip()