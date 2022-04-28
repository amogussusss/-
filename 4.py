if __name__ == "__main__":
    row = int(input( ))
    columns = int(input( ))
    array = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        assert len(row) == columns
        array.append(row)
    summ = 0
    for j in array:
        summ += sum(j)
        for a in j:
            if a < 0:
                summ -= sum(j)
                break
    print(summ)
 
    m = 0
    for i in range(rows):
        m += array[i][i]
    for i in range(rows):
        g1=0
        g2=0
        if g1<m:
            m=g1
        if g2<m:
            m=g2
    print(m)
