class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we need to count the frequency of elements in this nums array
        # iterate the list check the 'seen' dictionary if key exists -> increment the value. Otherwise, just create a new key with 1 value
        # initialize a results list, each element of the results list would be key, value pair
        # iterate the key value pair in dict
        # find the position in the results array, results array should contain value with decreasing order of frequency
        # return the top k elements in the results array
        seen = defaultdict(int)
        frequency = [[] for _ in range(len(nums) + 1)]
        results = []
        for i in nums:
            seen[i] += 1
        # group all elements with same frequency together
        for key, value in seen.items():
            frequency[value].append(key)
        # find the top k elements
        for elements in frequency[::-1]:
            # make sure we can add something to results
            if k == 0:
                break;
            for i in elements:
                if k > 0:
                    results.append(i)
                    k -= 1
        return results
                


