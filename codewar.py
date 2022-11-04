# It's pretty straightforward.
# Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
# You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1:-1]


# Write a function that accepts an integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.
def repeat_str(repeat, string):
    return repeat * string