"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

BCR: O(n)
"""


def replacedOnce(firstString: str, secondString: str) -> bool:
    differentChar = False
    for i in range(len(firstString)):
        if firstString[i] != secondString[i]:
            if differentChar:
                return False
            differentChar = True
    return True


def insertedOnce(firstString: str, secondString: str) -> bool:
    if len(firstString) > len(secondString):
        biggerString = firstString
        smallerString = secondString
    else:
        biggerString = secondString
        smallerString = firstString

    indexSmaller, indexBigger = 0, 0
    insertionFound = False
    while indexSmaller < len(smallerString) and indexBigger < len(biggerString):
        if smallerString[indexSmaller] != biggerString[indexBigger]:
            if insertionFound:
                return False
            insertionFound = True
            indexBigger += 1

        else:
            indexSmaller += 1
            indexBigger += 1

    return True


def oneAway(firstString: str, secondString: str) -> bool:
    if len(firstString) == len(secondString):
        return replacedOnce(firstString, secondString)
    elif abs(len(firstString) - len(secondString)) == 1:
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
