"""
Lab 3: The Row-Major Detective -- starter.

Complete the two functions below. See
Lab_03_The_Row_Major_Detective.md, Part B, for the full requirements.
"""

from typing import List


def transpose_inplace(matrix: List[List[float]]) -> None:
    """
    Transpose a SQUARE matrix in place (no new matrix allocated).
    Mutates `matrix` directly; returns None.
    """
    # DONE TODO
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]



def transpose_blocked(matrix: List[List[float]], block_size: int) -> List[List[float]]:
    """
    Transpose a (possibly non-square) matrix using a blocked/tiled
    access pattern for cache locality, returning a NEW matrix.
    """
    # DONE TODO
    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0
    result = [[0.0] * rows for _ in range(cols)]
    for r0 in range(0, rows, block_size):
        r1 = min(r0 + block_size, rows)
        for c0 in range(0, cols, block_size):
            c1 = min(c0 + block_size, cols)
            for i in range(r0, r1):
                row = matrix[i]
                for j in range(c0, c1):
                    result[j][i] = row[j]
    return result