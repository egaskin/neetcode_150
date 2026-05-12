"""
Problem statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
"""

from typing import List, Dict, Set, Tuple

class Solution:
    def twoSum(self, A: List[int], T: int) -> List[List[int]]:
        """
        using hints 1 to 3. time complexity is O(n) since we consider a single pair at a time while
        decreasing the items we consider by 1 each iteration starting with n items. that means we will
        consider at most n pairs.
        """
        print("\tSTART: TwoSum")
        L = 0
        R = len(A) - 1
        candidate_sum = A[L] + A[R]
        all_pairs = []
        while L < R:

            print(f"\tA[L]=A[{L}]={A[L]}, A[R]=A[{R}]={A[R]}, A[L] + A[R] = {A[L] + A[R]}, A[L:R+1] = A[L:R+1]")
            print(f"\t\tlen(A[L:R+1]) = {len(A[L:R+1])}")
            # if the largest number plus smallest number is bigger than target, then
            # sum cant use largest number. since all other numbers will be bigger than smallest
            if candidate_sum > T:
                R = R - 1
            elif candidate_sum < T:
                L = L + 1 # similar logic. smallest number cant be in any pair
            else: # if their equal, keep going!
                all_pairs.append([L + 1, R + 1])
                R -= 1
                L += 1

            candidate_sum = A[L] + A[R]

        # check the very iteration
        if candidate_sum == T and L != R:
            all_pairs.append([L + 1, R + 1])

        if len(all_pairs) == 0:
            print(f"\tRETURN: {None}")
            # handle cases where no target is found in the array
            return None # type: ignore
        print(f"\tRETURN: all_pairs = {all_pairs}")
        return all_pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        two-pointer version. we know that nums[i] + nums[j] + nums[k] == 0, so thus
        nums[k] = -(nums[i] + nums[j]). after sorting, we can apply two pointer with nums[k] as the target
        and everything with larget indices as containing potential solution pairs
        """
        nums.sort()
        outputs: List[List[int]] = []
        # for idx_k, num_k in enumerate(nums):
        for idx_k in range(len(nums) - 1):
            
            num_k = nums[idx_k]
            print(f"nums[idx_k] = nums[{idx_k}] = num_k = {num_k}")
            if num_k > 0:
                break 
                # after considering all the non-positives (negatives and zero), we will have covered all the solutions
                # containing positive values. stop early
            
            # note: we can get a decent speedup by only considering indices
            # greater than idx_k. we just need to add that startgin value back
            # in to any solutions found when using the nums[idx_k+1:] slice.
            all_candidate_idx_pair = self.twoSum(A = nums[idx_k+1:], T = -num_k)
            if all_candidate_idx_pair != None:
                for candidate_idx_pair in all_candidate_idx_pair:
                        candidate_idx_pair[0] += idx_k
                        candidate_idx_pair[1] += idx_k  
                        output = [num_k, nums[candidate_idx_pair[0]], nums[candidate_idx_pair[1]]]
                        output.sort()  
                        outputs.append(output)
                        # # ensure all 3 indices are unique
                        # if (len(set((candidate_idx_pair[0], candidate_idx_pair[1], idx_k))) == 3):
                        #     output = [num_k, nums[candidate_idx_pair[0]], nums[candidate_idx_pair[1]]]
                        #     output.sort()
                        #    outputs.append(output)
        print(f"outputs = {outputs}")
        # return outputs
        # remove duplicates
        outputs_set: Set[Tuple] = {(output[0], output[1], output[2]) for output in outputs}
        return [[output[0], output[1], output[2]] for output in outputs_set]
        
        
        
        

class Solution_HashTables: # using dict and set
    """
    I believe this solution is O(n^2) time complexity, O(n) additional space for nums. This additional space
    is above the goal space complexity for the problem statement.
    """

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

    nums = [-2,0,1,1,2] # this test case tests if algorithm can detect when a single nums[i] is used for multiple solutions

    nums=[-1,0,1,0]
    print(f"nums = {nums}")
    print("-----")
    print(Solution().threeSum(nums))