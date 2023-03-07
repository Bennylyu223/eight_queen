n = eval(input("what is n? "))

result = []
result.extend(n*[-10])
sums = 0


def eight_queen(row):
    if row == n:
        global sums
        sums += 1
        print(result)
    else:
        for col in range(n):
            if no_conflict(row, col):
                result[row] = col
                eight_queen(row+1)
            if row < n-1:
                result[row+1] = -10


def no_conflict(row, col):
    if col in result:
        return False
    for i in range(row):
        if i+result[i] == col+row or i-result[i] == row-col:
            return False
    return True


eight_queen(0)
print(sums)
