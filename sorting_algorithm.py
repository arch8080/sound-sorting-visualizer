"""
Abstract base class for all sorting algorithms
"""
from abc import ABC, abstractmethod
import pygame
from constants import FPS


class SortingAlgorithm(ABC):
    """Base class providing common functionality for all sorting algorithms"""
    
    def __init__(self, array, visualizer, audio_engine, clock):
        self.array = array
        self.visualizer = visualizer
        self.audio_engine = audio_engine
        self.clock = clock
        self.sorted_indices = set()
    
    @abstractmethod
    def get_name(self):
        """Return the name of the algorithm"""
        pass
    
    @abstractmethod
    def get_time_complexity(self):
        """Return the time complexity"""
        pass
    
    @abstractmethod
    def get_space_complexity(self):
        """Return the space complexity"""
        pass
    
    @abstractmethod
    def sort(self):
        """Implement the sorting algorithm"""
        pass
    
    def swap(self, i, j):
        """Swap two elements and visualize"""
        self.array[i], self.array[j] = self.array[j], self.array[i]
        self.draw(swapping=[i, j])
        self.play_sound(self.array[i])
        self.play_sound(self.array[j])
    
    def draw(self, comparing=None, swapping=None):
        """Draw the current state of the array"""
        # Handle events to prevent freezing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        self.visualizer.draw_array(self.array, comparing, swapping, self.sorted_indices)
        self.visualizer.draw_header(
            self.get_name(),
            self.get_time_complexity(),
            self.get_space_complexity(),
            True
        )
        self.visualizer.draw_instructions()
        self.visualizer.update_display()
        self.clock.tick(FPS)
    
    def play_sound(self, value):
        """Play a sound for the given value"""
        self.audio_engine.play_note(value)
    
    def mark_sorted(self, indices):
        """Mark indices as sorted"""
        if isinstance(indices, int):
            self.sorted_indices.add(indices)
        else:
            self.sorted_indices.update(indices)