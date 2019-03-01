import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

np.random.seed(seed=42)

x_j = np.array([3.5, 4.5])
mu = np.array([7,5])
mu_k = np.array([4, 3])
fig = plt.figure(figsize=(10,10))

ax0 = fig.add_subplot(111)
ax0.set_xlim(-1, 10)
ax0.set_ylim(-1, 10)
for i in [x_j, mu, mu_k]:
	ax0.scatter(i[0],i[1],s=50)

ax0.annotate('x_j', x_j)
ax0.annotate('mu_k', mu_k)
ax0.annotate('(x_j - mu) = (mu_k - mu) + (x_j - mu_k)',np.array(mu)+np.array([1,1]))

# Draw the position vectors
for i in [x_j, mu, mu_k]:
	ax0.arrow(0, 0, i[0], i[1], head_width=0.01, width=0.05)

# Draw the vectors
ax0.arrow(mu[0],mu[1],(x_j-mu)[0],(x_j-mu)[1],head_width=0.05,width=0.1,color='yellow') # xj_minus_mu
ax0.arrow(mu[0],mu[1],(mu_k-mu)[0],(mu_k-mu)[1],head_width=0.05,width=0.01,alpha=0.5,color='black') # mu_k_minus_mu
ax0.arrow(mu_k[0],mu_k[1],(x_j-mu_k)[0],(x_j-mu_k)[1],head_width=0.05,width=0.01,alpha=0.5,color='black') # xj_minus_mu_k

# If we now add up the vectors (mu_k-mu) and (x_j-mu_k) wee see that this vector alligns with the vector (x_k-mu)
mu_k_minus_mu = mu_k-mu
x_j_minus_mu_k = x_j-mu_k
res = (mu_k-mu)+(x_j-mu_k)
ax0.arrow(mu[0],mu[1],res[0],res[1],head_width=0.05,width=0.01,linestyle='-.',color='red')
plt.show()
