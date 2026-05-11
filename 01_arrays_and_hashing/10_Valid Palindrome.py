class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, otherwise return false.

        A palindrome is a string that reads the same forward and backward. 
        It is also case-insensitive and ignores all non-alphanumeric characters.

        Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
        """
        # remove the non-alphanumeric characters (includes white spaces) and make alphanumerics lowercase 
        # s_list = [char if char.isnumeric() or char.isalpha() else "" for char in s] # don't include an empty space for removed characters, introduces assymetry
        s_list = [char.lower() for char in s if char.isnumeric() or char.isalpha()]

        # https://www.geeksforgeeks.org/python/string-slicing-in-python/
        return s_list == s_list[::-1]