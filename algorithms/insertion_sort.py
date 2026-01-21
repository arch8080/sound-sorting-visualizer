"""
Insertion Sort Algorithm
"""
from sorting_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    """
    Insertion Sort implementation
    Builds the final sorted array one item at a time by inserting elements into their correct position
    """
    
    def get_name(self):
        return "Insertion Sort"
    
    def get_time_complexity(self):
        return "O(n²)"
    
    def get_space_complexity(self):
        return "O(1)"
    
    def sort(self):
        n = len(self.array)
        
        # First element is already "sorted"
        self.mark_sorted(0)
        
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            
            self.draw(comparing=[i])
            self.play_sound(key)
            
            # Move elements greater than key one position ahead
            while j >= 0 and self.array[j] > key:
                self.draw(comparing=[j, j + 1])
                self.play_sound(self.array[j])
                
                self.array[j + 1] = self.array[j]
                self.draw(swapping=[j, j + 1])
                
                j -= 1
            
            # Insert key at the correct position
            self.array[j + 1] = key
            self.mark_sorted(i)
            self.draw()
        
        # Mark all as sorted
        self.mark_sorted(range(n))
        self.draw()