#Dinārs Kemzāns 17. grupa 221RDB321

import heapq
def parallel_processing(n, m, data):
    output = []
    maxval =[(0,i) for i in range(n)]
    for x in data:
        beigsana, numurs = heapq.heappop(maxval)
        output.append((numurs, beigsana))

        beigsana += x
        heapq.heappush(maxval, (beigsana, numurs))


    return output

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
