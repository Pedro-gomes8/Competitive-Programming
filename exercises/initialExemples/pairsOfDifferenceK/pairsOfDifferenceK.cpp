#include <unordered_set>
#include <vector>
#include <string>
#include <iostream>

int pairsOfDifferenceK(const std::vector<int> &arr, int k, const std::string &solution = "best");

int pairsOfDifferenceK(const std::vector<int> &arr, int k, const std::string &method)
{
    int sum = 0;
    // BruteForce Method
    if (method == "brute force")
    {
        for (int i = 0; i < arr.size(); i++)
        {
            for (int j = i + 1; j < arr.size(); j++)
            {
                if (std::abs(arr[i] - arr[j]) == k)
                    sum++;
            }
        }
    }
    else if (method == "best")
    {
        std::unordered_set<int> hashtable(arr.begin(), arr.end());
        for (int elem : hashtable)
        {
            if (hashtable.find(elem - 2) != hashtable.end())
                sum++;
        }
    }
    return sum;
}

int main()
{
    std::vector<int> arr = {1, 7, 5, 9, 2, 12, 3};
    std::cout << (pairsOfDifferenceK(arr, 2, "brute force")) << "\n";
    std::cout << (pairsOfDifferenceK(arr, 2)) << "\n";
}