# Smart Sudoku Solver
This program Solves 3x3 and 4x4 sudoku using Crook's algorithm and backtracking. 
Using this hybrid method is much faster than brute-forcing the sudoku.

When [Crook](http://www.ams.org/notices/200904/rtx090400460p.pdf) can't fill in any more squares, we brute force the remaining empty squares.

Originally created to solve 16x16 sudoku's which took way too much time to brute-force.

## Usage
Use board templates from `board_templates.py` or create your own and
change the board name in `sudoku.py`, then run and let the magic do its work.
```python
import sudoku, board, board_templates
board = Board(board_templates.board_normal_medium)
sudoku = Sudoku(board)
sudoku.solve()
print(sudoku)
```

## Performance
For estimation purposes
Algorithm | Time 3x3 (sec) | Time 4x4 (sec)
--- | --- | ---
Crook | 0.006 | 0.26
Backtrack | 0.001 | +6 days

