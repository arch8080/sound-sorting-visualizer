"""
Merge Sort Algorithm
"""
from sorting_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    """
    Merge Sort implementation
    Divide and conquer algorithm that divides array into halves, sorts them and merges them back
    """
    
    def get_name(self):
        return "Merge Sort"
    
    def get_time_complexity(self):
        return "O(n log n)"
    
    def get_space_complexity(self):
        return "O(n)"
    
    def sort(self):
        self.merge_sort_helper(0, len(self.array) - 1)
        self.mark_sorted(range(len(self.array)))
        self.draw()
    
    def merge_sort_helper(self, left, right):
        if left < right:
            mid = (left + right) // 2
            
            # Sort first and second halves
            self.merge_sort_helper(left, mid)
            self.merge_sort_helper(mid + 1, right)
            
            # Merge the sorted halves
            self.merge(left, mid, right)
    
    def merge(self, left, mid, right):
        # Create temporary arrays
        left_array = self.array[left:mid + 1].copy()
        right_array = self.array[mid + 1:right + 1].copy()
        
        i = 0  # Initial index of left subarray
        j = 0  # Initial index of right subarray
        k = left  # Initial index of merged subarray
        
        # Merge the temp arrays back
        while i < len(left_array) and j < len(right_array):
            self.draw(comparing=[k])
            
            if left_array[i] <= right_array[j]:
                self.array[k] = left_array[i]
                self.play_sound(left_array[i])
                i += 1
            else:
                self.array[k] = right_array[j]
                self.play_sound(right_array[j])
                j += 1
            
            self.draw(swapping=[k])
            k += 1
        
        # Copy remaining elements of left_array
        while i < len(left_array):
            self.array[k] = left_array[i]
            self.draw(swapping=[k])
            self.play_sound(left_array[i])
            i += 1
            k += 1
        
        # Copy remaining elements of right_array
        while j < len(right_array):
            self.array[k] = right_array[j]
            self.draw(swapping=[k])
            self.play_sound(right_array[j])
            j += 1
            k += 1