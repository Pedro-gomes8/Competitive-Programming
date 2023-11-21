def permutation(arg: str, prefix: str = ""):
    if len(arg) == 0:
        print(prefix)
    else:
        for index, elem in enumerate(arg):
            rem = arg[:index] + arg[index + 1 :]
            permutation(rem, prefix + elem)


if __name__ == "__main__":
    permutation("fives")
