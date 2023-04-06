# PROBLEM 4
# PRE CONDITION: It is assumed that an uppercase character is different from the same lowercase character
# For example 'a' is different from 'A'

def minimunChangesToMakePasswordStrong(s):
    # Behaviour for deletion does not always work with the rest of the implementation
    # so we will remove repeating characters until we get to a length of at most 20 characters
    if len(s) > 20:
        for i in range(2, len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                # Count each removed character and recursively call the same method without it
                return 1 + minimunChangesToMakePasswordStrong(s[:i] + s[i+1:])

    # Variable which is used for checking if an uppercase letter is present withing the password
    containsLowercase = False
    
    # Variable which is used for checking if a lowercase letter is present withing the password
    containsUppercase = False
    
    # Variable which is used for checking if a digit is present withing the password
    containsDigit = False
    
    # Variable to count minimum number of changes
    # Initialized with 3 with the presumption that the password doesn't contain any uppercase or lowercase letters
    # and no digits
    thingsToChange = 3
    
    # Counter for consecutive repeating characters
    consecutiveEqualCharacters = 1
    
    # Number of characters we have to replace in order to not have 3 consecutive repeating characters anywhere
    # within the password
    breakRepeatingCharacters = 0
    
    # String index
    i = 0
    
    # Iterate over the string, character by character
    while i < len(s):
        # If an uppercase letter is found the containsUppercase variable becomes true
        if containsUppercase == False and s[i].isupper():
            containsUppercase = True
            thingsToChange -= 1
        # If a lowercase letter is found the containsLowercase variable becomes true
        if containsLowercase == False and s[i].islower():
            containsLowercase = True
            thingsToChange -= 1
        # If a digit is found the containsDigit variable becomes true
        if containsDigit == False and s[i].isdigit():
            containsDigit = True
            thingsToChange -= 1
        # If the password has more than 1 character
        if i > 0:
            # If two adjacent characters are the same, increase repeating characters count
            if s[i] == s[i - 1]:
                consecutiveEqualCharacters += 1
            # If the streak of repeating characters has ended
            else:
                # If the streak contained at least 3 repeating characters
                if consecutiveEqualCharacters >= 3:
                    # Increase count of characters that need to be replaced
                    breakRepeatingCharacters += consecutiveEqualCharacters // 3
                # Reset repeating character count; set it to one because we compare character at index i to
                # character at index i-1, so the first repeating character should already be counted
                consecutiveEqualCharacters = 1
        # Increase index to go to next character in password
        i += 1

    # Check for repeating characters at last index in case it also matches the second to last character.
    # This case is missed by the for loop because of the 'else' on line 57
    i -= 1
    if i > 0:
        if s[i] == s[i - 1]:
            if consecutiveEqualCharacters >= 3:
                breakRepeatingCharacters += consecutiveEqualCharacters // 3

    # If there are more characters that need to be replaced in order to not have 3 repeating characters than
    # characters that do not respect the requirements of the password (one uppercase/lowercase letter, one digit)
    # then we can consider that we can simply replace characters to satisfy both conditions at once:
    # REPLACE CHARACTERS THAT ARE REPEATING WITH CHARACTERS NEEDED TO SATISFY PASSWORD REQUIREMENTS
    # EXAMPLE --------------
    # For string "aaaaaaaaa" we need to replace characters at indexes 2, 5 and 8 because they are repeating for the
    # third time. We also need to have ONE UPPERCASE LETTER AND ONE DIGIT. As such, we replace character at index 2
    # with 'Z' and character at index 5 with '3' and character at index 8 with any character other than 'a',
    # for example 'b'.
    # AS SUCH, THE PASSWORD SATISFIES ALL REQUIREMENTS WITH MINIMUM NUMBER OF CHANGES
    # INITIAL STRING: "aaaaaaaaa"
    # RESULTING STRING: "aaZaa3aab"
    # CHANGES REQUIRED: 3 - replace 'a' with 'Z' at index 2, replace 'a' with '3' at index 5, replace 'a' with 'b'
    # at index 8
    if breakRepeatingCharacters > thingsToChange:
        thingsToChange = breakRepeatingCharacters
    # The principle used above of satisfying all requirements with minimum number of changes also applies to characters
    # that need to be added or removed to achieve a length of at least 6
    # EXAMPLE --------------
    # For string "aaa" we need to add 3 characters to get to a length of 6 and also have an UPPERCASE LETTER and
    # A DIGIT. For this, we can add an uppercase letter and a digit at the end, and ADD any character other than 'a'
    # to break the repeating 3, for example 'b'
    # INITIAL STRING: "aaa"
    # RESULTING STRING: "aabaZ3"
    # CHANGES REQUIRED: 3 - insert 'b' at index 2, add 'Z' and '3' at the end of the string
    if len(s) < 6:
        return thingsToChange if thingsToChange > 6 - len(s) else 6 - len(s)
    return thingsToChange

if __name__ == '__main__':
    print(minimunChangesToMakePasswordStrong("aaaaaaaaa"))  # This example prints 3, example explained above
    print(minimunChangesToMakePasswordStrong("aaa"))  # This example prints 3, example explained above

    # This example prints 8 - there are 22 characters - every third 'a' is replaced with any character (including one
    # uppercase letter and one digit); the last two characters are removed
    print(minimunChangesToMakePasswordStrong("aaaaaaaaaaaaaaaaaaaaaa"))

    # This example prints 2 - there are 22 characters and the ones removed will be at indexes 3 and 17
    # (both characters are 'a') resulting in a strong password
    print(minimunChangesToMakePasswordStrong("A3aaabcdefghijklaaamno"))
