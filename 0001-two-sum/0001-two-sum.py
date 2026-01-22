class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            sub = target - num
            if sub in map:
                return [map.get(sub), i]
            map[num] = i