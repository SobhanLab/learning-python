import numpy as np
import matplotlib.pyplot as plt

x=np.array([2,3,4,5])
y=np.array([1.6,3.4,4.5,5.8])
m=len(x)
sum_x=np.sum(x)
sum_y=np.sum(y)
sum_xy=np.sum(x*y)
sum_x2=np.sum(x*x)
x_mean=sum_x/m
y_mean=sum_y/m

a1=(m*sum_xy - (sum_x*sum_y))/(m*sum_x2 - (sum_x**2))
a0=y_mean- (a1*x_mean)
print(f"Slope(a1): {a1:.3f}")
print(f"Slope(a0): {a0:.3f}")

y_pred=a0 + a1*x
plt.scatter(x,y,color="red",label="Data points")
plt.plot(x,y_pred,color="green",label="Best fitted line")
plt.legend()
plt.show()