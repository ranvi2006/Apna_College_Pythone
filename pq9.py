# check if a list contains a palindrom or not
list1=[1,2,3,4,2,1]
copy=list1.copy()
copy.reverse()
if(list1==copy):
    print("Yes , list is a palindrom")
else:
    print("No, it is not a palindrom")

# -------------------------------------

list1=[1,"abc","abc",1]
copy=list1.copy()
copy.reverse()
if(list1==copy):
    print("Yes , list is a palindrom")
else:
    print("No, it is not a palindrom")