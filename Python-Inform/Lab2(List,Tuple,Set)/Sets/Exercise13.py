# l=list(map(int,input().split()))


# def Palindrome():
#     l1=[]
#     l2=[]
#     for i in range(0,int(len(l)//2)):
#         l1.append(l[i])
#     for i in range(int(len(l)//2)+1,len(l)):
#         l2.append(l[i])
#     l2.reverse()
#     if l1==l2:
#         return True
#     return False

# if Palindrome():
#     print("YES")
# else:
#     print("NO")
    
def n(a):
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    cnt = 0
    for i in d.values():
        if i % 2 == 1:
            cnt += 1
        if cnt > 1:
            return False
    return True


a = [int(i) for i in input().split()]

if n(a) == True:
    print("Yes")
else:
    print("No")