#Logarithmic Fibonacci
import matplotlib.pyplot as plt
from math import sqrt
from time import time
from math import log

def mat_mul_2by2(X,Y):
    z1 = X[0][0]*Y[0][0]+X[0][1]*Y[1][0]
    z2 = X[0][0]*Y[0][1]+X[0][1]*Y[1][1]
    z3 = X[1][0]*Y[0][0]+X[1][1]*Y[1][0]
    z4 = X[1][0]*Y[0][1]+X[1][1]*Y[1][1]
    return [[z1,z2],[z3,z4]]

def fibonacci(n):
    if n == 0:
        return [[n,n]]
    if n == 1:
        return [[1,1],[1,0]]
    if n == 2:
        return mat_mul_2by2([[1,1],[1,0]],[[1,1],[1,0]])
    x = fibonacci(n//2)
    if n%2==0:
        return mat_mul_2by2(x,x)
    elif n%2 == 1:
        return mat_mul_2by2(mat_mul_2by2(x,x),[[1,1],[1,0]])
length = 1000
times = []
for i in range(length):
    temp = []
    for j in range(50):
        t0 = time()
        f = fibonacci(i)[0][1]
        temp.append(time()-t0)
    times.append(sum(temp)/len(temp))
        
    
times_avg = []
for i in range(50):
    t1 = time()
    f0 = fibonacci(0)[0][1]
    times_avg.append(time()-t1)
    
time_avg = sum(times_avg)/len(times_avg)
n_line = [time_avg*i for i in range(length)]
n_log = [4*time_avg*log(i+1) for i in range(length)]
    
h = [i for i in range(length)]
sample = 5
h1 = [h[h0] for h0 in range(len(h)) if h0%sample==0]
n_line1 = [n_line[h0] for h0 in range(len(n_line)) if h0%sample==0] 
plt.plot(h1[:200//sample],n_line1[:200//sample],'r',label='n')
plt.plot(h1,[times[h0] for h0 in range(len(times)) if h0%sample==0],label='Fibonacci')
plt.plot([h[h0] for h0 in range(len(h)) if h0%sample==0],
         [n_log[h0] for h0 in range(len(n_log)) if h0%sample==0],'g',label='log(n)')
plt.xlabel('$n^{th}$ Fibonacci')
plt.ylabel('Time (sec)')
plt.legend()
plt.savefig('FiboLog.png',dpi=500)
plt.show()