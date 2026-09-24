class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we need to count the frequency of elements in this nums array
        # iterate the list check the 'seen' dictionary if key exists -> increment the value. Otherwise, just create a new key with 1 value
        # initialize a results list, each element of the results list would be key, value pair
        # iterate the key value pair in dict
        # find the position in the results array, results array should contain value with decreasing order of frequency
        # return the top k elements in the results array
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        # 1 -> 1, 2 -> 2, 3 -> 3, 4 -> 3

        frequency = [[] for _ in range(len(nums) + 1)]
        
        for key, value in seen.items():
            frequency[value].append(key)
        #[[], [1], [2], [3, 4]]
        results = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in range(len(frequency[i])):
                if k > 0:
                    results.append(frequency[i][j])
                    k -= 1
        return results



                


