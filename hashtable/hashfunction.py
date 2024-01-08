

capacity_of_list = 20

# 1. key is number
def hash_function(key):
    return key % capacity_of_list


# 2. key is string: convert string to number
def hash_function(key):
    hash = 0
    for char in key:
        hash += ord(char) # ord() returns an integer representing the Unicode character
    return hash % capacity_of_list


