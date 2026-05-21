"""
https://en.wikipedia.org/wiki/Binary_search
"""
from typing import List, Union
def binary_search(A: List[int], T: int, is_sorted: bool = False) -> Union[int, None]:
    """
    return the index m where A[m] = T, or None if T is not in A.
    """

    if not is_sorted:
        A.sort()

    L = 0
    R = len(A) - 1
    while L <= R:
        m = L + (L + R)//2

        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
        
    return None
        