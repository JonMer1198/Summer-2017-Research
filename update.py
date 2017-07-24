import merge_nomerge as mnm
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt

#mnm.Parameter('merger')

#mnm.Parameter('nomerger')

d = np.loadtxt('blackholes-merger.txt', usecols= [0,2,4,6])
sfr = np.loadtxt('sfr-merger.txt', usecols = [2])

time = (d[:,0])/ 0.73
mass = (d[:,1] * 10**10) / 0.73
mdot = d[:,2]
mdoter = d[:,3]

mdotwmed = mdot / np.median(mdot)
sfrwmed = sfr / np.median(sfr)

logplot = plt.gca()
logplot.plot(time, mdotwmed, 'b-', label = '<Mass Accretion>')
logplot.plot(time, sfrwmed, 'r-', label = '<SFR>')
logplot.set_xlim(2.45,4.1)
#logplot.set_ylim(10**-1, 10)
logplot.set_xlabel('Time (in $10^{9}$ yr)')
logplot.set_ylabel('<Mass Accretion and SFR>(in $M_{\odot}$ $yr^{-1})$')
logplot.legend()
plt.show(logplot)

