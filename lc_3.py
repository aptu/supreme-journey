import pytest

# 3. Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
    maxlen = 0
    start = 0
    freq = set()
    for end in range(len(s)):
        end_ch = s[end]
        while end_ch in freq:
            freq.remove(s[start])
            start += 1

        freq.add(end_ch)
        maxlen = max(maxlen, end - start + 1)
    return maxlen

def main():
    print(lengthOfLongestSubstring("abcabcbb"))  #

def test():
    assert(lengthOfLongestSubstring("abcabcbb") == 3)
