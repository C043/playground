class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rowCount, colCount = len(matrix), len(matrix[0])

        left, right = 0, rowCount * colCount - 1

        while left <= right:
            mid = (left + right) // 2

            value = matrix[mid // colCount][mid % colCount]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
matrix = [[1, 3]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))
