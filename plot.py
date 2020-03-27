import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]        # Stores ARG1 in filename, as in: $ python plot.py ARG1 ARG2 
data = np.loadtxt(filename,skiprows=32,delimiter=",")   # Attempts to load filename into local variable data.
#Skip past row 32 and find variable separated by a comma


## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ python plot.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)
end= (len(data)-1)
strain= data[:,7]
stress= data[:,3]
m,b=np.polyfit(strain,stress,1)
f_linear=np.poly1d((m,b))
reg=(b+m*strain)
#Y=mx+b

plt.plot(strain,stress,color='k',linestyle='-',linewidth=1)

plt.xlabel('Strain(%)')
plt.ylabel('Stress[MPa]')
plt.plot(strain,reg,linestyle='--',linewidth=1,label="Young's Modulus")
plt.legend(loc='best',fontsize=15) #Change font size here on legend
plt.savefig(filename+'.pdf')
plt.show()
print("Young's Modulus = "+str(m))


# Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.



