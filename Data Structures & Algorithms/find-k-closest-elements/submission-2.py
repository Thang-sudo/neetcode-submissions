class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, k - 1
        while right < len(arr) - 1:
            if abs(arr[left] - x) > abs(arr[right + 1] - x) or (abs(arr[left] - x) == abs(arr[right + 1] - x) and arr[left] == arr[right + 1]):
                left += 1
                right += 1
            else:
                break
        return arr[left : right + 1]
        