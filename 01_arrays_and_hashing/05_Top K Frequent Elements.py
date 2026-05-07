from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        alternatively could we sort it as we get the frequencies?
        """
        nums_dict: dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        print(f"BEFORE nums_dict = {nums_dict}")
        nums_dict = {k: v for k, v in sorted(nums_dict.items(), key=lambda item: item[1], reverse = False)}
        print(f"AFTER nums_dict = {nums_dict}")

        return list(nums_dict.keys())[-k:]

if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    nums = nums[::-1]
    k = 2
    print(Solution().topKFrequent(nums, k))