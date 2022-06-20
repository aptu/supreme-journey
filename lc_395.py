import pytest

# Longest substring with at least K repeating characters
# Given a string s and an integer k, return the length of the longest substring of s
# such that the frequency of each character in this substring is greater than or equal to k.

from collections import Counter

def longestSubstring(s, k):
    if k > len(s):
        return 0
    freq = Counter(s)
    print(freq)

    for i in freq:
        if freq[i] < k:
            # print(s.split(i))
            return max(longestSubstring(p, k) for p in s.split(i))

    return len(s)



def main():
    print(longestSubstring("ababacb", 3))  # == 0
    print(longestSubstring("aaabb", 3)) #== 3
    print(longestSubstring("ababbc", 2)) #== 5

main()

def test():
    assert (longestSubstring("ababacb", 3) == 0)
    assert(longestSubstring("aaabb", 3) == 3)
    assert(longestSubstring("ababbc", 2) == 5)