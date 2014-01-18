# import sys

def __init_matrix(rows, cols):
    """Build a matrix required for dynamic computing edit distance given number
    of rows and colums.

    Returns matix (list of list)."""
    matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        matrix[i][0] = i
    for i in range(cols):
        matrix[0][i] = i

    return matrix

def find_edit_distance(word_a, word_b):
    """Using dynamic programming to find the edit distance between word_a and
    word_b.

    Returns the distance as in integer"""

    cols = len(word_a)+1
    rows = len(word_b)+1
    
    matrix = __init_matrix(rows, cols)

    for r in range(1, rows):
        for c in range(1, cols):
            if word_a[c-1] == word_b[r-1]:
                matrix[r][c] = matrix[r-1][c-1]
            else:
                matrix[r][c] = min(matrix[r-1][c], matrix[r-1][c-1],
                        matrix[r][c-1]) + 1

    return matrix[rows-1][cols-1]


# if __name__ == "__main__":
# 
#     # words = ('Queensland', 'Quenads')
#     words = sys.argv[1:]
# 
#     print find_edit_distance(words[0], words[1])
