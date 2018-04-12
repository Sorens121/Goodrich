def is_multiple(n,m):
	if n %m == 0:
		return True
	else:
		return False

#----Driver Function----

n,m = map(int,input().split())
print(is_multiple(n,m))