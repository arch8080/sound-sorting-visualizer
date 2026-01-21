# Sound Sorting Visualizer - Modular Architecture

A modular, object-oriented implementation of sorting algorithm visualization with audio feedback.

## Project Structure

```
sound-sorting-visualizer/
├── constants.py              # Configuration and constants
├── audio_engine.py           # Audio generation and playback
├── visualizer.py             # Visual rendering
├── sorting_algorithm.py      # Abstract base class for algorithms
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── bubble_sort.py
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
├── app.py                    # Main application class
└── main.py                   # Entry point
```

## Architecture

### 1. Separation of Concerns
- `constants.py`: All configuration values in one place
- `audio_engine.py`: Isolated audio generation logic
- `visualizer.py`: Pure rendering logic
- `sorting_algorithm.py`: Abstract interface for all algorithms

### 2. Abstraction
- `SortingAlgorithm` base class provides common functionality
- Each algorithm extends the base class and implements `sort()` method
- Consistent interface across all algorithms

### 3. Modularity
- Each algorithm in its own file
- Easy to add new algorithms by extending `SortingAlgorithm`
- Components can be tested independently

### 4. Extensibility

To add a new sorting algorithm:

```python
# algorithms/heap_sort.py
from sorting_algorithm import SortingAlgorithm

class HeapSort(SortingAlgorithm):
    def get_name(self):
        return "Heap Sort"
    
    def get_time_complexity(self):
        return "O(n log n)"
    
    def get_space_complexity(self):
        return "O(1)"
    
    def sort(self):
        # Implement your algorithm
        # Use self.draw(), self.play_sound(), etc.
        pass
```

Then register it in `app.py`:

```python
from algorithms.heap_sort import HeapSort

self.algorithms = {
    # ...existing algorithms...
    pygame.K_6: HeapSort,
}
```

## Installation

```bash
pip install pygame numpy pyaudio
```

## Usage

```bash
python main.py
```

### Controls

- SPACE: Start sorting
- R: Generate new array
- 1: Bubble Sort
- 2: Insertion Sort
- 3: Selection Sort
- 4: Merge Sort
- 5: Quick Sort
- ESC: Quit

## Benefits of This Architecture

1. **Maintainability**: Each component has a single responsibility
2. **Testability**: Components can be unit tested independently
3. **Reusability**: AudioEngine and Visualizer can be reused in other projects
4. **Scalability**: Easy to add new algorithms without modifying existing code
5. **Readability**: Clear structure makes the code easier to understand

## Key Classes

- **AudioEngine**: Handles all sound generation
- **Visualizer**: Manages all visual rendering
- **SortingAlgorithm**: Abstract base for algorithm implementations
- **SoundSortingApp**: Main application controller

## Design Patterns Used

- **Strategy Pattern**: Interchangeable sorting algorithms
- **Template Method**: Base class defines structure, subclasses implement details
- **Facade Pattern**: SoundSortingApp provides simple interface to complex subsystems

## Algorithm Complexity

| Algorithm | Time (Average) | Space |
|-----------|----------------|-------|
| Bubble Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(log n) |

## License

MIT License
