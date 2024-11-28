def contains_special_characters(data):
    special_characters = set('@&+/:;=?\"<>#%{}|\\^~[]`()')
    return len(set(data) & special_characters)> 0 #return True if the intersection of sets its not empty


def is_hex_char(char):
    return char in '0123456789ABCDEFabcdef'