# Given two strings, write a method to decide if one is a permutation of the other.

def is_equal_length(str1, str2) -> bool:
    return len(str1) != len(str2)

def check_permutation_sorted(str1, str2) -> bool:
    # O(nlogn) time, O(n) space
    if is_equal_length(str1, str2):
        return False
    return sorted(str1) == sorted(str2)

def check_permutation(str1, str2) -> bool:
    # O(n) time, O(n) space
    if is_equal_length(str1, str2):
        return False
    hash_map = {}
    for s in str1:
        hash_map[s] = hash_map.get(s, 0) + 1
    for s in str2:
        hash_map[s] = hash_map.get(s, 0) - 1
        if hash_map[s] < 0:
            return False
    return True
