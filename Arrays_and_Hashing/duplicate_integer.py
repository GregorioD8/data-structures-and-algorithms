from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums) # set has unique elements

print(hasDuplicate([1,2,3,4,5])) # Expected False
print(hasDuplicate([1,2,3,4,5,5])) # Expected True

###Notes
# I chose the other solution for readability, brevity and more pythonic

# A little more efficient for large amounts of data
# checks 
# Time: O(n)
# Space: O(n)
#
# def hasDuplicate(self, nums: List[int]) -> bool:
#     seen = set()
#     for num in nums:
#         if num in seen: #will only return true if duplicate in seen
#             return True
#         seen.add(num)
#     return False