noOfRows = int(input())
noOfColumns = int(input())
noOfTree = int(input())

if noOfTree <= noOfRows or noOfTree % noOfRows == 1 or noOfTree % (noOfRows - 1) == 1:
    print("true")
else:
    print("false")