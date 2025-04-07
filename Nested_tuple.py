t1=int(input("enter the limit for the first tuple :"))
t2 = int(input("enter the limit for the second tuple :"))
a=()
e=()
c=()
for i in range(0,t1):
    x = input("enter the element ")
    a = a+(x, )
print("The first tuple :",a)
for j in range(0,t2):
    b = input("enter the element")
    e = e+(b, )
print("The second tuple :",e)
c= a + e
print(c)
    
  
