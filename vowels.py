def countVowels(s):
    # Define a set of vowels
    vowels = 'aeiouAEIOU'
    # Count the number of vowels in the string
    return sum(1 for char in s if char in vowels)

# Example usage
print(countVowels("hello world"))            # Output: 3
print(countVowels("The quick brown fox"))    # Output: 5
print(countVowels("AEIOU"))                   # Output: 5
print(countVowels("Python Programming"))      # Output: 4