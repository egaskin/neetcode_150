class Solution_BruteForce:
    """
    for every position in the string, try to build the longest string with a single unique letter
    """
    def characterReplacement(self, s: str, k: int) -> int:
        max_window_length = 0
        max_window_indices = (0, 0)
        for L in range(len(s)):
            uniques_so_far = 1 # allows us to start R = L + 1
            print(f"L = {L}")
            for R in range(L + 1, len(s)):
                print(f"\t R = {R}")
                if s[L] != s[R]:
                    uniques_so_far += 1

                if uniques_so_far > k:
                    break
                
                # only consider the substring defined by s[L:R] if s[R] is 
                # NOT a unique val that causes uniques_so_far > k
                cur_window_length = R - L + 1 
                if cur_window_length > max_window_length:
                    max_window_length = cur_window_length
                    max_window_indices = (L, R)
        print(f"best substring: {s[max_window_indices[0]:max_window_indices[1]+1]}")
        return len(s[max_window_indices[0]:max_window_indices[1]+1])
                

class Solution_SlidingWindow:
    """
    Solution is based on neetcode's solution.

    """
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 1
        char_set = set(s[l])
        max_window_size = 0
        max_window_indices = (0, 0)
        unique_so_far = 0
        for r in range(1, len(s)):
            print(f"\t START OF LOOP: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}, s[l] = {s[l]}, s[r] = {s[r]}")
            while unique_so_far < k: # we can remove s[l] from set and increment l
                print(f"\t\twhile loop: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}, s[l] = {s[l]}, s[r] = {s[r]}")
                char_set.remove(s[l]) # s[r] MUST EQUAL s[l]
                l += 1

            # always add s[r]. this may replace s[l] if s[l] = s[r] (in which case s[l] was removed in the previous if statement)
            char_set.add(s[r])

            if max_window_size < r - l + 1:
                max_window_size = r - l + 1
                max_window_indices = (l, r)
            print(f"\t END OF LOOP: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}, s[l] = {s[l]}, s[r] = {s[r]}\n")
        print(f"\t AFTER LOOP: l = {l}, r = {r}, char_set = {char_set}, max_window_size = {max_window_size}")
        print(f"best substring: {s[max_window_indices[0]:max_window_indices[1]+1]}")
        return len(s[max_window_indices[0]:max_window_indices[1]+1])

if __name__ == "__main__":
    s = "XYYX"
    k = 2
    # s = "AAABABB"
    # k = 1
    s = "ABCDADCBAA"
    # s = "ABCDADCABAAA"
    k = 1
    print(f"s = {s}, k = {k}")
    print(f"ANSWER: {Solution_BruteForce().characterReplacement(s, k)}")