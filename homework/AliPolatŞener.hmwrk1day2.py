#homework1

nums=list(range(10))
print(nums)
print(len(nums))
i=int(len(nums)/2)
print(int(i))
list1=list(range(0,i))
list2=list(range(i,2*i))
print(list2+list1)

#homework1
i = int(input("Please enter a single digit integer: "))
if i>=10:
    print("invalid number")
elif i<0:
    print("invalid number")
else:
    i1=i
    i1%=2
    if i1==0:
        a=0
        while a<=i:
            print(a)
            a+=2
    else:
        a=0
        while a<i:
            print(a)
            a+=2
        print(i)
