"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""


def frequency_sort(s):
    # Count the frequency of each character
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    print(char_freq)

    # Sort the characters by frequency in descending order
    # In case of a tie, it doesn't matter which character comes first, so we ignore the character order
    sorted_chars = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)
    print(sorted_chars)

    # Construct the sorted string
    sorted_string = ''.join(char * freq for char, freq in sorted_chars)

    return sorted_string


# Example usage
print(frequency_sort("tree"))  # Output: "eert" or "Petr"
print(frequency_sort("cccaaa"))  # Output: "cccaaa" or "aaaccc"
print(frequency_sort("Aabb"))  # Output: "bbAa" or "bbaA"
print(frequency_sort("raaeaedere"))

"""
Explanation:

char_freq.items(): This part of the code takes the char_freq dictionary, which contains characters as keys and their frequencies as values, and converts it into a list of tuples. Each tuple consists of a character and its frequency, e.g., [('a', 2), ('b', 3)].

sorted(...): The sorted function is used to sort these tuples. However, we need to sort them based on the frequency of each character (which is the second element of each tuple), not the character itself.

key=lambda item: item[1]: The key parameter specifies a function of one argument that is used to extract a comparison key from each element in the list. Here, lambda item: item[1] is a lambda function that takes an item (a tuple) and returns its second element (the frequency). This tells the sorted function to sort the tuples based on their frequencies.

reverse=True: Normally, the sorted function sorts in ascending order. By setting reverse=True, we sort the items in descending order instead. This means characters with higher frequencies will come first.
"""
