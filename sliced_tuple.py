a = int(input("Enter the number of elements: "))
t = ()
e =()
for i in range(a):
    x = input("Enter an element: ")
    t = t + (x, )
b = int(input("Enter the last index you want to include: "))
sliced = t[b:]
print(sliced)
