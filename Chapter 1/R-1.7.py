t = int(input())
x = sum([i*i for i in filter(lambda x:x%2!=0,range(1,t))])
print(x)