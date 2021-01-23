def decodeString(s):

    currStr, currNum, stack = "", 0, []

    for char in s:
        if char is "[":
            stack.append(currStr)
            stack.append(currNum)
            currStr = ""
            currNum = 0
        elif char is "]":
            num = stack.pop()
            prevStr = stack.pop()
            currStr = prevStr + currStr*num
        elif char.isdigit():
            currNum = currNum*10 + int(char)
        else:
            currStr += char
    
    return currStr