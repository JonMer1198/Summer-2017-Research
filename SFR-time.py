import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.axes as ax

l = np.loadtxt('SFR-time.txt')

# time = k[:,0]
# mdot = k[:,1]

logPlot=plt.gca()
logPlot.semilogy(l[:,0],l[:,1],'m-', lw = 2) # logged y axis
logPlot.set_xlabel('Time (in $10{^9}$ yr)', fontsize = 12) # x and y axis labels
logPlot.set_ylabel('SFR (in $M_{\odot}/yr$)')
# logPlot.set_xlim(0.0,4.5) # the range of x and y values
# logPlot.set_ylim(1e-08,1.0000000000000001e-05)
#plt.ticklabel_format(style= 'sci', scilimits= (0,0))
plt.savefig('SFR-time')
plt.show(logPlot)