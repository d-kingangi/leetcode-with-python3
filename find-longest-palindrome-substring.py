# Find the Longest Palindromic Substring

# is_palindrome function compares a given string to its reverse
# empty list palindromic_substring tracks the longest substring 
# nested loops iterate through possible substrings of input string s
# for each substring, the is_palindrome function checks if it is a palindrome
# if a palindrome longer than the previous palindromic string is found, the palindromic_substring is updated with the new palindrome 
# returns the palindromic_substring, the longest palindromic substring found in the input

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]
        palindromic_substring=[]
        for i in range ( len(s)):
            for j in range (i, len(s)):
                sub_string = s[i:j+1]
                if is_palindrome(sub_string):
                    if len(palindromic_substring)>len(sub_string):
                        continue
                    else:
                        palindromic_substring = sub_string
        return palindromic_substring
