# Given two strings, write a function to check if they are one edit (or zero edits) away.
# Three types of edits: insert, remove, replace a character.


def get_shortest_length(str1, str2) -> int:
    if len(str1) < len(str2):
        return len(str1)
    return len(str2)


def check_replace(str1, str2) -> bool:
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count <= 1


def check_insert(str1, str2) -> bool:
    index1 = 0
    index2 = 0
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def is_one_away(str1, str2) -> bool:
    # time complexity: O(n), space complexity: O(n)
    if len(str1) == len(str2):
        return check_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return check_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return check_insert(str2, str1)
    else:
        return False
