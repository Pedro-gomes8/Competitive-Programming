from collections import defaultdict


def majorityElement(nums):
    n = len(nums)
    m = defaultdict(int)

    for num in nums:
        m[num] += 1

    n = n // 2
    for key, value in m.items():
        if value > n:
            return key

    return 0
