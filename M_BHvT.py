import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

d = np.loadtxt('BHmass-time.txt')


plt.plot(d[:,0],d[:,1],'p-', lw= 2,)
plt.xlabel('Time (in $10{^9}$ yr)', fontsize = 12)
plt.ylabel('BH Mass (in $M_{\odot}$)', fontsize=12)
plt.xlim(0,4.1)
plt.ylim(99000,145000)
plt.title('Mass of BH at some Time t')
plt.ticklabel_format(style= 'sci', scilimits= (0,0))
plt.show()