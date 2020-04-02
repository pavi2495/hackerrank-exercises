class dia:

    def diagonalDifference(self,arr):
        index = 0
        primary_diagonal =0
        secondary_diagonal =0
        arrl =len(arr) -1
        for i in arr:
            primary_diagonal += i[index]
            index += 1
        for i in arr:
            secondary_diagonal += i[arrl]
            arrl -= 1
        result = abs(primary_diagonal -secondary_diagonal)
        return result





pt =dia()
n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split(","))))
result = pt.diagonalDifference(arr)
print(result)


