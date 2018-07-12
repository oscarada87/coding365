def main():
    symbols = "()+-*/^"
    stack = []
    data = input()
    for ch in data:
        if symbols.find(ch) != -1:
            stack.append(ch)
            check(stack, ch)
        else:
            print(ch,end='')
    for i in range(len(stack)-1,-1,-1):
        print (stack[i],end='')
def check(stack,ch):
    if ch == ')':
        stack.pop()
        for i in range (len(stack)-1,-1,-1):
            if stack[i] == '(':
                stack.pop()
                break
            else:
                print(stack[i],end='')
                stack.pop()
    elif ch == '^':
        try:
            if stack[-2] == '^':
                print(stack[-2],end='')
                stack.pop(-2)
        except IndexError:
            pass
    elif ch == '/' or ch == '*':
        try:
            if stack[-2] == '^' or stack[-2] == '/' or stack[-2] == '*':
                print(stack[-2],end='')
                stack.pop(-2)
        except IndexError:
            pass
    elif ch == '+' or ch == '-':
        try:
            if stack[-2] == '^' or stack[-2] == '*' or stack[-2] == '/' or stack[-2] == '+' or stack[-2] == '-':
                print(stack[-2],end='')
                stack.pop(-2)
        except IndexError:
            pass

main()
