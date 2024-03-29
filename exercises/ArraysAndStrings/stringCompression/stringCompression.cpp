#include "stringCompression.h"
#include <iostream>

StringCompressor::StringCompressor(std::string &str) : str(str)
{
    char prevChar = str[0];
    int lengthCounter = 1;
    int prevCharCounter = 1;
    for (char character : str)
    {
        if (character != prevChar)
        {
            lengthCounter++; // For new char
            lengthCounter += std::to_string(prevCharCounter).size();
            prevChar = character;
            prevCharCounter = 1;
        }
        else
            prevCharCounter++;
    }
    lengthCounter++; // For last character
    lengthCounter += std::to_string(prevCharCounter).size();

    // New string is gonna have the different characters and the frequency associated
    this->worthIt = (lengthCounter < str.size());
}

std::string StringCompressor::compress()
{
    if (!this->worthIt)
        return this->str;

    char prevChar = this->str[0];
    int indexToInsert = -1;
    int charFrequency = 0;
    for (char character : str)
    {
        if (character != prevChar)
        {
            this->str[++indexToInsert] = prevChar;
            for (char number : std::to_string(charFrequency))
            {
                this->str[++indexToInsert] = number;
            }
            prevChar = character;
            charFrequency = 1;
        }
        else
        {
            charFrequency++;
        }
    }
    this->str[++indexToInsert] = prevChar;
    for (char number : std::to_string(charFrequency))
    {
        this->str[++indexToInsert] = number;
    }
    this->str.resize(++indexToInsert);
    return this->str;
}

int main()
{
    std::string str = "aaaabbbccceee";
    StringCompressor compressor(str);
    std::cout << compressor.compress() << '\n';
}