if __name__ == "__main__":
    t = int(input())
    m = int(input())
    a = []
    for _ in range(t):
        row = list(map(int, input().split()))
        assert len(row) == m
        a.append(row)

    count = 0
    f = []

    for i in a:
        if 0 not in i:
            count += 1

    for i in a:
        f_count = 0
        for j in i:
            if j not in f:
                f_count += 1
            if f_count > 1:
                f.append(j)
                f_count = 0

    print(count, max(f))
