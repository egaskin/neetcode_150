from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return "_".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("_")
