"""
Quick Sort Algorithm
"""
from sorting_algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    """
    Quick Sort implementation
    Divide and conquer algorithm that picks a pivot and partitions array around it
    """
    
    def get_name(self):
        return "Quick Sort"
    
    def get_time_complexity(self):
        return "O(n log n) avg, O(n²) worst"
    
    def get_space_complexity(self):
        return "O(log n)"
    
    def sort(self):
        self.quick_sort_helper(0, len(self.array) - 1)
        self.mark_sorted(range(len(self.array)))
        self.draw()
    
    def quick_sort_helper(self, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_idx = self.partition(low, high)
            
            # Recursively sort elements before and after partition
            self.quick_sort_helper(low, pivot_idx - 1)
            self.quick_sort_helper(pivot_idx + 1, high)
    
    def partition(self, low, high):
        # Choose the rightmost element as pivot
        pivot = self.array[high]
        self.draw(comparing=[high])
        self.play_sound(pivot)
        
        # Index of smaller element
        i = low - 1
        
        for j in range(low, high):
            self.draw(comparing=[j, high])
            self.play_sound(self.array[j])
            
            # If current element is smaller than or equal to pivot
            if self.array[j] <= pivot:
                i += 1
                if i != j:
                    self.swap(i, j)
        
        # Swap the pivot element with the element at i+1
        if i + 1 != high:
            self.swap(i + 1, high)
        
        return i + 1