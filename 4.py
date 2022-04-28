if __name__ == "__main__":
    row = int(input( ))
    columns = int(input( ))
    array = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        assert len(row) == columns
        array.append(row)
    summ = 0
    for i in array:
        summ += sum(i)
        for a in i:
            if a < 0:
                summ -= sum(i)
                break
    print(summ)
 
    m = 0
    for i in range(rows):
        m += array[i][i]
    for i in range(rows):
        d1=0
        d2=0
        if d1<m:
            m=d1
        if d2<m:
            m=d2
    print(m)
