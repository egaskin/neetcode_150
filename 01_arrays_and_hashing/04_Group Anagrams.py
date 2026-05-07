from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        """
        # to group all the strings that can be anagrams, lets use a dictionary with a key unique to a given anagram set.
        # by definition anagrams have to have the same set of characters. if we sort that list of characters this can be 
        # the key identifies all strings belonging to an anagram group 
        answers_dict = {}
        for cur_str in strs:
            # split the string, sort it, and then covert back into a string and attempt fetching from dict
            split_sorted_string = "".join(sorted(cur_str))
            # print(split_sorted_string)
            # get the existing list, or make an empty one if there isn't one, then append the current string to it
            answers_dict[split_sorted_string] = answers_dict.get(split_sorted_string, []) + [cur_str]

        # convert the dictionary to a list of anagram lists (each key matches to a value that is an anagram list)
        return [list(answers_dict[key]) for key in answers_dict.keys()]

if __name__ == "__main__":
    print(Solution().groupAnagrams(["abcddda", "abcdadd", "abcdad"]))