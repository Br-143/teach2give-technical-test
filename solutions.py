# Technical Test Solutions

def is_palindrome(text):
    """
    Question 2: Function to check if a word or phrase is palindrome.
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    
    Args:
        text (str): The input string to check
    Returns:
        bool: True if the text is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for phrase comparison
    cleaned_text = ''.join(text.lower().split())
    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]

def is_pangram(string):
    """
    Question 3: Function to check if a string is a pangram.
    A pangram is a sentence containing every letter of the alphabet at least once.
    
    Args:
        string (str): The input string to check
    Returns:
        bool: True if the string is a pangram, False otherwise
    """
    # Convert to lowercase and remove spaces
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Return True if all letters in alphabet are in the string
    return set(string.lower()) >= alphabet

def reverse_integer(num):
    """
    Question 4: Function to reverse the digits of an integer.
    
    Args:
        num (int): The input integer
    Returns:
        int: The integer with reversed digits
    """
    # Convert to string, keeping the sign
    sign = -1 if num < 0 else 1
    # Reverse the absolute value and convert back to integer
    reversed_num = int(str(abs(num))[::-1])
    return sign * reversed_num

def capitalize_words(string):
    """
    Question 5: Function to capitalize the first letter of each word in a string.
    
    Args:
        string (str): The input string
    Returns:
        str: The string with each word capitalized
    """
    # Split the string into words and capitalize each word
    return ' '.join(word.capitalize() for word in string.split())

# Test cases
def run_tests():
    # Test palindrome function
    print("\nPalindrome Tests:")
    test_cases = ["madam", "nurses run", "hello", "racecar"]
    for test in test_cases:
        print(f"'{test}' is palindrome: {is_palindrome(test)}")

    # Test pangram function
    print("\nPangram Tests:")
    test_cases = ["The quick brown fox jumps over the lazy dog", "Hello world"]
    for test in test_cases:
        print(f"'{test}' is pangram: {is_pangram(test)}")

    # Test reverse integer function
    print("\nReverse Integer Tests:")
    test_cases = [500, -56, -90, 91]
    for test in test_cases:
        print(f"Reverse of {test} is: {reverse_integer(test)}")

    # Test capitalize words function
    print("\nCapitalize Words Tests:")
    test_cases = ["hi", "i love programming"]
    for test in test_cases:
        print(f"'{test}' capitalized: {capitalize_words(test)}")

if __name__ == "__main__":
    run_tests()
