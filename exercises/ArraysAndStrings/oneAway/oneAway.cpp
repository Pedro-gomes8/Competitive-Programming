/*
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

BCR: O(n)
*/

#include <string>
#include <cstdlib>
#include <vector>
#include <iostream>

bool replacedOnce(std::string &firstString, std::string &secondString)
{
    bool differenceFound = 0;
    for (int i = 0; i < firstString.size(); i++)
    {
        if (firstString[i] != secondString[i])
        {
            if (differenceFound)
                return false;
            differenceFound = 1;
        }
    }
    return true;
}

bool insertedOnce(std::string &firstString, std::string &secondString)
{
    std::string biggerString, smallerString;
    if (firstString.size() > secondString.size())
    {
        biggerString = firstString;
        smallerString = secondString;
    }
    else
    {
        biggerString = secondString;
        smallerString = firstString;
    }

    int indexSmaller, indexBigger = 0;
    bool insertedFound = false;

    while (indexSmaller < smallerString.size() && indexBigger < biggerString.size())
    {
        if (smallerString[indexSmaller] != biggerString[indexBigger])
        {
            if (insertedFound)
                return false;
            indexBigger++;
            insertedFound = true;
        }
        else
        {
            indexBigger++;
            indexSmaller++;
        }
    }
    return true;
}

bool oneAway(std::string &firstString, std::string &secondString)
{
    if (firstString.size() == secondString.size())
        return replacedOnce(firstString, secondString);
    else if (std::abs(static_cast<int>(firstString.size() - secondString.size())) <= 1)
        return insertedOnce(firstString, secondString);
    else
        return false;
}

int main()
{
    std::vector<std::pair<std::string, std::string>> testCases = {
        {"pale", "ple"},
        {"pales", "pale"},
        {"pale", "bale"},
        {"pale", "bake"},
        {"aab", "bba"},
    };

    for (std::pair<std::string, std::string> test : testCases)
    {
        std::cout << oneAway(test.first, test.second) << '\n';
    }
}