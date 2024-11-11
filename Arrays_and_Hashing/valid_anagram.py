from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

print(isAnagram("racecar", "carrace")) # Expected value: True
print(isAnagram("abcd", "accc"))


### Notes ###

## Solution 1: Using collections.Counter
# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(k), where k is the number of unique characters in the strings.
# Use Case: Ideal for scenarios involving single words or short phrases.
# Reasoning: This Pythonic approach prioritizes readability and brevity, making it suitable when space complexity is not a primary concern.

## Solution 2: Using a Fixed-Size List for Character Counting
# Time Complexity: O(n), where n is the length of the strings.
# Space Complexity: O(1), due to the fixed-size list of 26 elements (assuming only lowercase English letters).
# Use Case: Optimal for scenarios requiring high efficiency and scalability, such as processing large texts or datasets.
# Reasoning: This approach offers superior space efficiency, making it well-suited for performance-critical applications, including those in AI and machine learning domains.
#
# def is_anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = [0] * 26  # Assuming only lowercase English letters
#     for char in s:
#         count[ord(char) - ord('a')] += 1
#     for char in t:
#         count[ord(char) - ord('a')] -= 1
#
#     return all(x == 0 for x in count)