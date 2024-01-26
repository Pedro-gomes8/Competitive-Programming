"""
Given an array of distinct integer values, count the number of pairs of integers that have difference k.
"""


def pairsDifference(arr, k, solution="best"):
    sol = 0
    if solution == "bruteforce":
        # O(n2) time complexity. O(1) memory complexity
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) == k:
                    sol += 1
        return sol
    elif solution == "best":
        # O(n) time complexity O(n) memory
        hashtable = set(arr)
        for element in arr:
            if element - k in hashtable:
                sol += 1
        return sol


if __name__ == "__main__":
    arr = [1, 7, 5, 9, 2, 12, 3]
    print(pairsDifference(arr, 2, solution="best"))
