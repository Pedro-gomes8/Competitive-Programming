/*
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string.

BCR: O(N)
*/

#include <string>
#include <vector>
#include <iostream>

void URLify(std::string &str, int length)
{
    // First step is to count how many spaces there are
    int spaceCount = 0;
    for (int i = 0; i < length; i++)
    {
        if (str[i] == ' ')
        {
            spaceCount++;
        }
    }

    int index = length + 2 * spaceCount;

    str.resize(index);

    for (int i = length - 1; i >= 0; i--)
    {
        if (str[i] == ' ')
        {
            str[--index] = '0';
            str[--index] = '2';
            str[--index] = '%';
        }
        else
        {
            str[--index] = str[i];
        }
    }
}

int main()
{
    std::string test = "Mr John Smith   ";
    int length = 13;
    URLify(test, length);
    std::cout << test << '\n';
}