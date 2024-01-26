"""
Implement an algorithm to determine if a string has all unique characters. What to do if you cannot use additional data structures?

Thoughts: BCR is O(n)
Ideas: Hash table -> set, later, check if set has the same length

"""


def uniqueCharacters(string: str) -> bool:
    uniqueChars = set(string)
    if len(uniqueChars) == len(string):
        return True
    return False


def noDataStruct(string: str) -> bool:
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


testCases = ["abcdefg", "aabcdfeg", "sddwfv", "hgpknlm"]

for test in testCases:
    print(noDataStruct(test))
