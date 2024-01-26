from collections import Counter


def palindromePermutation(string: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    Parma1 : the string to be checked.

    Returns: true if it's a permutation of a palindrome
             false otherwise

    BCR: O(n)
    """

    string = string.lower()

    charCounter = {}

    for char in string:
        if char != " ":
            charCounter[char] = charCounter.setdefault(char, 0) + 1

    return sum(count % 2 for count in charCounter.values()) <= 1


def usingCounter(string: str) -> bool:
    string = string.lower().replace(" ", "")

    charCounter = Counter(string)

    return sum(count % 2 for count in charCounter.values()) <= 1


def main():
    testCase = "Tact coo"
    print(palindromePermutation(testCase))


main()
