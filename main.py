
#   1. Generates a random maze.
#   2. Lets the user choose a search algorithm (BFS, DFS, or A*).
#   3. Finds a path from the start to the goal.
#   4. Prints the maze and overlays the path.

from maze_gen import generate_maze                
from search_algorithm import bfs, dfs, astar     

# Function: print_maze
def print_maze(maze, path=None, start=None, goal=None):
    """
    Prints the maze in the console.
    
    Args:
        maze: 2D list (0 = open path, 1 = wall)
        path: list of coordinates forming the found path
        start: tuple (x, y) for the start position
        goal: tuple (x, y) for the goal position
    """
    # Symbols to display maze walls and open spaces
    display = {1: "█", 0: " "}   # Wall = █, Open path = space
    
    for y, row in enumerate(maze):
        line = ""
        for x, cell in enumerate(row):
            # Mark the path, start, and goal
            if path and (x, y) in path:
                line += "."       # Path cell
            elif start == (x, y):
                line += "S"       # Start point
            elif goal == (x, y):
                line += "G"       # Goal point
            else:
                line += display[cell]  # Default maze cell
        print(line)  # Print one row of the maze

# Function: main
def main():
    """
    Main function to:
    - Generate a maze
    - Ask user for algorithm choice
    - Solve the maze
    - Print result
    """
    width, height = 21, 21                # Maze dimensions
    maze = generate_maze(width, height)   # Generate new maze
    start = (1, 1)                        # Starting point (top-left area)
    goal = (width - 2, height - 2)        # Goal point (bottom-right area)

    # Ask the user to select which search algorithm to use
    print("Choose algorithm: 1) BFS  2) DFS  3) A*")
    choice = input("Enter choice (1/2/3): ").strip()

    # Run the chosen algorithm
    if choice == "1":
        path = bfs(maze, start, goal)
        algo = 'BFS'
    elif choice == "2":
        path = dfs(maze, start, goal)
        algo = 'DFS'
    elif choice == "3":
        path = astar(maze, start, goal)
        algo = 'A*'
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    # Display results
    print(f"\nAlgorithm used: {algo}")

    if path:
        print("\nSolved Maze:")
        print_maze(maze, path=path, start=start, goal=goal)
    else:
        print("No path found.")

# Run the main program only if this file is executed directly
if __name__ == "__main__":
    main()
