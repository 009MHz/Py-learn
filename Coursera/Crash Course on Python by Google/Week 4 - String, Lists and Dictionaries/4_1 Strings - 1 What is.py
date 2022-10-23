"""String is..."""
"""
1. String is data type in python that's used to represent a piece of text
2. It's written either in single quotes or double quotes as long as they match
3. Unmatched quotes will resulted an error
    SyntaxError: unterminated string literal
4. Concatenation is a method to combine strings using the '+' sign
5. String can be multiplied (less common operation) using '*' sign
6. len() can be used to count the number of the characters contained in the string
7. The text contents under .txt files is also string
"""

# 'example 1:
'''Modify the double_word function so that it returns the same word repeated twice, followed by the length of
the new doubled word. For example, double_word("hello") should return hellohello10.'''
def double_word(word):
    new = word*2
    return new + str(len(new))


print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0