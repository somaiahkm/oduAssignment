testString = "aabbc"
length = len(testString)

table = [[0 for i in range(0,length+1)] for j in range(0,length+1)]

for i in range(1,length+1):
    for j in range(1, length+1):
        if (testString[i-1]==testString[j-1] and (i!=j)):
            table[i][j]=1+table[i-1][j-1]
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])

if(table[length][length]==0):
    print("There is no repeating subsequence")
else:
    print(table[length][length])









