import numpy as np

import matplotlib as mpl
mpl.use('Qt5Agg')

import matplotlib.pyplot as plt
plt.ion()

# for the symbolic manipulation
import sympy as sp
from sympy.utilities.lambdify import lambdify

from sympy.solvers import solve

# solve jacobian of constraint equation
(theta_sym, 
 src_dist_sym, 
 fov_sym,
  d_sym) = sp.symbols("""theta_sym 
                            src_dist_sym 
                            fov_sym
                            d_sym""", real = True)

k = sp.sqrt((src_dist_sym*sp.cos((np.pi/2)+theta_sym))**2+(src_dist_sym*sp.sin((np.pi/2)+theta_sym)-d_sym)**2)

solutions = solve(d_sym+k*sp.cos(fov_sym/2)+src_dist_sym*sp.sin(theta_sym)*sp.tan(theta_sym/2)-src_dist_sym, d_sym)



d1 = solutions[0].subs([(src_dist_sym, 10), (fov_sym, (100*np.pi)/180)]).evalf()
d2 = solutions[1].subs([(src_dist_sym, 10), (fov_sym, (100*np.pi)/180)]).evalf()


d1_func = lambdify((theta_sym,), d1)
d2_func = lambdify((theta_sym,), d2)

thetaD1=[]
thetaD2=[]


theta_range = np.arange(0,50.25,0.25)

for theta in theta_range:
    d1 = d1_func((theta*np.pi)/180)
    d2 = d2_func((theta*np.pi)/180)
    thetaD1.append((theta, d1))
    thetaD2.append((theta, d2))

fig, axs = plt.subplots(2, figsize=(10,10))
axs[0].scatter(*zip(*thetaD1))
axs[0].set_title('Case 1 - straight distance before out of fov vs theta')
axs[0].set_xlabel('theta')
axs[0].set_ylabel('distance 1')

axs[1].scatter(*zip(*thetaD2))
axs[1].set_title('Case 2 - straight distance before out of fov vs theta')
axs[1].set_xlabel('theta')
axs[1].set_ylabel('distance 2')
fig.tight_layout()
plt.grid(True)
plt.show()