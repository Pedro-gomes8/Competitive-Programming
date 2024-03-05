#include <iostream>
#include <string>

int minimumLength(std::string s)
{
    int l = 0;
    int r = s.size() - 1;

    // Two pointers approach. test if same char in suffix and prefix.
    while ((l < r) && s[l] == s[r])
    {
        char c = s[l];
        while ((l <= r) && s[l] == c)
            l++;

        // remember char on the right is the same as the left
        while ((r >= l) && s[r] == c)
            r--;
    }
    return r - l + 1;
}

int main()
{
    std::vector<std::string> testCases = {"ca", "cabaabac", "aabccabba"};

    for (auto test : testCases)
    {
        std::cout << minimumLength(test) << '\n';
    }
}