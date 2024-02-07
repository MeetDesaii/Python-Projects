"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome_check_using_string(num):
    string = num.__str__()
    reversed_string = string[::-1]
    # Another way to reverse a string using while loop
    # iterate = len(string)
    # reversed_string = ""
    # while iterate > 0:
    #     reversed_string += string[iterate - 1]
    #     iterate -= 1
    # print(reversed_string)

    if string == reversed_string:
        return True
    else:
        return False


def is_palindrome_check_using_int(num):
    # Edge cases: negative numbers and multiples of 10 (except 0) are not palindromes
    if num < 0 or (num != 0 and num % 10 == 0):
        return False

    reversed_half_int = 0

    while num > reversed_half_int:
        reversed_half_int = reversed_half_int * 10 + num % 10
        num //= 10

    # The number is a palindrome if it's the same as the reversed half
    # or the same when the middle digit is removed (for odd-length numbers)
    return num == reversed_half_int or num == reversed_half_int // 10


print(is_palindrome_check_using_int(121))
print(is_palindrome_check_using_int(-121))
print(is_palindrome_check_using_int(10))


"""
Explanation:

The while loop continues as long as x is greater than reversed_half. This condition ensures that the loop runs only until half of the number is processed, which is crucial for comparing the two halves of the number.

Inside the loop:

x % 10 extracts the last digit of x.
reversed_half * 10 shifts the digits in reversed_half to the left by one position (equivalent to appending a new digit at the rightmost position in decimal representation).
reversed_half * 10 + x % 10 adds the extracted digit to reversed_half, effectively appending it to the reversed number.
x //= 10 removes the last digit from x by performing integer division by 10.

After the loop, x contains the first half of the number (or the entire number minus the middle digit if the original number had an odd number of digits), and reversed_half contains the reversed second half.

x == reversed_half: This checks if the first half of the number is equal to the reversed second half. This condition would be true for numbers with an even number of digits.

x == reversed_half // 10: This condition accounts for numbers with an odd number of digits. Since reversed_half contains one extra digit in this case (the middle digit), dividing it by 10 removes that extra digit. This comparison checks if the first half of the number (excluding the middle digit) is equal to the reversed second half (also excluding the middle digit).
"""


