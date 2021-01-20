def setZeroes(self, matrix: List[List[int]]) -> None:
    """
        Do not return anything, modify matrix in-place instead.
        """
    rows, cols = set(), set()
    R = len(matrix)
    C = len(matrix[0])

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0


def setZeroesOne(self, matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    is_col = False
    for r in range(ROWS):
        if matrix[0][0] == 0:
            is_col = True

        # if the current CELL is Zero, then you want to set the 1st col and 1st row as reference to ZERO
        for c in range(1, COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # we don't account for the 1st col or the 1st row yet (bc we still need as reference)
    # but check to see if every cell is zero and if the reference is zero
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # change the first row to ZEROS
    if matrix[0][0] == 0:
        for c in range(COLS):
            matrix[0][c] = 0

    # change the first column to ZEROs
    if is_col:
        for r in range(ROWS):
            matrix[r][0] = 0
