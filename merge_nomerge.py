import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys

def AllPlot(arg):
    if arg is 'merger' :
        d = np.loadtxt('blackholes-merger.txt', usecols= [0,2,4,6])
        sfr = np.loadtxt('sfr-merger.txt', usecols = [2])

        time = (d[:,0])/ 0.73
        mass = d[:,1]
        mdot = d[:,2]
        mdoter = d[:,3]
        
        fig = plt.figure(figsize=(14,14))
        gs = gridspec.GridSpec(2, 2) # make a grid of 2x2
        
        ax1 = fig.add_subplot(gs[0,0]) # ax1 is is in upper right
        ax1.semilogy(time, mdot, 'b-') # semilogy with mdot vs time , blue line
        ax1.axvline(4.071671232876712, color = 'k') # create a vertical line inputing x value
        ax1.annotate('max accretion rate', xy=(4.071671232876712, max(mdot) ),
                     xytext=(2.07, max(mdot)),arrowprops=dict(arrowstyle="->", facecolor='black'))
        # create a text within ax1 with text, location, location of text, and properties of the arrow pointing to location
        ax1.set_ylabel('BH Mass Accretion (in $M_{\odot}$ $yr^{-1}$)') # set y label
        
        
        ax2 = fig.add_subplot(gs[0,1])
        ax2.semilogy(time, sfr, 'y-')
        ax2.axvline(3.53312328767, color = 'k')
        ax2.annotate('max SFR rate', xy=(3.53312328767, max(sfr) ), xytext=(1.07, max(sfr)),arrowprops=dict(arrowstyle="->", facecolor='black'))
        ax2.set_ylabel('SFR (in $M_{\odot}$)')
        
        
        ax3 = fig.add_subplot(gs[1,0])
        ax3.semilogy(time, mass, 'm-')
        ax3.set_ylabel('Mass (in $M_{\odot}$)')
        
        
        ax4 = fig.add_subplot(gs[1,1])
        ax4.semilogy(time, mdoter, 'r-')
        ax4.set_ylabel('BH Mass Accretion compared to Eddington Accretion')
        ax1.set_xlabel('Time (in $10{^9}$ yr)')
        ax2.set_xlabel('Time (in $10{^9}$ yr)')
        ax3.set_xlabel('Time (in $10{^9}$ yr)')
        ax4.set_xlabel('Time (in $10{^9}$ yr)')
        
        
        gs.update(wspace=0.15, hspace=0.1)
        # updates the grid, wspace= spacing in the width, hspace= spacing in the height
        plt.suptitle('Data for Merger', y= 0.92, fontsize = 18)
        # title for the whole subplot, name, y= location in height, font size
        plt.savefig('Merger Data'+'.pdf')
        # saves the figure, name +'.pdf' makes it a pdf
        
        mdot1=mdot
        mdoter1=mdoter
        sfr1=sfr
        time1=time
        mass1=mass 
        
    else:
        d = np.loadtxt('blackholes-nomerger.txt', usecols= [0,2,4,6])
        sfr = np.loadtxt('sfr-nomerger.txt', usecols = [2])

        time = (d[:,0])/ 0.73
        mass = d[:,1]
        mdot = d[:,2]
        mdoter = d[:,3]
        
        
        fig = plt.figure(figsize=(14,14))
        gs = gridspec.GridSpec(2, 2) # make a grid of 2x2
        
        ax1 = fig.add_subplot(gs[0,0]) # ax1 is is in upper right
        ax1.semilogy(time, mdot, 'b-') # semilogy with mdot vs time , blue line
        ax1.axvline(3.84695890411, color = 'k') # create a vertical line inputing x value
        ax1.annotate('max accretion rate', xy=(3.84695890411, max(mdot) ),
                     xytext=(2.07, max(mdot)),arrowprops=dict(arrowstyle="->", facecolor='black'))
        # create a text within ax1 with text, location, location of text, and properties of the arrow pointing to location
        ax1.set_ylabel('BH Mass Accretion (in $M_{\odot}$ $yr^{-1}$)') # set y label
        
        
        ax2 = fig.add_subplot(gs[0,1])
        ax2.semilogy(time, sfr, 'y-')
        ax2.axvline(0.0712492054795, color = 'k')
        ax2.annotate('max SFR rate', xy=(0.0712492054795, max(sfr) ), xytext=(1.07, max(sfr)),arrowprops=dict(arrowstyle="->", facecolor='black'))
        ax2.set_ylabel('SFR (in $M_{\odot}$)')
        
        
        ax3 = fig.add_subplot(gs[1,0])
        ax3.semilogy(time, mass, 'm-')
        ax3.set_ylabel('Mass (in $M_{\odot}$)')
        
        
        ax4 = fig.add_subplot(gs[1,1])
        ax4.semilogy(time, mdoter, 'r-')
        ax4.set_ylabel('BH Mass Accretion compared to Eddington Accretion')
        ax1.set_xlabel('Time (in $10{^9}$ yr)')
        ax2.set_xlabel('Time (in $10{^9}$ yr)')
        ax3.set_xlabel('Time (in $10{^9}$ yr)')
        ax4.set_xlabel('Time (in $10{^9}$ yr)')
        
        
        gs.update(wspace=0.15, hspace=0.1)
        # updates the grid, wspace= spacing in the width, hspace= spacing in the height
        plt.suptitle('Data for No Merger', y= 0.92, fontsize = 18)
        # title for the whole subplot, name, y= location in height, font size
        plt.savefig('No Merger Data'+'.pdf')
        # saves the figure, name +'.pdf' makes it a pdf

def mergetxt():
        d = np.loadtxt('blackholes-merger.txt', usecols= [0,2,4,6])
        sfr = np.loadtxt('sfr-merger.txt', usecols = [2])

        time = (d[:,0])/ 0.73
        mass = d[:,1]
        mdot = d[:,2]
        mdoter = d[:,3]
        
        time1=time
        mass1=mass
        mdot1=mdot
        mdoter1=mdoter
        sfr1=sfr
        
        maxmdotrow = mdot1.argmax(axis=0)
        sfr_at_t_max = sfr1[maxmdotrow]

        t_max = time1[maxmdotrow]
        acmed = np.median(mdot1)

        ratio = (max(mdot1) / acmed) * 100

        sfrmed = np.median(sfr1)

        ratio1 = (sfr_at_t_max / sfrmed) * 100

        sys.stdout=open("merger.txt","w")
        print ("Row with max accretion is row " + str(maxmdotrow))
        print ("Time at max accretion is: " + str(t_max) + ' Gyr')
        print ("Max accretion rate is: " + '%e' %max(mdot1) + ' solar masses per year')
        print ("Median of Accretion Rate is " + '%e' %acmed + ' solar masses per year')
        print ("The maximum accretion rate is " + str(ratio) + " percent higher than the median.") 
        print ("SFR at max accretion is: " + "%e" %sfr_at_t_max + " solar masses per year")
        print ("Median of SFR is " + '%e' %sfrmed + ' solar masses per year')
        print ("The SFR at the max accretion rate time is " + str(ratio1) + ' percent higher than the median.')
        maxsfrrow = sfr1.argmax(axis=0)
        mdot_at_t_max = mdot1[maxsfrrow]

        t_max = time1[maxsfrrow]
        acmed = np.median(mdot1)

        ratio = (mdot_at_t_max / acmed) * 100

        sfrmed = np.median(sfr1)

        ratio1 = (max(sfr1) / sfrmed) * 100

        print "Row with max SFR is row " + str(maxsfrrow)
        print "Time at max SFR is: " + str(t_max) + ' Gyr'
        print "Max SFR rate is: " + '%e' %max(sfr1) + ' solar masses per year'
        print "Median of SFR Rate is " + '%e' %sfrmed + ' solar masses per year'
        print "The maximum SFR rate is " + str(ratio1) + " percent higher than the median." 
        print "Accretion at max SFR is: " + "%e" %mdot_at_t_max + " solar masses per year"
        print "Median of accretion rate is " + '%e' %acmed + ' solar masses per year'
        print "The accretion rate at the max SFR rate time is " + str(ratio) + ' percent higher than the median.'
        #sys.stdout.close()        

def nomergetxt():
        d = np.loadtxt('blackholes-nomerger.txt', usecols= [0,2,4,6])
        sfr = np.loadtxt('sfr-nomerger.txt', usecols = [2])

        time = (d[:,0])/ 0.73
        mass = d[:,1]
        mdot = d[:,2]
        mdoter = d[:,3]   
        
        maxmdotrow = mdot.argmax(axis=0)
        sfr_at_t_max = sfr[maxmdotrow]

        t_max = time[maxmdotrow]
        acmed = np.median(mdot)

        ratio = (max(mdot) / acmed) * 100

        sfrmed = np.median(sfr)

        ratio1 = (sfr_at_t_max / sfrmed) * 100

        sys.stdout=open("nomerger.txt","w")
        print ("Row with max accretion is row " + str(maxmdotrow))
        print ("Time at max accretion is: " + str(t_max) + ' Gyr')
        print ("Max accretion rate is: " + '%e' %max(mdot) + ' solar masses per year')
        print ("Median of Accretion Rate is " + '%e' %acmed + ' solar masses per year')
        print ("The maximum accretion rate is " + str(ratio) + " percent higher than the median.") 
        print ("SFR at max accretion is: " + "%e" %sfr_at_t_max + " solar masses per year")
        print ("Median of SFR is " + '%e' %sfrmed + ' solar masses per year')
        print ("The SFR at the max accretion rate time is " + str(ratio1) + ' percent higher than the median.')
        maxsfrrow = sfr.argmax(axis=0)
        mdot_at_t_max = mdot[maxsfrrow]

        t_max = time[maxsfrrow]
        acmed = np.median(mdot)

        ratio = (mdot_at_t_max / acmed) * 100

        sfrmed = np.median(sfr)

        ratio1 = (max(sfr) / sfrmed) * 100

        print "Row with max SFR is row " + str(maxsfrrow)
        print "Time at max SFR is: " + str(t_max) + ' Gyr'
        print "Max SFR rate is: " + '%e' %max(sfr) + ' solar masses per year'
        print "Median of SFR Rate is " + '%e' %sfrmed + ' solar masses per year'
        print "The maximum SFR rate is " + str(ratio1) + " percent higher than the median." 
        print "Accretion at max SFR is: " + "%e" %mdot_at_t_max + " solar masses per year"
        print "Median of accretion rate is " + '%e' %acmed + ' solar masses per year'
        print "The accretion rate at the max SFR rate time is " + str(ratio) + ' percent higher than the median.'
        #sys.stdout.close()
        
def Parameter(m):
    if m is 'merger':
        AllPlot('merger')
        mergetxt()
    else:
        AllPlot('no merger')
        nomergetxt()
