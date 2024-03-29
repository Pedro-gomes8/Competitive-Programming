"""
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def stringCompression(string: str) -> str:
    listOfChars = []
    prevChar = string[0]
    prevCharCounter = 0

    for char in string:
        if char != prevChar:
            listOfChars.append(prevChar)
            listOfChars.append(str(prevCharCounter))
            prevCharCounter = 1
            prevChar = char
        else:
            prevCharCounter += 1

    listOfChars.append(prevChar)
    listOfChars.append(str(prevCharCounter))

    if len(listOfChars) > len(string):
        return string
    return "".join(listOfChars)


def main():
    testCases = ["aabcccccaaa"]
    for test in testCases:
        print(stringCompression(test))


if __name__ == "__main__":
    main()
