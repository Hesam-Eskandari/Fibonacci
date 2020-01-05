#Linear Fibonacci
import matplotlib.pyplot as plt
from math import sqrt, log
import time


def fibonacci(n,l=[0,1],i=1):
    #time.sleep(1)
    #print(l,i)
    if i == 1:
        l = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif i == n:
        return l[1]
    else:
        s = sum(l)
        l[0] = l[1]
        l[1] = s
        return fibonacci(n,l,i+1)
        
times = []

length = 1000

for i in range(length):
    temp = []
    for j in range(50):
        t0 = time.time()
        f = fibonacci(i)
        temp.append(time.time()-t0)
    times.append(sum(temp)/len(temp))
    
times_avg = []
for i in range(1000):
    t1 = time.time()
    f0 = fibonacci(0)
    times_avg.append(time.time()-t1)
    
time_avg = sum(times_avg)/len(times_avg)
n_line = [time_avg*i for i in range(length)]
n_nlog = [time_avg*i*log(i+1) for i in range(700)]
#phi = (1+sqrt(5))/2
#expon = [time_avg*phi**i for i in range(length)]
h = [i for i in range(length)]
#plt.plot(h,expon,'r',label='$\phi^n$')
sample = 8
h1 = [h[h0] for h0 in range(len(h)) if h0%sample==0]
times1 = [times[h0] for h0 in range(len(times)) if h0%sample==0] 
plt.plot(h1,times1,label='Fibonacci')
plt.plot(h,n_line,'g',label='$n$')
plt.plot(h[:700],n_nlog,'r',label='$n log(n)$')
plt.xlabel('$n^{th}$ Fibonacci')
plt.ylabel('Time (sec)')
plt.legend()
plt.savefig('FiboLinear.png',dpi=500)
plt.show()
