# Given a string, write a function to check if it is a permutation of a palindrome.

def is_palindrome_permutation(string) -> bool:
    # time complexity: O(n), space complexity: O(n)
    hashmap = {}
    odd_count = 0

    for s in string:
        if s.isalpha():
            s = s.lower()
            hashmap[s] = hashmap.get(s, 0) + 1
    
    for count in hashmap.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True

