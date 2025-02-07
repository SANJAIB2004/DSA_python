import collections

def validsuduko(suduko):
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if suduko[r][c] ==0:
                return ['']
            if suduko[r][c] in rows[r] or suduko[r][c] in cols[c] or suduko[r][c] in squares[(r//3,c//3)]:
                return False
            rows[r].add(suduko[r][c])
            cols[c].add(suduko[r][c])
            squares[(r//3,c//3)].add(suduko[r][c])
    return True


suduko =[ [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
print(validsuduko(suduko))

