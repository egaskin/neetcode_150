"""
Problem statement:
You are given an integer array heights where heights[i] represents the height of the 
i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_area = -1
        best_pair = None
        while L < R:
            area = (R - L)*min(heights[L], heights[R])
            if area > max_area:
                best_pair = [L, R]
                max_area = area
            
            # we can always decrease the number of items from heights being
            # considered by 1 by removing the smaller height. the smaller
            # height will contribute the most by using the largest width possible
            # which we maximize by setting L and R equal to the ends of the current
            # slice being considered. for instance, if the smallest height is 
            # at heights[0] then the max area it can contribute comes from using
            # heights[n-1] as it's partner. we no longer need to consider heights[0] 
            # after that (any other pair with heights[0] will have smaller area)
            if heights[R] < heights[L]: 
                R -= 1
            else:
                L += 1 # also do when heights[R] and heights[L] are equal
            
        return max_area
class Solution_BruteForce:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        best_idx = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)

                # max_area = max(max_area, area)
                if max_area < area:
                    max_area = area
                    best_idx = [i, j]
        print(f"best_idx = [i, j] = [{best_idx[0]}, {best_idx[1]}], max_area = {max_area}")
        return max_area
    
import pytest # type: ignore
@pytest.mark.parametrize(
    "heights,result", 
    [
        # format of test cases:
        # (heights, result)

        # ensure works on easy scenario all heights same v1
        ([2,2], 2), 
        
        # ensure works on easy scenario all heights same v2, add more bars
        ([2,2,2,2], 6),
        
        # ensure works when bar heights are different
        ([2,2,2,3], 6), 

        # neetcode test case 1, many different heights
        ([1,7,2,5,4,7,3,6], 36), 

        # ensure selects a "wide" rectangle over a "tall" rectangle appropriately
        # instead of rectangle defined by heights[0], heights[4]
        # chooses rectangle defined by heights[0], heughts[9]
        ([2,1,1,1,2,1,1,1,1,1], 9),

        # instead rectangle heights[1], heights[8]
        # chooses rectangle heights[0], heights[37]
        ([1, 7, 2, 5, 4, 7, 3, 6, 
          1, 1, 1, 1, 1, 1, 1, 1, 
          1, 1, 1, 1, 1, 1, 1, 1, 
          1, 1, 1, 1, 1, 1, 1, 1, 
          1, 1, 1, 1, 1, 1], 
          37)
    ]
)
def test_maxArea(heights, result):
    assert (Solution().maxArea(heights) == result)

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))