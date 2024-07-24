def add(a,b):
     return a+b
def sub(a,b):
     return a-b
def mul(a,b):
     return a*b
def div(a,b):
     return a/b



print("select an operation:")
print("1. Add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. Exit")

while True:
    choice = input("enter ur choice('1','2','3','4',):")
    if choice =='5':
        print("bye")
        break  
    if choice in('1','2','3','4'):
        n1 =int(input("enter 1st number: "))
        n2 =int(input("enter 2st number: ")) 
        if choice == '1':
            print(add(n1,n2))
        elif choice == '2':
            print(sub(n1,n2))
        elif choice == '3':
            print(mul(n1,n2))
        elif choice == '4':
            print(div(n1,n2))
        else:
            print("invalid choice")
