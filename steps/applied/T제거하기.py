S = input()
check = input()

stack=[]
for s in S:
    stack.append(s)
    if stack[-len(check):]==list(check):
        del stack[-len(check):]

answer=''.join(stack)
print(answer)
