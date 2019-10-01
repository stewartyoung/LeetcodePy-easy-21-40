string = f'A man, a plan, a canal: Panama'

class ValidPalindrome:
    def isPalindrome(self, string):
        # remove non alphanumeric characters from string
        for char in string:
            if char.isalnum() == False:
                string = string.replace(char, '')
        
        # switch string to all lower case
        string = string.lower()

        # does the string equal the reversed string?
        return string == string[::-1]

test = ValidPalindrome()
print(test.isPalindrome(string))