"""
Main application controller for Sound Sorting Visualizer
"""
import pygame
import random
from constants import ARRAY_SIZE, MIN_VALUE, MAX_VALUE, FPS
from visualizer import Visualizer
from audio_engine import AudioEngine
from algorithms import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort


class SoundSortingApp:
    """Main application class that coordinates all components"""
    
    def __init__(self):
        self.visualizer = Visualizer()
        self.audio_engine = AudioEngine()
        self.clock = pygame.time.Clock()
        
        # Algorithm registry
        self.algorithms = {
            pygame.K_1: BubbleSort,
            pygame.K_2: InsertionSort,
            pygame.K_3: SelectionSort,
            pygame.K_4: MergeSort,
            pygame.K_5: QuickSort,
        }
        
        # State
        self.array = self.generate_array()
        self.current_algorithm = BubbleSort
        self.is_sorting = False
        self.running = True
    
    def generate_array(self):
        """Generate a random array of values"""
        return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARRAY_SIZE)]
    
    def reset(self):
        """Reset the visualizer with a new array"""
        self.array = self.generate_array()
        self.is_sorting = False
    
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                
                elif event.key == pygame.K_SPACE and not self.is_sorting:
                    self.start_sorting()
                
                elif event.key == pygame.K_r:
                    self.reset()
                
                elif event.key in self.algorithms and not self.is_sorting:
                    self.current_algorithm = self.algorithms[event.key]
    
    def start_sorting(self):
        """Start the sorting process"""
        self.is_sorting = True
        
        # Create algorithm instance
        algorithm = self.current_algorithm(
            self.array,
            self.visualizer,
            self.audio_engine,
            self.clock
        )
        
        # Run the sorting algorithm
        algorithm.sort()
        
        self.is_sorting = False
    
    def draw(self):
        """Draw the current state"""
        self.visualizer.draw_array(self.array)
        
        # Create a temporary algorithm instance to get info
        temp_algo = self.current_algorithm(self.array, None, None, None)
        
        self.visualizer.draw_header(
            temp_algo.get_name(),
            temp_algo.get_time_complexity(),
            temp_algo.get_space_complexity(),
            self.is_sorting
        )
        self.visualizer.draw_instructions()
        self.visualizer.update_display()
    
    def run(self):
        """Main application loop"""
        while self.running:
            self.handle_events()
            
            if not self.is_sorting:
                self.draw()
            
            self.clock.tick(FPS)
        
        # Cleanup
        self.audio_engine.cleanup()
        pygame.quit()


def main():
    """Entry point for the application"""
    app = SoundSortingApp()
    app.run()


if __name__ == "__main__":
    main()