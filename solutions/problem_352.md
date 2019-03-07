# Skipping implementation since no unit tests are provided.

## Steps
- For a white square, if the previous row/column was black/before the start of the grid
  - Check if next 2 squares to the right are white (if column). Ditto for the next 2 squares below (if row). If not for either case, the crossword is invalid.
- Enumerate set of white squres.
- Start at the first white square and do a BFS until there are no more adjacent white squares to be seen. 
  - If the set difference of all white squares and seen white squares from this process if non-empty, then the crossword is invalid.
