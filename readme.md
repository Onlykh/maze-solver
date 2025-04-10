# Maze Solver

A Python application that generates and solves random mazes with visual representation.

## Overview

This project creates random mazes using a depth-first search algorithm and solves them using recursive backtracking. The entire process is visualized in a graphical interface built with Tkinter.

## Features

- Random maze generation
- Automated maze solving with visualization
- Configurable maze size and dimensions
- Animation of both generation and solving processes

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/maze-solver.git
   cd maze-solver
   ```

2. No external dependencies required beyond Python's standard library.

## Usage

Run the main script:

```
python src/main.py
```

This will:

1. Open a window displaying the maze
2. Generate a random maze with walls
3. Automatically solve the maze, showing the path from start to finish
4. The window will stay open until manually closed

## How It Works

- **Maze Creation**: Uses a depth-first search recursive algorithm to break walls and create paths
- **Maze Solving**: Uses a recursive backtracking algorithm to find the path from entrance to exit
- **Visualization**: The process is animated to show both generation and solution finding

## Project Structure

- `main.py` - Entry point of the application
- `maze.py` - Contains the Maze class that handles generation and solving
- `cell.py` - Represents a single cell in the maze with walls
- `window.py` - Handles the GUI window using Tkinter
- `line.py` - Utility for drawing lines in the window
- `point.py` - Represents a 2D point
- `tests.py` - Unit tests for the maze implementation

## Testing

Run the tests with:

```
python src/tests.py
```

## Customization

You can modify parameters in `main.py` to change:

- Window size
- Number of rows and columns
- Cell size
