from typing import List

"""
Problem statement:
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to 
a given target number target and index1 < index2. Note that index1 and index2 cannot be 
equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O(1) additional space.
"""

class Solution:
    def twoSum(self, A: List[int], T: int) -> List[int]:
        """
        using hints 1 to 3. time complexity is O(n) since we consider a single pair at a time while
        decreasing the items we consider by 1 each iteration starting with n items. that means we will
        consider at most n pairs.
        """

        L = 0
        R = len(A) - 1
        candidate_sum = A[L] + A[R]
        while candidate_sum != T and L < R:
            # print(f"A[L]=A[{L}]={A[L]}, A[R]=A[{R}]={A[R]}, A[L] + A[R] = {A[L] + A[R]}, A[L:R+1] = A[L:R+1]")
            # print(f"\tlen(A[L:R+1]) = {len(A[L:R+1])}")
            # if the largest number plus smallest number is bigger than target, then
            # sum cant use largest number. since all other numbers will be bigger than smallest
            if candidate_sum > T:
                R = R - 1
            elif candidate_sum < T:
                L = L + 1 # similar logic. smallest number cant be in any pair

            candidate_sum = A[L] + A[R]
        # print("FINAL:")
        # print(f"A[L]=A[{L}]={A[L]}, A[R]=A[{R}]={A[R]}, A[L] + A[R] = {A[L] + A[R]}")
        # print(f"\tlen(A[L:R]) = {len(A[L:R+1])}")

        if candidate_sum != T:
            # handle cases where no target is found in the array
            return None # type: ignore
        return [L + 1, R + 1]

    def binarySearch(self, A: List[int], T: int) -> int:
        """
        https://en.wikipedia.org/wiki/Binary_search#Algorithm
        """

        L = 0
        R = len(A) - 1
        while L <= R:
            m = (L + R)//2 # middle element of interval
            if A[m] < T:
                L = m + 1
            elif A[m] > T:
                R = m - 1
            else:
                return m
        return -1

class Solution_BADv1BinarySearchAttempt:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        we have a sorted array. let's do binary search?
        """

        start_idx = 0
        end_idx = len(numbers) - 1

        while (numbers[start_idx] + numbers[end_idx]) != target:
            print(f"start_idx = {start_idx}, end_idx = {end_idx}")
            if target < numbers[start_idx] + numbers[end_idx]:
                end_idx //= 2 # bad because what if the upper half of numbers has the sum
            else:
                start_idx *= 2

        return [start_idx + 1, end_idx + 1]

class Solution_BruteForce:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Brute force 
        """
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                
        return None # type: ignore

if __name__ == "__main__":
    # numbers=[-5,-3,0,2,4,6,8]
    # target=5

    numbers = [i*10 for i in range(26)]
    target = 49*10 # requires 240 + 250 = 490
    print(Solution().twoSum(numbers, target))