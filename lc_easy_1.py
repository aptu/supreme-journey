from heapq import *


#316. remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order
def smallestSubsequence(s):
    stack = []
    for i in range(len(s)):
        letter = s[i]
        if letter in stack:
            continue
        else:
            while (stack and stack[-1] >= s[i]):
                last = stack[-1]
                # more of those chars later?
                if last in s[i+1:]:
                    stack.pop()
                else:
                    break
        stack.append(letter)
    return "".join(stack)

# third max number from ARRAYS EXPLORE
def third_max(nums):
    minheap = []

    if len(set(nums)) < 3:
        return max(nums)
    else:
        i = 0
        while len(minheap) < 3:
            if nums[i] not in minheap:
                heappush(minheap,  nums[i])
            i += 1
        for j in range(i, len(nums)):
            num = nums[j]
            if num not in minheap and num > minheap[0]:
                heappop(minheap)
                heappush(minheap, nums[j])
        return minheap[0]


if __name__=='__main__':
    print(smallestSubsequence("bcabc"))
    print(smallestSubsequence("cbacdcbc"))

    print(third_max([3, 2, 1])) # 1
    print(third_max([1, 1, 2]))  #2
    print(third_max([2, 2, 3, 1])) #1
    print(third_max([1, 2, 2, 5, 3, 5])) #2