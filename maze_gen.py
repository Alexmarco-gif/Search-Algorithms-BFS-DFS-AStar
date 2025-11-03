import random

def generate_maze(width, height):
    # Initialize the maze with all walls (1 = wall, 0 = path)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Ensure new cell is inside bounds and not yet carved
            if 0 < nx < width and 0 < ny < height and maze[ny][nx] == 1:
                # Remove wall between current and next cell
                maze[y + dy // 2][x + dx // 2] = 0
                maze[ny][nx] = 0
                carve(nx, ny)

    # Pick a random odd start position
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    maze[start_y][start_x] = 0
    carve(start_x, start_y)

    return maze


