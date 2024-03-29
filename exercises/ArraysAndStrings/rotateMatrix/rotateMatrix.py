"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

 
1 2 3 4                 13 9 5 1               13 9 5 1
5 6 7 8                 14 10 6 2                     2
9 10 11 12              15 11 7 3                     3
13 14 15 16             16 12 8 4                     5
"""
import copy


def rotateMatrix(matrix: list[list[int]]) -> list[list[int]]:
    maxIndex = len(matrix) - 1
    leftPtr, rightPtr = (0, maxIndex)
    while leftPtr < rightPtr:
        for i in range(rightPtr - leftPtr):
            top, bottom = leftPtr, rightPtr

            # save the top left element
            topLeft = matrix[top][leftPtr + i]

            # move bottom left to top left
            matrix[top][leftPtr + i] = matrix[bottom - i][leftPtr]

            # move bottom right to bottom left
            matrix[bottom - i][leftPtr] = matrix[bottom][rightPtr - i]

            # move top right to bottom right
            matrix[bottom][rightPtr - i] = matrix[top + i][rightPtr]

            # Place the temporary variable into top right
            matrix[top + i][rightPtr] = topLeft

        leftPtr += 1
        rightPtr -= 1

    for row in range(len(matrix)):
        print(matrix[row])


"""
1 2 3     7 4 1
4 5 6     8 5 2
7 8 9     9 6 3
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateMatrix(matrix)
