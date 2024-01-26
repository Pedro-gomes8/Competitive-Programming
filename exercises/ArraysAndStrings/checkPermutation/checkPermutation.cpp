#include <string>
#include <unordered_map>
/*
Given two strings, write a method to decide if one is permutation of another
*/

bool checkPermutation(std::string firstString, std::string secondString)
{
    if (firstString.size() != secondString.size())
        return false;

    std::unordered_map<char, int> mp;

    for (char character : firstString)
    {
        mp[character]++;
    }

    for (char character : secondString)
    {
        if (mp.find(character) != mp.end())
        {
            mp[character]--;
            if (mp[character] < 0)
                return false;
        }
        else
            return false;
    }
    return true;
}