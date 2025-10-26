import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,2,4,5],dtype=float)
y=np.array([2.9,7.6,15.5,20.3],dtype=float)

n=2
m=len(x)

x_sum=[np.sum(x**k) for k in range(2*n+1)]
xy_sum=[np.sum((x**k)*y) for k in range(n+1)]

A=np.zeros((n+1,n+1))
B=np.zeros(n+1)

for i in range(n+1):
    for j in range(n+1):
        A[i,j]=x_sum[i+j]
    B[i]=xy_sum[i]

a=np.linalg.solve(A,B)
print("Coefficient are(a0,a1,a2): ",a)

y_pred=np.zeros_like(x)
for i in range(n+1):
    y_pred+=a[i]*(x**i)

plt.scatter(x,y,color="red",label="data point")
plt.plot(x,y_pred,color="green",label=f"Degree {n} fitted curve")
plt.legend()
plt.show()
