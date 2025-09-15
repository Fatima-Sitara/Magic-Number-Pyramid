# Number Pattern Printing 

# Ask user for number of rows
rows = int(input("Please enter number of rows: "))

#outer loop
for i in range(1, rows + 1):
    # Inner loop 
    for j in range(1, i + 1):
        print(j, end=" ")  
    print() 
