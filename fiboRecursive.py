
#Recursive Fibonacci
from time import time
import matplotlib.pyplot as plt
from math import sqrt

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return fibonacci(n-1) + fibonacci(n-2)

times = []
length = 35
for i in range(length):
    t0 = time()
    f = fibonacci(i)
    times.append(time()-t0)
    
times_avg = []
for i in range(100):
    t1 = time()
    f0 = fibonacci(0)
    times_avg.append(time()-t1)
    
time_avg = sum(times_avg)/len(times_avg)
n_line = [time_avg*i**3 for i in range(length)]
phi = (1+sqrt(5))/2
expon = [time_avg*phi**i for i in range(length)]
h = [i for i in range(length)]
plt.plot(h,expon,'r',label='$\phi^n$')
plt.plot(h,times,label='Fibonacci')
plt.plot(h,n_line,'g',label='$n^3$')
plt.xlabel('$n^{th}$ Fibonacci')
plt.ylabel('Time (sec)')
plt.legend()
plt.savefig('FiboRecursive.png',dpi=500)
plt.show()