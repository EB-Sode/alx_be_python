#Ask user for size of pattern
length = int(input("Enter the size of the pattern:"))
count = 1

#loop over the range of the length column
while count <= length:
    count += 1
    #loop over the range of the length row
    for j in range (length):
    #print the star
        print("*", end="")
    #Move to the next line
    print("")