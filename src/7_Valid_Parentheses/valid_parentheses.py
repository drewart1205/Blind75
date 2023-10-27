def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []

    for c in s:
        if c == "(":
            stack.append(")")
        elif c == "{":
            stack.append("}")
        elif c == "[":
            stack.append("]")
        else:
            if len(stack) > 0:
                if c != stack.pop():
                    return False
            else:
                return False
    if len(stack) != 0:
        return False
    return True