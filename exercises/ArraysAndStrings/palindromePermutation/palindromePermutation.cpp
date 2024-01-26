/*
Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

    Parma1 : the string to be checked.

    Returns: true if it's a permutation of a palindrome
             false otherwise

    BCR: O(n)
*/
#include <string>
#include <iostream>
#include <unordered_map>

bool palindromePermutation(std::string &str)
{
    std::unordered_map<char, int> charFrequency;

    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] == ' ')
            continue;
        str[i] = std::tolower(str[i]);

        charFrequency[str[i]]++;
    }

    int oddCounter = 0;
    for (const auto &[maybeUnused, value] : charFrequency)
    {
        if (value % 2 != 0)
        {
            oddCounter++;
            if (oddCounter > 1)
                return false;
        }
    }
    return true;
}

int main()
{
    std::string testCase = "Tact coo";
    std::cout << palindromePermutation(testCase) << '\n';
}