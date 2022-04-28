   if __name__ == "__main__":
    c = int(input())
    m = c
    a = []
    for _ in range(nc):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    print(a)

    b = []

    for _ in range(m):
        b.append([0] * c)
    for i in range(c):
        for g in range(m):
            b[j][i] = a[c-(1+i)][g]
    for row in b:
        print(" ".join([str(x) for x in row]))
