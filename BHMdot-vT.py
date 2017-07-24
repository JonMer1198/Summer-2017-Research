import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.axes as ax

k = np.loadtxt('BHMdot-time.txt')

time = k[:,0]
mdot = k[:,1]

logPlot=plt.gca()
logPlot.semilogy(k[:,0],k[:,1],'b-', lw = 2) # logged y axis
logPlot.set_xlabel('Time (in $10{^9}$ yr)', fontsize = 12) # x and y axis labels
logPlot.set_ylabel('BH Mass Accretion (in $M_{\odot}/yr$)')
logPlot.set_xlim(0.0,4.5) # the range of x and y values
logPlot.set_ylim(1e-08,1.0000000000000001e-05)
#plt.ticklabel_format(style= 'sci', scilimits= (0,0))
plt.savefig('BHMdot-time')
plt.show(logPlot)
#print mdot


# plt.plot(k[:,0],k[:,1],'b-', lw= 2,)
# plt.xlabel('Time (in $10{^9}$ yr)', fontsize = 12)
# plt.ylabel('BH Mass Accretion (in $M_{\odot}/yr$)', fontsize=12)
# # plt.xlim(0,4.1)
# # plt.ylim(99000,145000)
# plt.title('Mass of BH at some Time t')
# plt.ticklabel_format(style= 'sci', scilimits= (0,0))
# ax.semilogy()
# plt.show()

print plt.axis()