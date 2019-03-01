import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
np.random.seed(seed=42)
mu = np.array([7,5]).reshape(2,1)
mu_c = np.array([4,3]).reshape(2,1)
fig = plt.figure(figsize=(10,10))
ax0 = fig.add_subplot(111)
ax0.set_xlim(-1,10)
ax0.set_ylim(-1,10)
# Plot the meshgrid
X,Y = np.meshgrid(np.linspace(-1,10,num=12),np.linspace(-1,10,num=12))
data = np.array([X.reshape(1,144),Y.reshape(1,144)]).reshape(2,144)
ax0.scatter(X,Y)
# Transform the data using w
w = np.array([[0.5,0],[0,0.5]])
data_trans = np.dot(data.T,w)
mu_trans = np.dot(mu.reshape(2,1).T,w).reshape(2,1)
mu_c_trans = np.dot(mu_c.reshape(2,1).T,w).reshape(2,1)
ax0.scatter(data_trans[:,0],data_trans[:,1],alpha=0.8,color='grey',edgecolor='black')
# Plot mu, mu_trans, mu_k, and mu_k_trans
# Plot mu and mu_k
for i in [mu,mu_c,mu_trans,mu_c_trans]:
    ax0.scatter(i[0],i[1],s=80)
ax0.annotate('mu',[mu[0],mu[1]])
ax0.annotate('mu_c',mu_c)
ax0.annotate('mu_c_transformed',mu_c_trans)
ax0.annotate('mu_transformed',mu_trans)
plt.show()
