rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()