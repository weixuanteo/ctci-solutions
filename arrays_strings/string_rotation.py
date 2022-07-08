# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of "erbottlewat").


def is_substring(s1, s2):
    return s2 in s1


def is_string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # yx always is a substring of xyxy
    return is_substring(s1 + s1, s2)
