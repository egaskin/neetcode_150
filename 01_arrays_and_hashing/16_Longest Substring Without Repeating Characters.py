class Solution_SlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 1
        char_set = set(s[l])
        max_window_size = 0
        max_window_indices = (0, 1)
        for r in range(1, len(s)):
            print(f"\t IN LOOP: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}, s[l] = {s[l]}, s[r] = {s[r]}")
            if s[r] in char_set: # we can remove s[l] from set and increment l
                char_set.remove(s[l])
                l += 1

            # always add s[r]. this may replace s[l] if s[l] = s[r]
            char_set.add(s[r])

            if max_window_size < r - l + 1:
                max_window_size = r - l + 1
                max_window_indices = (l, r)
        print(f"\t END LOOP: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}")
        print(f"best substring: {s[max_window_indices[0]:max_window_indices[1]+1]}")
        return len(s[max_window_indices[0]:max_window_indices[1]+1])


class Solution_BruteForceKinda:
    """
    this solution builds a substring for each position in the string
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
       
        best_substring = ""
        # for each starting position in the string, build out the substring until 
        # duplicates have been found
        for i in range(len(s)):
            # print(f"i = {i}")
            j = i
            cur_set = set(s[i])
            prev_set_len = -1
            

            # incrementally build the substring until a duplicate encountered
            while prev_set_len != len(cur_set):
                # print(f"\tIN LOOP: j = {j}, cur_set = {cur_set}")
                if j >= len(s) - 1:
                    j += 1
                    break
                prev_set_len = len(cur_set) # get the length before attempting
                cur_set.add(s[j + 1]) # attempt to add to the set
                j += 1 # increment to the next value, s[j+1] will be the latest letter added to the set
                

            # print(f"\tEND OF LOOP: j = {j}, cur_set = {cur_set}")

            if len(cur_set) > len(best_substring):
                # FUTURE IMPROVEMENT: save best indices i and j instead of the actual substring
                # FUTURE IMPROVEMENT: save all the indices that qualify (if the best substring without duplicate happens >1)? currently the first one found is saved since "len(cur_set) > len(best_substring)" is used
                best_substring = s[i:j] # j will be 1 greater than the stopping point, so this is good

        print(f"best_substring = {best_substring}")

        return len(best_substring)
if __name__ == "__main__":
    # s = "x"
    s = "zxyzxyz"
    # s = "xxxx"
    print(f"s = {s}")
    # Solution_BruteForceKinda().lengthOfLongestSubstring(s)
    Solution_SlidingWindow().lengthOfLongestSubstring(s)