def is_product_odd_in(s):
    n = len(s)
    count = 0
    for i in range(1,n):
        for j in range(0,i):
            if s[j]*s[i]%2!=0:
                count +=1
                break

    if count > 0:
        return True
    else:
        return False

#----Driver Function----

s = list(map(int,input().split()))
print(is_product_odd_in(s))


"""
Explaination:
Basic maths 
odd*even = even
odd*odd = odd
function is_product_odd_in checks for the pair in the sequence
if found atleast one prints True or else prints false

"""