"""As the binary term explains, the system will take any
input starting from 0 to any range that you specify and
display a range of numbers with a difference of two"""

start = int(input("Enter Starting Number:"))
end = int(input("Enter Ending Number:"))
for i in range(start, end+1, 2):
    print(i, end=" ")