def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        charToSkip = s[left]
        while left <= right and s[left] == charToSkip:
            left += 1
        while right >= left and s[right] == charToSkip:
            right -= 1

    return right - left + 1


if __name__ == "__main__":
    testCases = ["ca", "cabaabac", "aabccabba"]
    for test in testCases:
        print(minimumLength(test))
