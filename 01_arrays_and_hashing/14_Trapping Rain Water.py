"""
Problem statement:

You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
-----
Example 1:

https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/0c25cb81-1095-4382-fff2-6ef77c1fd100/public

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
"""
from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        using hints 1 and 2. we have the formula

        trapped_water[i] = min(heights[l], heights[r]) - heights[i]

        now we just need to know how to define and increment l and r.
        """

        pass

class Solution_BAD_v2:
    def trap(self, heights: List[int]) -> int:
        """
        this method + formula doesnt work for sub regions like
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]
        heights[9:12] = [2,1,2]

        my method ends up spilling this over the edge rather than accounting 
        for the 1 that's supposed to accumulate at heights[9]
        """
        # ensure the ends will make water "fall off"
        heights.insert(0,0)
        heights.append(0)
        print(f"""
after prepend and append, 
heights = {heights},
indices = {[i for i in range(len(heights))]}
""")
        total_water_trapped: int = 0
        idx_region_start: int = 0
        idx_region_end: int = idx_region_start + 1
        total_heights_in_region: int = 0
        while idx_region_start < len(heights)-1:
            print("-----")
            print(f"total_water_trapped = {total_water_trapped}, idx_region_start = {idx_region_start}, idx_region_end = {idx_region_end}, total_heights_in_region = {total_heights_in_region}")
            # check if a region ends
            if (
                heights[idx_region_start] <= heights[idx_region_end] or 
                idx_region_end == len(heights)-1
            ):
                print("new region starts")
                width = idx_region_end - idx_region_start - 1
                print(f"width = {width}")
                if width > 0:
                    if idx_region_start != 0 and idx_region_end != len(heights)-1:
                        total_water_trapped += (width)*min(
                            heights[idx_region_start], heights[idx_region_end]
                        ) - total_heights_in_region
                    elif idx_region_start == 0:
                        print("idx_region_start == 0")
                        # special_end = idx_region_end
                    elif idx_region_end == len(heights)-1:
                        print(f"idx_region_end == len(heights)-1 == {len(heights)-1}")
                        # special_start = idx_region_start
                # reset and perform the operation again for next region
                idx_region_start = idx_region_end
                idx_region_end = idx_region_start + 1
                total_heights_in_region = 0
            else:
                # add the height from the region to the running total
                total_heights_in_region += heights[idx_region_end]
                idx_region_end += 1
        print("---- final")
        print(f"total_water_trapped = {total_water_trapped}, idx_region_start = {idx_region_start}, idx_region_end = {idx_region_end}, total_heights_in_region = {total_heights_in_region}")
        return total_water_trapped
   
class Solution_BAD_v1:
    def trap(self, heights: List[int]) -> int:
        """
        issue is im not taking into account when water should fall of the start or end
        """
        idx_overall_start: int = 0

        # find the first height where there are either 
        for i in range(len(heights)):
            if heights[i] > 0:
                idx_overall_start = i
                break
        
        idx_overall_end: int = 0
        for j in range(len(heights)-1,-1,-1):
            if heights[j] > 0:
                idx_overall_end = j
                break

        total_water_trapped: int = 0
        idx_region_start: int = idx_overall_start
        idx_region_end: int = idx_region_start + 1
        total_heights_in_region: int = 0
        while idx_region_start < idx_overall_end:
            print("-----")
            print(f"total_water_trapped = {total_water_trapped}, idx_region_start = {idx_region_start}, idx_region_end = {idx_region_end}, total_heights_in_region = {total_heights_in_region}")
            # check if a region ends
            if (
                heights[idx_region_start] <= heights[idx_region_end] or 
                idx_region_end == idx_overall_end
            ):
                print("new region starts")
                width = idx_region_end - idx_region_start - 1
                print(f"width = {width}")
                if width > 0:
                    total_water_trapped += (width)*min(
                        heights[idx_region_start], heights[idx_region_end]
                    ) - total_heights_in_region
                # reset and perform the operation again for next region
                idx_region_start = idx_region_end
                idx_region_end = idx_region_start + 1
                total_heights_in_region = 0
            else:
                # add the height from the region to the running total
                total_heights_in_region += heights[idx_region_end]
                idx_region_end += 1
        print("---- final")
        print(f"total_water_trapped = {total_water_trapped}, idx_region_start = {idx_region_start}, idx_region_end = {idx_region_end}, total_heights_in_region = {total_heights_in_region}")
        return total_water_trapped
    

import pytest # type: ignore
@pytest.mark.parametrize(
    "heights,result", 
    [
        # format of test cases:
        # (heights, result)

        # test case 1 from neetcode
        ([0,2,0,3,1,0,1,3,2,1], 9), 

        # test - all bars
        ([1,1,1,1,1,1,1,1,1,1], 0),

        # test - no bars
        ([], 0),

        # test 1 bar
        ([1], 0),

        # test - normal distribution
        ([0,1,2,3,4,3,2,1,0], 0),

        # test case 2 from neetcode
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6)
    ]
)
def test_trap(heights, result):
    assert (Solution().trap(heights) == result)

if __name__ == "__main__":
    
    # print(Solution().trap([0,2,0,3,1,0,1,3,2,1]))
    print(Solution().trap(heights=[0,1,0,2,1,0,1,3,2,1,2,1]))
    # raise SystemExit(pytest.main([__file__]))