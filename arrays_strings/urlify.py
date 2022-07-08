# Replace all spaces in a string with '%20'

def urlify(string, size) -> str:
    s = list(string)
    for i in range(size):
        if s[i].isspace():
            s[i] = '%20'
    return ''.join(s[:size])
