s = input()
l = eval(input())
nl = []
for i in l :
    if s == i[:len(s)] :
        nl.append(i)
print(nl)
