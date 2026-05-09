from typing import List, Dict

class Solution_dict: # O(n^2) time complexity is list concatenation vs O(n) for append. why?
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict: Dict[int, List[int]] = {nums[i]:[int()] for i in range(len(nums))} 
        starts = self.identify_starts(nums_dict)
        # print(starts)
        for start in starts:
            nums_dict[start][0] = start
            print(f"start = {start}, nums_dict[start] = {nums_dict[start]}")
            next_val = start + 1
            while nums_dict.get(next_val, None) != None:

                # # https://pythoncomplexity.com/builtins/list/#complexity-reference
                # # RESULTS in O(n^2) since list concatenation is O(n + m)
                # nums_dict[start] = nums_dict[start] + [next_val] 

                # RESULTS in O(n) since append is amortized O(1)
                nums_dict[start].append(next_val) 
                next_val += 1
                print(f"\tnums_dict[start] = {nums_dict[start]}")

        best_length = float('-inf')
        best_key = int()
        for nums_key, consecutive_sequence in nums_dict.items():
            if len(consecutive_sequence) > best_length:
                best_key = nums_key
                best_length = len(consecutive_sequence)

        return len(nums_dict.get(best_key, []))


    def identify_starts(self, nums_dict: Dict[int, List[int]]) -> List[int]:
        starts = []
        for num_key in nums_dict:
            # if there is a key that is greater than 1 and no key less than 1, then this is a start
            if nums_dict.get(num_key + 1, None) != None and nums_dict.get(num_key - 1, None) == None:
                starts.append(num_key)

        return starts

class Solution_BAD_v3:
    """
    this solution almost works. but, it turns out that the fixing step really needs to merge the lists for keys 
    where the last element or first element of dict[key] is equal to some key in dict. i think i should just start
    over using the hints!

    so for the n operations done on nums, we occassionally have to range over the entire dict but 
    in general it will be O(1). thus, it's better than O(n^2) since for most of the [1,n] operations performed,
    there will be O(1) look up time; sometimes it will be O(n). but can i gurantee that the overall solution
    iss O(n)?
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        since hashing key lookup is O(n) worst case and O(1) on average, we can
        rely on dicts https://pythoncomplexity.com/builtins/dict/
        """

        # each key represents a growing sequence. the key is the "next" value in the sequence.
        # if nums[i] is the next value in the sequence then pop that key (which returns the val
        # and deletes the key), increment the key, and re-assign the new value
        next_vals_dict: dict = {}
        prev_vals_dict: dict = {}

        # generate the next_vals_dict ranging over nums once
        for num in nums:
            print(f"num = {num}")

            # handle next_vals_dict
            # if the key doesnt exist, initalize it
            if next_vals_dict.get(num, None) == None:
                # we have num, we need to see if some previously seen nums[i] is num+1, so the key is num + 1
                # when we search next_vals_dict to see if num[i] is nums[i]+1 or nums[i]-1 for some previous i, BUT
                # make sure that we don't overwrite a next value for some sequence that is growing which shares a
                # next value with the one we are trying to establish. for instance if 
                # nums = [2,4,10,3,4,5]
                # then next_vals_dict = {3: [2], 1: [2]}
                # and when we consider nums[1] = 4, we need to not overwrite the key 3. this key

                if next_vals_dict.get(num + 1, None) == None:
                    next_vals_dict[num + 1] = [num] 
            
            # last element in the sequence is num - 1, then num is incrementing the sequence
            else:
                # num must be the next val in a sequence such that there is key val pair in
                # next_vals_dict[num] = old_val_list, where
                # num - 1 = old_val_list[-1]

                old_val_list: List[int] = next_vals_dict.pop(num) # get rid of the old key
                next_vals_dict[num + 1] = old_val_list + [num] # insert new key
            
            if prev_vals_dict.get(num, None) == None:
                # print(f"1 we saw this prev_vals_dict = {prev_vals_dict}") 
                if prev_vals_dict.get(num - 1, None) == None:
                    prev_vals_dict[num - 1] = [num]
                    # print(f"2 we saw this prev_vals_dict = {prev_vals_dict}") 
            # num must be the first element in the sequence, so prepend it
            else:
                old_val_list: List[int] = prev_vals_dict.pop(num) # get rid of the old key
                prev_vals_dict[num - 1] =  [num] + old_val_list # insert new key and sequence
            print(f"\tnext_vals_dict = {next_vals_dict}")
            print(f"\tprev_vals_dict = {prev_vals_dict}")

        # cleanup step part 1, 
        # for next val dict, see if key is plus 1 for any other key
        for next_val_key in next_vals_dict.keys():
            if next_vals_dict.get(next_val_key + 1, None) != None:
                # list_to_merge = next_vals_dict.pop(next_val_key + 1)
                next_vals_dict[next_val_key] = next_vals_dict[next_val_key] + next_vals_dict[next_val_key + 1]

        for prev_val_key in prev_vals_dict.keys():
            if prev_vals_dict.get(prev_val_key - 1, None) != None:
                # list_to_merge = prev_vals_dict.pop(prev_val_key - 1)
                prev_vals_dict[prev_val_key] = prev_vals_dict[prev_val_key - 1] + prev_vals_dict[prev_val_key]

        # part 2 - merge the two dictionaries such that the sequences make sense
        final_dict = {}

        # part 3 BAD DONT DO WHILE LOOP- while there are no keys that are 


        # range over the keys and returns the longest one
        max_length = -1
        for next_val_key in next_vals_dict.keys():
            if len(next_vals_dict[next_val_key]) > max_length:
                best_key = next_val_key
                max_length = len(next_vals_dict[next_val_key])
        print(f"next_vals_dict = {next_vals_dict}")
        print(f"prev_vals_dict = {prev_vals_dict}")
        print(f"next_vals_dict[best_key] = {next_vals_dict[best_key]}")
        return len(next_vals_dict[best_key]) # the sequence is next_vals_dict[best_key]


class Solution_BAD_v2:
    """
    this solution almost works. but, it turns out that the fixing step really needs to merge the lists for keys 
    where the last element or first element of dict[key] is equal to some key in dict

    so for the n operations done on nums, we occassionally have to range over the entire dict but 
    in general it will be O(1). thus, it's better than O(n^2) since for most of the [1,n] operations performed,
    there will be O(1) look up time; sometimes it will be O(n). but can i gurantee that the overall solution
    iss O(n)?
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        since hashing key lookup is O(n) worst case and O(1) on average, we can
        rely on dicts https://pythoncomplexity.com/builtins/dict/
        """

        # each key represents a growing sequence. the key is the "next" value in the sequence.
        # if nums[i] is the next value in the sequence then pop that key (which returns the val
        # and deletes the key), increment the key, and re-assign the new value
        next_vals_dict: dict = {}

        # generate the next_vals_dict ranging over nums once
        for num in nums:
            print(f"num = {num}")
            # if the key doesnt exist, initalize it
            if next_vals_dict.get(num, None) == None:
                # we have num, we need to see if some previously seen nums[i] is num+1, so the key is num + 1
                # when we search next_vals_dict to see if num[i] is nums[i]+1 or nums[i]-1 for some previous i, BUT
                # make sure that we don't overwrite a next value for some sequence that is growing which shares a
                # next value with the one we are trying to establish. for instance if 
                # nums = [2,4,10,3,4,5]
                # then next_vals_dict = {3: [2], 1: [2]}
                # and when we consider nums[1] = 4, we need to not overwrite the key 3. this key

                if next_vals_dict.get(num + 1, None) == None:
                    next_vals_dict[num + 1] = [num] 

                if next_vals_dict.get(num - 1, None) == None:
                    next_vals_dict[num - 1] = [num]
            
            # if last element in the sequence is num - 1, then num is incrementing the sequence
            elif next_vals_dict[num][-1] == num - 1:
                # num must be the next val in a sequence such that there is key val pair in
                # next_vals_dict[num] = old_val_list, where
                # num - 1 = old_val_list[-1]

                old_val_list: List[int] = next_vals_dict.pop(num) # get rid of the old key
                next_vals_dict[num + 1] = old_val_list + [num] # insert new key
            
            # num must be the first element in the sequence, so prepend it
            else:
                old_val_list: List[int] = next_vals_dict.pop(num) # get rid of the old key
                next_vals_dict[num - 1] =  [num] + old_val_list # insert new key and sequence
            print(f"\tnext_vals_dict = {next_vals_dict}")

        # one final cleanup step, range over nums one more time, and see if the first or last value
        # in next_vals_dict[key] is nums[i]+1 or nums[i] - 1. if so, append or prepend it
        for num in nums:
            # if True, there was a number in nums which could have been appended or prepended
            if next_vals_dict.get(num, None) != None:
                # check if it should be prepend
                if next_vals_dict[num][0] - 1 == num:
                    next_vals_dict[num] = [num] + next_vals_dict[num]
                else:
                    next_vals_dict[num] = next_vals_dict[num] + [num]
            

        # range over the keys and returns the longest one
        max_length = -1
        for next_val_key in next_vals_dict.keys():
            if len(next_vals_dict[next_val_key]) > max_length:
                best_key = next_val_key
                max_length = len(next_vals_dict[next_val_key])
        print(f"next_vals_dict = {next_vals_dict}")
        print(f"next_vals_dict[best_key] = {next_vals_dict[best_key]}")
        return len(next_vals_dict[best_key]) # the sequence is next_vals_dict[best_key]

class Solution_BAD_v1:
    """
    this solution didn't work because it doesn't consider earlier values in nums as possible
    candidates for the next value in the sequence. for example in [5,4,3,2,3], this algorithm
    would return 2 for the consecutive sequence [2,3] but really the best consecutive sequence is
    [2,3,4,5] and thus it should return 4.
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        since hashing key lookup is O(n) worst case and O(1) on average, we can
        rely on dicts https://pythoncomplexity.com/builtins/dict/
        """

        # each key represents a growing sequence. the key is the "next" value in the sequence.
        # if nums[i] is the next value in the sequence then pop that key (which returns the val
        # and deletes the key), increment the key, and re-assign the new value
        next_vals_dict: dict = {}

        # generate the next_vals_dict ranging over nums once
        for num in nums:
            # if the key doesnt exist, initalize it
            if next_vals_dict.get(num, None) == None:
                # we have num, we need to see if some previously seen nums[i] is num+1, so the key is num + 1
                # when we search next_vals_dict to see if num[i] is nums[i]+1 for some previous i.
                next_vals_dict[num + 1] = [num] 
            else:
                # num must be the next val in a sequence such that there is key val pair in
                # next_vals_dict[num] = old_val_list, where
                # num - 1 = old_val_list[-1]

                old_val_list: List[int] = next_vals_dict.pop(num) # get rid of the old key
                next_vals_dict[num + 1] = old_val_list + [num] # insert new key
    
        # range over the keys and returns the longest one
        max_length = -1
        for next_val_key in next_vals_dict.keys():
            if len(next_vals_dict[next_val_key]) > max_length:
                best_key = next_val_key
                max_length = len(next_vals_dict[next_val_key])
    
        return len(next_vals_dict[best_key]) # the sequence is next_vals_dict[best_key]
    
if __name__ == "__main__":
    
    # nums = [2,20,4,10,3]
    # print(f"nums = {nums}")
    # print(Solution().longestConsecutive(nums))

    # nums = [2,20,4,10,3,4,5]
    # print(f"nums = {nums}")
    # print(Solution().longestConsecutive(nums))

    # nums=[0,3,2,5,4,6,1,1]
    # print(f"nums = {nums}")
    # print(Solution().longestConsecutive(nums))

    # nums = [3, 1, 2, 11, 10, 12]
    # print(f"nums = {nums}")
    # print(Solution().longestConsecutive(nums))

    nums = [i for i in range(20,0,-1)]
    print(f"nums = {nums}")
    print(Solution().longestConsecutive(nums))