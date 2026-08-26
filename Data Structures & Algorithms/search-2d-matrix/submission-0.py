class Solution:
    def searchArray(self, arr: List[int], target: int) -> bool:
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if target == arr[middle]:
                return True
            elif target < arr[middle]: # Search left side
                right = middle - 1
            elif target > arr[middle]:
                left = middle + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        upper, lower = 0, num_rows - 1
        row_length = len(matrix[0])

        while upper <= lower:
            middle_row = (upper + lower) // 2
            if matrix[middle_row][0] == target or target == matrix[middle_row][row_length - 1]:
                print("Found as beginning or the last col of middle row")
                return True
            elif matrix[middle_row][0] < target and target < matrix[middle_row][row_length - 1]:
                print("Doing binary search for  row " + str(middle_row))
                return self.searchArray(matrix[middle_row], target)
            elif target < matrix[middle_row][0]:
                lower = middle_row - 1
            elif target > matrix[middle_row][row_length - 1]:
                upper = middle_row + 1
        return False
        