"""
Sound Sorting Visualizer
An interactive educational tool for visualizing sorting algorithms with audio feedback
"""
from app import main

if __name__ == "__main__":
    print("=" * 60)
    print("Sound Sorting Visualizer")
    print("=" * 60)
    print("\nStarting application...")
    print("\nControls:")
    print("  SPACE - Start sorting")
    print("  R - Generate new random array")
    print("  1 - Bubble Sort")
    print("  2 - Insertion Sort")
    print("  3 - Selection Sort")
    print("  4 - Merge Sort")
    print("  5 - Quick Sort")
    print("  ESC - Quit\n")
    
    main()
    
    print("\nThank you for using Sound Sorting Visualizer!")