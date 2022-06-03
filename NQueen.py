class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows, cols = (n, n)
        res = []
        arr = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(arr, 0, res)
        return res

    def solve(self, arr, col, res):
        if col == len(arr):
            # res.append(list(arr[i]))
            res.append([''.join(arr[i]) for i in range(len(arr))])
            return

        for i in range(len(arr)):
            if self.isSafe(arr, i, col):
                arr[i][col] = 'Q'
                if self.solve(arr, col + 1, res):
                    return True
                arr[i][col] = '.'
        return False

    def isSafe(self, arr, row, cols):

        for i in range(cols):
            if arr[row][i] == 'Q':
                return False

        # upper diagonal
        for i, j in zip(range(row, -1, -1), range(cols, -1, -1)):
            if arr[i][j] == 'Q':
                return False

        # lower diagonal
        for i, j in zip(range(row, len(arr), 1), range(cols, -1, -1)):
            if arr[i][j] == 'Q':
                return False

        return True
