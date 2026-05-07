class Solution_2:
    def isAnagram(self, s: str, t: str) -> bool:

        # sorted() splits a string into consitutent characters and sorts the list
        # if they are different lengths, comparison of lists will be false
        return sorted(s) == sorted(t)

class Solution_1:
    def get_kmer_dict(self, some_string, k = 1):

        kmer_dict = {}
        # sliding window
        for i in range(len(some_string) - k + 1):
            substring = some_string[i:i+k]
            kmer_dict[substring] = kmer_dict.get(substring, 0) + 1

        return kmer_dict

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_s: dict = self.get_kmer_dict(s, k = 1)
        counts_t: dict = self.get_kmer_dict(t, k = 1)

        for kmer in counts_s:
            if counts_t.get(kmer, 0) != counts_s[kmer]:
                return False
            
        return True

class Solution_BAD_v1:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        I'm proud of myself for catching this and thinking of the edge case that would break this.
        """

        """
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

        WHY BAD? t = "abbc" s = "abcc" would pass this, they have the same length and same set of characters. we also need to consider
        the freqency of each
        """

        # check same length, if they are not, then cannot be anagram
        if len(s) != len(t):
            return False
        
        # assert that 
        # now that we know they are same length, just make sure every character in s is in t
        for i in s:
            # if a character from s is not in t, then cannot be anagram
            if i not in t:
                return False
        
        # if strings have same length and the same set of characters
        return True
    
if __name__ == "__main__":
    print(Solution_1().get_kmer_dict("abcddda"))
    
    # test different lengths
    print(Solution_2().isAnagram("abcddda", "abcddd"))