"""
Problem statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
"""

from typing import List, Dict, Set, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n*log(n))
        # hash all the values and save the lowest index where they are. 
        # since they are sorted the first value will identify ALL of the indices for a given value
        nums_dict: Dict[int, int] = {} # {key,val} are {num,idx in nums}
        for idx, num in enumerate(nums):
            if nums_dict.get(num, None) == None:
                nums_dict[num] = idx

        outputs: Set[Tuple[int, int, int]] = set()
        # range over all the unique index pairs in numss
        for i in range(len(nums)):
            num_i = nums[i]
            for j in range(i + 1, len(nums)):
                print(f"(i,j,k)= ({i},{j},k)")
                num_j = nums[j]
                candidate_num_k_val = -(num_i + num_j)
                if candidate_num_k_val in nums_dict:
                    cur_k = nums_dict[candidate_num_k_val]
                    print(f"\tcur_k = {cur_k}")
                    cur_candidate_output = [num_i, num_j, candidate_num_k_val]
                    cur_candidate_output.sort()
                    cur_candidate_output = tuple(cur_candidate_output)


                    if cur_candidate_output not in outputs:
                        
                        # see if we can make the indices unique, we know that i and j are not equal from 
                        # the outer for loops structure. we just need to increment cur_k up to two times
                        # to avoid duplicate
                        if cur_k == i or cur_k == j:
                            print(f"\t\t cur_k = {cur_k}, avoid dupicate indices")
                            cur_k += 1
                            if cur_k == i or cur_k == j:
                                print(f"\t\t cur_k = {cur_k}, avoid dupicate indices again")
                                cur_k += 1
                        
                        if cur_k < len(nums): # ensure cur_k in bounds
                            if nums[cur_k] == candidate_num_k_val:
                                outputs.add(cur_candidate_output) # type: ignore

        return [[output[0], output[1], output[2]] for output in outputs]


class Solution_BAD_v2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        this solution is bad since sometimes you need two of the same number to get to zero,
        but i hash away all duplicates. perhaps we should store ALL the indices for a repeat. then,
        we can reference all of them when we need it?

        but that still doesnt quite do it. what would we do with the list of indices after? we'd have
        to range through that list and make sure none of the 3-tuples formed by choosing 1 is already in 
        our output list. and then we have to manage dealing with all of the indices for each key every time.
        """

        # remove duplicates and hash the numbers. O(n)
         # nums_dict keys are all the unique numbers from nums, and value is the highest index where a value occured
        nums_dict: Dict[int, Set[int]] =  {}
        
        for i in range(len(nums)):
            if nums_dict.get(nums[i], None) == None:
                nums_dict[nums[i]] = set()
            nums_dict[nums[i]].add(i)
   
        output: Set[Tuple[int, int, int]] = set()
        for num_key_i in nums_dict.keys():
            for num_key_j in nums_dict.keys():
                num_key_k_candidate = -num_key_i - num_key_j
                
                # only perform the operation if we have a candidate
                if nums_dict.get(num_key_k_candidate, None) != None:
                    available_indices = nums_dict[num_key_k_candidate]
                    # get a unique len 3 list or stop
                    for cur_available_index in available_indices:
                        candidate_3_list_indices = [nums_dict[num_key_i], nums_dict[num_key_j], cur_available_index]
                        if len(set(candidate_3_list_indices)) == 3: # check all unique indices
                            candidate_3_list = [num_key_i, num_key_j, num_key_k_candidate]
                            candidate_3_list.sort()
                            output.add(tuple(candidate_3_list)) # type: ignore
                            break # only need it once


        return [[cur_tuple[0], cur_tuple[1], cur_tuple[2]] for cur_tuple in output]
   
class Solution_BAD_v1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        this solution is bad since sometimes you need two of the same number to get to zero,
        but i hash away all duplicates. perhaps we should store ALL the indices for a repeat. then,
        we can reference all of them when we need it?

        but that still doesnt quite do it. what would we do with the list of indices after? we'd have
        to range through that list and make sure none of the 3-tuples formed by choosing 1 is already in 
        our output list
        """

        # remove duplicates and hash the numbers. O(n)
         # nums_dict keys are all the unique numbers from nums, and value is the highest index where a value occured
        nums_dict: Dict[int, int] =  {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i # for repeated values in nums, the highest index with that value will be saved.

        output: Set[Tuple[int, int, int]] = set()
        for num_key_i in nums_dict.keys():
            for num_key_j in nums_dict.keys():
                num_key_k_candidate = -num_key_i - num_key_j
                
                # only perform the operation if we have a candidate
                if nums_dict.get(num_key_k_candidate, None) != None:
                    # make sure the indices are unique
                    if self.check_indices_unique(nums_dict, num_key_i, num_key_j, num_key_k_candidate):
                        next_output: List[int] = [num_key_i, num_key_j, num_key_k_candidate] # type: ignore
                        next_output.sort() # type: ignore
                        next_output: Tuple[int, int, int] = tuple(next_output) # type: ignore
                        output.add(next_output)

        return [[cur_tuple[0], cur_tuple[1], cur_tuple[2]] for cur_tuple in output]
        
    def check_indices_unique(self, nums_dict: Dict[int, int], num_key_i, num_key_j, num_key_k: int) -> bool:
        cur_indices_set = set((nums_dict[num_key_i], nums_dict[num_key_j], nums_dict[num_key_k]))
        if (len(cur_indices_set) == 3):
            return True
        
        return False
    
if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]

    nums = [0 for i in range(1,20)]
    print(Solution().threeSum(nums))