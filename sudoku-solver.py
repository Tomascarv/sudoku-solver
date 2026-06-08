
"""
Sudoku Solver using backtracking with Minimum Remaining Values heuristic.
Author: Tomas Carvalho Mendes
Date: June 2025
Goal: Show algorithmic skills.
"""

def print_grid(grid):
    #Print nice grid
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()

def find_empty(grid):
    # Finds empty squares and returns its position 
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    # Check if the move is vaid
    row, col = pos
    # Check row
    for j in range(9):
        if grid[row][j] == num and col != j:
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == num and row != i:
            return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def find_possibilities(grid, row, col):
    # Finds all the numbers that can go in a square
    possibilities = []
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            possibilities.append(num)
    return possibilities

def solve(grid):
    """
    Solve Sudoku using backtracking with MRV heuristic.
    Returns True if solved, modifies grid in place.
    """
    empty = find_empty(grid)
    if not empty:
        return True   # Solved

    row, col = empty

    best_cell = None
    best_poss = None
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                poss = find_possibilities(grid, i, j)
                if best_cell is None or len(poss) < len(best_poss):
                    best_cell = (i, j)
                    best_poss = poss
                    if len(best_poss) == 1:
                        break
        if best_cell and len(best_poss) == 1:
            break

    if best_cell:
        row, col = best_cell
        possibilities = find_possibilities(grid, row, col)
    else:
        row, col = empty
        possibilities = list(range(1, 10))

    for num in possibilities:
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0   # backtrack

    return False

# Example usage
if __name__ == "__main__":
    # Sample Sudoku (where 0 indicates that square is empty)
    example_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original grid:")
    print_grid(example_grid)

    # Make a copy to solve
    grid_copy = [row[:] for row in example_grid]
    if solve(grid_copy):
        print("\nSolved grid:")
        print_grid(grid_copy)
    else:
        print("No solution exists.")
