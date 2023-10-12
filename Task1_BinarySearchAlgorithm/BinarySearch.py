"""As the binary term explains, the system will take any
input starting from 0 to any range that you specify and
display a range of numbers with a difference of two"""

number = int(input("Enter number:"))
for i in range(0, number+1, 2):
    print(i, end=" ")