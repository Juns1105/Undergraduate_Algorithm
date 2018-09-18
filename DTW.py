
import numpy as np
import sys

def DTW(A, B, d=lambda x, y: abs(x - y)):
    # cost matrix initialize
    A, B = np.array(A), np.array(B)
    M, N = len(A), len(B)
    cost = sys.maxsize * np.ones((M, N))

    # fill the first row and column
    cost[0, 0] = d(A[0], B[0])
    for i in range(1, M):
        cost[i, 0] = cost[i - 1, 0] + d(A[i], B[0])

    for j in range(1, N):
        cost[0, j] = cost[0, j - 1] + d(A[0], B[j])

    # fill the remaining index.
    for i in range(1, M):
        for j in range(1, N):
            choices = cost[i - 1, j - 1], cost[i, j - 1], cost[i - 1, j]
            cost[i, j] = min(choices) + d(A[i], B[j])

    # find the optimum path
    n,m=N-1,M-1
    path = []
    
    while (m,n)!=(0,0):
        path.append((m,n))
        m,n=min((m-1,n-1),(m,n-1),(m-1,n),key=lambda x:cost[x[0],x[1]])
         # eg.(m-1,n-1) -> respectively cost[x[0],x[1]]=cost[m-1,n-1] matching.

    path.append((0, 0))
    return cost, path


def main():
    A = np.array([6,2,3,1,2,3,4,5,6])
    B = np.array([4,5,1,2,3,4,5,6,3,2,7,8])
    cost, path = DTW(A, B)
    print ('cost matrix')
    print (cost)
    print ('optimal path')
    print (path)
    import matplotlib.pyplot as plt
    offset = 5
    plt.xlim([-1, max(len(A), len(B)) + 1])
    plt.subplot(2,1,1)
    plt.xlim([-1, max(len(A), len(B)) + 1])
    plt.plot(A)
    plt.plot(B + offset)

    plt.subplot(2,1,2)
    plt.plot(A)
    plt.plot(B + offset)
    for (x1, x2) in path:
        plt.plot([x1,x2], [A[x1], B[x2] + offset])
    plt.show()

if __name__ == '__main__':
    main()
