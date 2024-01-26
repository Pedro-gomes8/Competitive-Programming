"""
Given two strings, write a method to decide if one is permutation of another
O(N) implementation where N is the size of both strings.
Returns false immediately if the size of the strings are different
"""


def checkPermutation(firstString: str, secondString: str) -> bool:
    # If both string have not the same length, no need to check
    if len(firstString) != len(secondString):
        return False

    # Hashmap to keep track of frequency
    charFrequency = {}
    for char in firstString:
        charFrequency.setdefault(char, 0)
        charFrequency[char] += 1

    # Checks second string for character in hashmap
    for char in secondString:
        # If it's not a character that the hashmap knows, return false
        if charFrequency.get(char):
            charFrequency[char] -= 1
            if charFrequency[char] < 0:
                return False
        else:
            return False

    return True
