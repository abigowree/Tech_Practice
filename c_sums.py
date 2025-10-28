# 1. Reverse a list
# Write a program that takes a list as input and returns a new list with the elements in reverse order. Do not use the built-in reverse() method or slicing [::-1].
# Sample input: ``
# Sample output: `` 
# Reverse a list without using reverse() or slicing
lst = [10, 20, 30, 40, 50]
reversed_list = []
for item in lst:
    reversed_list.insert(0, item)
print("Original list:", lst)
print("Reversed list:", reversed_list)


# 2. Find the largest item
# Create a function find_max(numbers) that accepts a list of numbers and returns the largest number. Do not use the built-in max() function.
# Sample input: ``
# Sample output: 10 
# 3. Count occurrences
# Write a function count_element(input_list, element) that counts how many times a given element appears in input_list.
# Sample input: input_list = [5, 2, 5, 8, 5, 1], element = 5
# Sample output: 3 
# 4. Find common elements
# Write a program that takes two lists and returns a new list containing only the elements that are present in both lists.
# Sample input: list1 = [1, 2, 3, 4, 5], list2 = [4, 5, 6, 7, 8]
# Sample output: `` 
# 5. Remove duplicates
# Write a function remove_duplicates(input_list) that removes all duplicate items from a list, preserving the original order of the first occurrence of each element.
# Sample input: [3,4,5,6,5,1]
# Sample output: [3,4,5,6,1]
# Strings
# 1. Check for a palindrome
# Create a function is_palindrome(input_string) that checks if a string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same forwards and backwards. The function should ignore case and non-alphanumeric characters.
# Sample input 1: 'Racecar'
# Sample output 1: True
# Sample input 2: 'A man, a plan, a canal: Panama'
# Sample output 2: True 
# 2. Count vowels
# Write a program that counts the number of vowels (a, e, i, o, u) in a given string. The counting should be case-insensitive.
# Sample input: 'Hello World'
# Sample output: 3 (for 'e', 'o', 'o') 
# 3. Reverse words in a sentence
# Write a function reverse_words(sentence) that takes a string containing multiple words and returns a new string with the words in reverse order.
# Sample input: 'Python is fun'
# Sample output: 'fun is Python' 
# 4. Count character frequency
# Write a program to count the occurrences of each character in a given string and return the counts in a dictionary. Ignore spaces.
# Sample input: 'hello world'
# Sample output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1} 
# 5. Remove the n-th character
# Write a function remove_char(s, n) that takes a string s and an integer n and returns a new string with the character at index n removed.
# Sample input: s = 'Python', n = 2
# Sample output: 'Pyhon' 
