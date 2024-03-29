/**
 * @file stringCompression.cpp
 * @author Pedro Gomes (pedro.gomes@centrale.centralelille.fr)
 * @brief Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
 * @version 0.1
 * @date 2024-01-30
 */

#include <string>

class StringCompressor
{
private:
    bool worthIt = false;
    std::string &str;

public:
    StringCompressor(std::string &str);
    std::string compress();
};
