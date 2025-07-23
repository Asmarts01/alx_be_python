# pattern drawing in form of squares
size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end=" ")
        col += 1
    print()  # Move to the next line after finishing a row
    row += 1