def decodeString(s):
    # 4 cases, it can be "[", "]", num, char
    currStr, currNum, stack = "", 0, []

    for c in s:
        if c is "[":  # if it is an open bracket, that means it's the start of a new code
            # add whatever was already decoded into the stack
            stack.append(currStr)
            # store the number that was just calculated 23["ab"], you would be storing the 23
            stack.append(currNum)
            currStr = ""  # start the str from new
            currNum = 0  # zero out the num
        elif c is "]": #this means you can start decoding
            num = stack.pop() #retrieve the num
            prevStr = stack.pop() #retrieve the part that has already been decoded
            currStr = prevStr + currStr*num #decode the string by multiplying currStr by num and then add it to the already decoded part
        elif c.isdigit():
            currNum = currNum*10 + int(c) #store the num i.e. 21 will be (2 at first, then 2*10 + 1) == 21
        else:
            currStr += c #add the char to the string

    return currStr
