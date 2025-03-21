N = 8  # Chessboard size

def print_solution(pos):
    """Prints the board configuration using the position array."""
    for row in range(N):
        line = ["." for _ in range(N)]
        line[pos[row]] = "Q"  # Place queen
        print(" ".join(line))
    print("\n")

def is_safe(pos, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(row):
        # Check same column or diagonals
        if pos[i] == col or abs(pos[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(pos, row):
    """Recursively places queens row by row."""
    if row == N:
        print_solution(pos)
        return True  # Stop after finding the first solution

    for col in range(N):
        if is_safe(pos, row, col):
            pos[row] = col  # Place queen
            if solve_n_queens(pos, row + 1):  # If a solution is found, stop
                return True

    return False  # No valid placement found

def solve():
    """Initializes position array and starts solving."""
    pos = [-1] * N  # pos[i] stores the column of the queen in row i
    if not solve_n_queens(pos, 0):
        print("No solution exists")

solve()
