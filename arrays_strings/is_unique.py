# Implement an algorithm to determine if a string has all unique characters.


def is_unique(string) -> bool:
    seen = set()
    for s in string:
        if s in seen:
            return False
        seen.add(s)
    return True


def is_unique_chars(string) -> bool:
    # constraints: all lowercase letters, ascii, no data structures
    def get_binary_representation(char):
        return 1 << char

    checker = 0
    for s in string:
        val = ord(s) - ord("a")
        if (checker & get_binary_representation(val)) > 0:
            return False
        checker |= get_binary_representation(val)
    return True
