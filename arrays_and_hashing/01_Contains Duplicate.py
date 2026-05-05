from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set removes duplicates
        return len(nums) == len(set(nums))