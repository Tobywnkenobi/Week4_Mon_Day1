"""
# Introduction:

# Winter is almost here, and you're gearing up for an exciting ski vacation. As a coding enthusiast, you love a good challenge. Here's a fun one for you: let's calculate the number of pairs of gloves you can create from your collection.

# Problem Description:

# You're given an array that describes the color of each glove in your collection. Your task is to write a function that calculates how many pairs of gloves you can form. Remember, a pair consists of two gloves of the same color.

# Function Signature:


# def count_glove_pairs(glove_colors):
#     # Your code here


# Input:

# - `glove_colors` (List of Strings): An array of glove colors. The length of the array (n) will be between 1 and 1000.

# Output:

# - An integer representing the number of pairs you can create from the given gloves.

# Examples:

# Example 1:

# glove_colors = ["red", "green", "red", "blue", "blue"]
# count_glove_pairs(glove_colors)
# Output: 2
# Explanation:You can form 1 pair of red gloves and 1 pair of blue gloves. 2 pairs of gloves.


# Example 2:

# glove_colors = ["red", "red", "red", "red", "red", "red"]
# count_glove_pairs(glove_colors)
# Output: 3
#Explanation: You can form 3 pairs of red gloves.

# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function


input is a string, output is an integer
"""
from collections import defaultdict

def count_gloves(glove_color: list[str]) -> int:
    color_count = defaultdict(int)

    for color in glove_color:
        color_count[color] += 1

    pairs = sum(count // 2 for count in color_count.values())
   
    return pairs


example1 = ['red','green','red','blue','blue']
example2 = ['red','red','red','red','red','red']

print(count_gloves(example1))
print(count_gloves(example2))
