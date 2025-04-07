a=int(input("enter the number of element :"))
t=()
e=()
o=()
for i in range(0,a):
    x = int(input("enter the number :"))
    t = t+(x,)
for i in t:
    if i % 2 == 0:
        e = e+(i,)
    else:
        o = o+(i,)
print(e)
print(o)
            
