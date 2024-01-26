"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string.

BCR: O(N)
"""


def URLify(string: str, length: int) -> str:
    # O(n) operation - time complexity
    string = string.strip()  # O(n) memory
    string = string.replace(" ", "%20")
    return string


def URLifyWithoutLibrary(string: str, length: int) -> str:
    # Idea here is to create a list of every character up to a certain length. This avoid creating string concatenations every loop. Since strings are immutable. it is bad practice to create another string every loop.
    ans = list(string[:length])

    # O(n) time.
    for i in range(length):
        if ans[i] == " ":
            ans[i] = "%20"
    return "".join(ans)


def main():
    testCase = ("Mr John Smith   ", 13)
    print(URLifyWithoutLibrary(*testCase))


if __name__ == "__main__":
    main()
