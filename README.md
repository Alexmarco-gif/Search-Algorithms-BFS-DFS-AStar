# Pathfinding Algorithms Comparison

**Pathfinding project comparing Breadth-First Search (BFS), Depth-First Search (DFS), and A* (A-Star) search algorithms to solve randomly generated mazes in Python.**

A Python implementation comparing the performance and path characteristics of three fundamental search algorithms—**Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **A\*** (A-Star)—to solve randomly generated mazes.

## ✨ Features

* **Three Search Strategies:** Implementations of BFS, DFS, and the informed A\* algorithm for pathfinding.
* **Maze Generation:** Uses a simple recursive backtracking algorithm to generate perfect, solvable mazes.
* **Visual Output:** Prints the solved maze to the console, clearly marking the **Start (S)**, **Goal (G)**, and the found **Path (.)**.
* **Modularity:** Clean separation of concerns with dedicated files for maze generation, search logic, and the main execution script.

---

## ⚙️ Algorithms Implemented

| Algorithm | Key Characteristic | Optimality | Search Strategy |
| :--- | :--- | :--- | :--- |
| **BFS** | Uses a Queue (FIFO). Explores uniformly outward. | **Guaranteed Shortest Path** (by steps). | Uninformed (Exhaustive) |
| **DFS** | Uses a Stack (LIFO). Explores one branch completely. | **Not Guaranteed Shortest Path**. | Uninformed (Depth-first) |
| **A\*** | Uses a Priority Queue. Guided by $f(n) = g(n) + h(n)$. | **Guaranteed Shortest Path** (if heuristic is admissible). | Informed (Heuristic) |

---

## 📁 Project Structure

| File Name | Description |
| :--- | :--- |
| `main.py` | The entry point. Handles maze generation, user input for algorithm selection, calling the solver, and printing the results. |
| `search_algorithm.py` | Contains the core logic for `bfs`, `dfs`, and `astar` functions, along with path reconstruction and neighbor finding helpers. |
| `maze_gen.py` | Contains the `generate_maze` function, which uses a recursive backtracking algorithm to create the maze grid. |

---

## 🔎 Algorithm Visualizations

To better understand how each algorithm explores the maze, compare the pathfinding mechanisms below.

### 1. Breadth-First Search (BFS)
BFS guarantees the shortest path by exploring all nodes at depth $k$ before moving to depth $k+1$. It expands like ripples in a pond.



### 2. Depth-First Search (DFS)
DFS quickly dives deep into the maze, exploring one direction as far as possible before backtracking. This can lead to a long, non-optimal path.



### 3. A* Search (A-Star)
A\* uses a heuristic (Manhattan distance in this implementation) to estimate the cost to the goal, allowing it to prioritize the most promising nodes and find the shortest path efficiently.


---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are strictly required beyond the standard library modules used (`collections`, `heapq`, `random`).

### Running the Program

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YourUsername/Maze-Search-Algorithms-BFS-DFS-AStar.git](https://github.com/YourUsername/Maze-Search-Algorithms-BFS-DFS-AStar.git)
    cd Maze-Search-Algorithms-BFS-DFS-AStar
    ```
    *(**Note:** Remember to replace `YourUsername` and the repo name if necessary.)*

2.  Run the main script:
    ```bash
    python main.py
    ```
3.  Follow the prompts to select an algorithm (**1** for BFS, **2** for DFS, or **3** for A\*) and see the solved maze printed in your console!

---
---

## 💡 Future Enhancements and Scope

This project was developed primarily as a **practical exercise** to clearly understand and contrast the mechanics of Breadth-First Search (BFS), Depth-First Search (DFS), and A\* (A-Star) pathfinding algorithms.

While functional, there are several areas where the code and presentation could be significantly improved for efficiency, user experience, and robustness:

### Potential Improvements

* **GUI/Visualizer:** The current output is purely console-based. A major enhancement would be adding a graphical user interface (GUI) using libraries like **Pygame** or **Tkinter** to visualize the search process in real-time (showing the 'wave' of expansion for BFS or the 'dive' of DFS). 
* **Performance Benchmarking:** Implement a feature to automatically run the algorithms multiple times on the same maze and track metrics like **execution time** and **path length** for a direct, quantitative comparison.
* **Weighted Grids:** Currently, all open paths have a uniform cost of 1. The A\* algorithm could be enhanced to handle **weighted grids** where different path types (e.g., mud, water, grass) have different movement costs.
* **Maze Complexity:** The maze generation could be expanded to include different generation algorithms (e.g., Kruskal's or Prim's algorithm) or to create mazes with solutions that are more challenging for DFS.

### Scope Disclaimer
Was just playing with this kind of problem to have beter understanding 
