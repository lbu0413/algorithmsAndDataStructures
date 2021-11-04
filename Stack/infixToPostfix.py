def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        "-": 2,
        "(": 1,
    }
    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else:
            if opStack.isEmpty():
                opStack.push(token)
            else:
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
