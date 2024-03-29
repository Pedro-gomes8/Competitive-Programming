"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

BCR: O(n)

Idea: Necessary to check for each of those operations.
Replace: When we replace a character, the length of both strings will be equal. We then need to check if there are more than 1 different characters.
Insert and remove: Both are basically the same thing. the idea here is to keep a flag that says if a character has already been inserted or not. When we are checking both strings, since one is bigger than the other, we must have different indexes to keep track of. In the case where a different character is found. The differentChar flag is set and the index of the bigger string is incremented.
"""


def replacedOnce(firstString: str, secondString: str) -> bool:
    differentChar = False
    for i in range(len(firstString)):
        # if found different characters
        if firstString[i] != secondString[i]:
            # set the differentChar flag if not already set
            if differentChar:
                return False
            differentChar = True
    return True


def insertedOnce(firstString: str, secondString: str) -> bool:
    # grab the biggest string
    if len(firstString) > len(secondString):
        biggerString = firstString
        smallerString = secondString
    else:
        biggerString = secondString
        smallerString = firstString

    indexSmaller, indexBigger = 0, 0
    insertionFound = False

    # while both indexes are inbounds of their respective strings
    while indexSmaller < len(smallerString) and indexBigger < len(biggerString):
        # if found a diff char
        if smallerString[indexSmaller] != biggerString[indexBigger]:
            if insertionFound:
                return False
            insertionFound = True
            # check the next char and see if it's really the same
            indexBigger += 1

        else:
            # if the chars are the same, we increment both indexes
            indexSmaller += 1
            indexBigger += 1

    return True


def oneAway(firstString: str, secondString: str) -> bool:
    if len(firstString) == len(secondString):
        # Case where len() are equal must mean replace
        return replacedOnce(firstString, secondString)
    elif abs(len(firstString) - len(secondString)) == 1:
        # The length of the string can be different by at most 1 character. In this case, it will be an insertion case
        return insertedOnce(firstString, secondString)
    else:
        return False


def main():
    testCases: list[str] = [
        ("pale", "ple"),
        ("pales", "pale"),
        ("pale", "bale"),
        ("pale", "bake"),
        ("aab", "bba"),
    ]
    for test in testCases:
        print(oneAway(*test))


if __name__ == "__main__":
    main()
