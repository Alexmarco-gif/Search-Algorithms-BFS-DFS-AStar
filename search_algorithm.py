
# This program finds paths through a maze
# different search strategies: Breadth-First Search (BFS),
# Depth-First Search (DFS), and A* (A-Star) algorithm.
#
# Each cell in the maze:
#   0 = open path (walkable)
#   1 = wall (blocked)

from collections import deque   # Efficient queue for BFS and DFS
import heapq                    # Priority queue for A* search

# Helper Function: Get Neighbors
def get_neighbors(maze, node):
    """
    Given a maze and a current node (x, y), 
    return all valid neighboring positions (up, down, left, right)
    that are walkable (== 0).
    """
    x, y = node
    # Directions: down, right, up, left
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    neighbors = []

    # Check all 4 possible moves
    for dx, dy in directions:
        nx, ny = x + dx, y + dy   # new position
        # Validate: inside grid and walkable (0)
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] == 0:
            neighbors.append((nx, ny))
    
    return neighbors


# Helper Function: Reconstruct Path
def reconstruct_path(parent, start, goal):
    """
    Reconstructs the path from 'start' to 'goal' 
    using the 'parent' dictionary that records how we reached each node.
    """
    path = []
    current = goal

    # Backtrack from goal → start
    while current != start:
        path.append(current)
        current = parent.get(current)  # Move one step back using parent links
        if current is None:  # If goal is unreachable
            return []

    path.append(start)
    path.reverse()  # Reverse so path goes from start → goal
    return path


# Breadth-First Search (BFS)
def bfs(maze, start, goal):
    """
    BFS explores the maze level by level, ensuring 
    the shortest path (in terms of number of steps) is found.
    """
    queue = deque([start])   # FIFO queue for BFS
    visited = {start}        # Keep track of visited cells
    parent = {}              # Store how we reached each cell
    
    while queue:
        current = queue.popleft()  # Take the first node in the queue

        # If we reached the goal, reconstruct and return the path
        if current == goal:
            return reconstruct_path(parent, start, goal)

        # Explore all valid neighbors
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)           # Mark as visited
                parent[neighbor] = current      # Record the path
                queue.append(neighbor)          # Add to queue for exploration
    
    return []  # No path found


# Depth-First Search (DFS)
def dfs(maze, start, goal):
    """
    DFS explores the maze deeply along one branch before backtracking.
    It doesn't guarantee the shortest path, but it's simple and fast for small mazes.
    """
    stack = deque([start])   # LIFO stack (using deque)
    visited = {start}
    parent = {}
    
    while stack:
        current = stack.pop()  # Take the last node (deepest branch first)

        # Check if goal is reached
        if current == goal:
            return reconstruct_path(parent, start, goal)

        # Explore all possible moves
        for neighbor in get_neighbors(maze, current): 
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)  # Add to stack for deep exploration
    
    return None  # No path found


# Heuristic Function (used in A*)
def heuristic(a, b):
    """
    Estimates distance between two points using Manhattan distance.
    This is the heuristic used in A* to guide the search.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Search Algorithm
def astar(maze, start, goal):
    """
    A* combines the strengths of BFS and Greedy Search.
    It finds the shortest path efficiently using both:
      g(n): cost from start to current node
      h(n): heuristic estimate from current node to goal
    """
    open_set = []  # Priority queue (min-heap)
    heapq.heappush(open_set, (0, start))  # Push starting node with f-score = 0
    parent = {}
    g_score = {start: 0}  # Distance from start to each node
    visited = set()
    
    while open_set:
        # Select node with lowest f = g + h
        _, current = heapq.heappop(open_set)

        # Skip if we've already processed this node
        if current in visited:
            continue
        visited.add(current)

        # Goal reached → build path
        if current == goal:
            return reconstruct_path(parent, start, goal)

        # Explore all neighbors
        for neighbor in get_neighbors(maze, current):
            # Tentative g = cost from start to neighbor
            tentative_g = g_score[current] + 1

            # If new shorter path found, or neighbor not yet visited
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)  # Total estimated cost
                heapq.heappush(open_set, (f_score, neighbor))      # Add to priority queue
                parent[neighbor] = current                         # Track path
    
    return None  # No path found
