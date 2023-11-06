# check if a string input by a user is a palindrome or not
# print out whether this string is a palindrome or not. 
# use for loops


def is_palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
  
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('Enter word:\n')
x = reverse(word)
if x == word:
	print('This is a palindrome')
else:
	print('This is not a palindrome')

