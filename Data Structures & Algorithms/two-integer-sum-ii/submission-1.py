class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = defaultdict(int)

        for idx, val in enumerate(numbers):
            if visited.get(val):
                return [visited[val], idx+1]
            else:
                visited[target - val] = idx+1



        
        #　因為題目要求使用Space: O(1)