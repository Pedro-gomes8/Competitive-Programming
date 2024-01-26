#include <unordered_set>
#include <string>
#include <iostream>

bool uniqueCharacters(std::string str)
{
    std::unordered_set<char> uniqueChars(str.begin(), str.end());
    if (uniqueChars.size() == str.size())
        return true;
    return false;
}

int main()
{
    std::string testCases[] = {"abcdefg", "aabcdfeg", "sddwfv", "hgpknlm"};
    for (std::string test : testCases)
    {
        std::cout << uniqueCharacters(test) << "\n";
    }
}