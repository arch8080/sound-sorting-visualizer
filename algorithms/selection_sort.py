"""
Selection Sort Algorithm
"""
from sorting_algorithm import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    """
    Selection Sort implementation
    Divides the array into sorted and unsorted regions, repeatedly selects the minimum element
    """
    
    def get_name(self):
        return "Selection Sort"
    
    def get_time_complexity(self):
        return "O(n²)"
    
    def get_space_complexity(self):
        return "O(1)"
    
    def sort(self):
        n = len(self.array)
        
        for i in range(n):
            # Find the minimum element in the unsorted portion
            min_idx = i
            
            for j in range(i + 1, n):
                self.draw(comparing=[min_idx, j])
                self.play_sound(self.array[j])
                
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            
            # Swap the found minimum element with the first element
            if min_idx != i:
                self.swap(i, min_idx)
            
            # Mark this position as sorted
            self.mark_sorted(i)
            self.draw()
        
        # Mark all as sorted
        self.mark_sorted(range(n))
        self.draw()