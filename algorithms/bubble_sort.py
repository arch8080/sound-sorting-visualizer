"""
Bubble Sort Algorithm
"""
from sorting_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    """
    Bubble Sort implementation
    Repeatedly steps through the list, compares adjacent elements and swaps them if they're in wrong order
    """
    
    def get_name(self):
        return "Bubble Sort"
    
    def get_time_complexity(self):
        return "O(n²)"
    
    def get_space_complexity(self):
        return "O(1)"
    
    def sort(self):
        n = len(self.array)
        
        for i in range(n):
            swapped = False
            
            for j in range(0, n - i - 1):
                # Compare adjacent elements
                self.draw(comparing=[j, j + 1])
                self.play_sound(self.array[j])
                
                if self.array[j] > self.array[j + 1]:
                    # Swap if they're in wrong order
                    self.swap(j, j + 1)
                    swapped = True
            
            # Mark the last element as sorted
            self.mark_sorted(n - i - 1)
            
            # If no swaps occurred, array is sorted
            if not swapped:
                self.mark_sorted(range(n - i - 1))
                break
        
        # Mark all as sorted
        self.mark_sorted(range(n))
        self.draw()