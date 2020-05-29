
def multi_bracket_validation(string):
    """Takes in a string argument and returns a boolean representing whether or not the brackets within the string are balanced.
    """
    output = False

    if string.count('{') == string.count('}') and string.count('(') == string.count(')') and string.count('[') == string.count(')'):
        output = True

    return output
