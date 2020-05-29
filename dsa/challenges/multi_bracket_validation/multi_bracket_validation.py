
def multi_bracket_validation(string):
    """Takes in a string argument and returns a boolean representing whether or not the brackets within the string are balanced.
    """
    output = False
    brackets = []
    test = []

    if string.count('{') == string.count('}') and string.count('(') == string.count(')') and string.count('[') == string.count(']'):

        for char in string:
            if char in ['(', ')', '[', ']', '{', '}']:
                brackets.append(char)

        if brackets[0] in [')', '}', ']']:
            return False

        for i in range(len(brackets)):
            test.append(brackets[i])

    return output
