num=int(input("Enter a number: "))
half=int(num/2)

for i in range(half):
    for j in range(0,half-i):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end=" ")
    for j in range(0,2*(half-i)):
        print("  ",end="")
    for j in range(0,i+1):
        print("* ",end=" ")
    print("\n")
for i in range(num,0,-1):
    for j in range(0,num-i):
        print("  ",end="")
    for j in range(0,i):
        print("*   ",end="")
    print("\n")
    