"""Collection of Sudoku grids for testing."""
from solver import print_grid, solve
# Empty grid (all zeros)
empty_grid = [[0]*9 for _ in range(9)]

# Easy grid (already almost solved)
easy_grid = [
    [0, 0, 3, 0, 0, 0, 9, 0, 0],
    [0, 9, 0, 0, 3, 0, 0, 6, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 3],
    [0, 0, 5, 0, 0, 0, 8, 0, 0],
    [0, 7, 0, 0, 1, 0, 0, 9, 0],
    [0, 0, 9, 0, 0, 0, 4, 0, 0],
    [3, 0, 0, 6, 0, 4, 0, 0, 7],
    [0, 1, 0, 0, 8, 0, 0, 2, 0],
    [0, 0, 6, 0, 0, 0, 3, 0, 0]
]

# Hard grid (world's hardest Sudoku by Arto Inkala)
hard_grid = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

if __name__ == "__main__":
    print("Testing hard grid:")
    print_grid(hard_grid)
    import copy
    grid_copy = copy.deepcopy(hard_grid)
    if solve(grid_copy):
        print("\nSolved hard grid:")
        print_grid(grid_copy)
    else:
        print("No solution.")
