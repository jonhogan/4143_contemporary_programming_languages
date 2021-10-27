'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         10/27/21                                                   
 
Program for Question 3:

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed
integer (similar to C/C++'s atoi function). (40 points)

The algorithm for myAtoi(string s) is as follows:
    a) Read in and ignore any leading whitespace.

    b) Check if the next character (if not already at the end of the string) is '-'
       or '+'. Read this character in if it is either. This determines if the final
       result is negative or positive respectively. Assume the result is positive if
       neither is present.

    c) Read in next the characters until the next non-digit character or the end
       of the input is reached. The rest of the string is ignored.

    d) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If
       no digits were read, then the integer is 0. Change the sign as necessary
       (from step 2).

    e) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then
       clamp the integer so that it remains in the range. Specifically, integers less
       than -231 should be clamped to -231, and integers greater than 231 - 1 should
       be clamped to 231 - 1.

    f) Return the integer as the final result.

Note:
 Only the space character ' ' is considered a whitespace character.

 Do not ignore any characters other than the leading whitespace or the rest of the
 string after the digits.
'''

def myAtoi(s):
    isNeg = False
    s = s.strip()

    if s[0] == '-':
        isNeg = True

    for idx in range(len(s)):
        if (s[idx].isnumeric() == True):
            number += s[idx]
