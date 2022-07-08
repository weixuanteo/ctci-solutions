# Implement a method to perform basic string compression using the counts of repeated characters.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).


def is_zero_or_one_char(string) -> bool:
    return len(string) <= 1


def is_compressed_string_bigger(csize, osize) -> bool:
    return csize >= osize


def compress_string(string) -> str:
    og_size = len(string)
    LAST_CHAR_INDEX = -1
    compressed = []
    cmp_size = 0
    count = 1

    def add_to_compressed(char, count, cmp_size) -> int:
        compressed.append(char + str(count))
        return cmp_size + 2

    if is_zero_or_one_char(string):
        return string

    for i in range(1, og_size):
        prev_char = string[i - 1]
        if string[i] == prev_char:
            count += 1
        else:
            cmp_size = add_to_compressed(prev_char, count, cmp_size)
            count = 1

    cmp_size = add_to_compressed(string[LAST_CHAR_INDEX], count, cmp_size)

    if is_compressed_string_bigger(cmp_size, og_size):
        return string
    return "".join(compressed)
