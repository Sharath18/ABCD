size = int(input("Enter the size:- "))
a = [0]*size;
for i in range(0,size):
    a[i] = int(input("Enter the elements"))
    
a.reverse()
for i in range(0,size):
    print(a[i])