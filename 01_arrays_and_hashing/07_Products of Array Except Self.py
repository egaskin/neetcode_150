from typing import List

class Solution_Fancy:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        fancy solution based on hints 1 to 3
        """
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        # skip the first value of prefix and suffix, this will be 1.
        for i in range(1, len(nums)):
            # cumulative products forward. value nums[n-1] will never be included
            prefix[i] = nums[i-1] * prefix[i-1]

            # cumulative products backwards. value nums[0] will never be included
            suffix[i] = nums[len(nums)-i] * suffix[i-1]
        print(f"prefix = {prefix}")
        print(f"suffix = {suffix}")

        output = [0]*len(nums)
        # now, multiply the forward and backwards products, but range over suffix backwards.
        for i in range(0, len(nums)):
            output[i] = prefix[i] * suffix[len(nums)-i-1]
        return output


class Solution_Division:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution using division by treating the problem as 3 cases (how many zeroes are present):

        (1) if there's no zeros, its easy. get total product, output[i] = total_product/nums[i]

        (2) if there's a single zero at index k, then output[i] = 0 for all i except i = k, output[k] = product of nums[j] for all i != j

        (3) if there's more than 1 zero, then output[i] = 0 for all i. why? since there will always be some other number that is 0 when considering the output for nums[i]

        """
        # check how many zeros are in the list
        count_zeros = sum([1 if num == 0 else 0 for num in nums])

        if count_zeros == 0:
            total_product = 1
            for num in nums:
                total_product *= num

            # integer division to ensure List[int]
            return [total_product//num for num in nums]

        elif count_zeros == 1:
            
            total_product = 1

            for num in nums:
                # skip the zero!
                if num != 0:
                    total_product *= num

            # output[i] = 0 if nums[i] != 0, otherwise its total_product skipping the zero
            return [0 if num != 0 else total_product for num in nums]

        else:
            return [0 for num in nums]

class Solution_BruteForce:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        products = [1]*len(nums)
        for i, _ in enumerate(nums):
            for j, num_j in enumerate(nums):
                if i != j:
                    products[i] *= num_j

        return products

class Solution_AI:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

        Each product is guaranteed to fit in a 32-bit integer.

        Follow-up: Could you solve it in
        O(n) time without using the division operation?
        """
        left = [1]
        right = [1]
        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])
            right.append(right[i-1] * nums[len(nums)-i])
        return [left[i] * right[len(nums)-i-1] for i in range(len(nums))]