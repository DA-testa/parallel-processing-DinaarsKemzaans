#Dinārs Kemzāns 17. grupa 221RDB321

def parallel_processing(n, m, data):
    resultats = []
    laiks = 0
    uzdevumi = list(range(n))
    job = {}
    indeks = 0

    while indeks < int(len(data)):
        for tekosais, beigas in job.items():
            if beigas == laiks:
                uzdevumi.append(tekosais)
        
        while uzdevumi and indeks < m:
            tekosais = uzdevumi.pop(0)
            resultats.append([tekosais, laiks])
            job[tekosais] = laiks + data[indeks]
            indeks += 1

        laiks += 1

    return resultats

def main():
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    data = list(map(int, input().split()))
    assert len(data) == m
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for x in range(len(result)):
        print(str(result[x][0]) + " " + str(result[x][1]))

if __name__ == "__main__":
    main()
