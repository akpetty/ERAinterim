import matplotlib
matplotlib.use("AGG")
# Numpy import
from pylab import *
from netCDF4 import Dataset
from matplotlib import rc
# basemap import
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

rcParams['xtick.labelsize']=10
rcParams['font.size']=10
rc('font',**{'family':'sans-serif','sans-serif':['Arial']})

m = Basemap(projection='spstere',boundinglat=-40.,lon_0=-45., lat_ts=0.0,resolution='l'  )

rawdatapath='../../../../DATA/'
figPath='../Figures/'
outPath='../Output/ERAI/'

varStr='t2m'
labelStr='2 m temperature (C)'

#varStr='v10'
#labelStr='v10 winds (m/s)'

year='2010'
varMYr =loadtxt(outPath+'/'+varStr+'/'+varStr+year+'.txt')

time=np.arange(0, size(varMYr)*60*6, 60*6)
timeN=np.arange(30*6, size(varMYr)*60*6-(30*6), 1)



varMYrN = griddata(time,varMYr, timeN, method='linear')

savetxt(outPath+'/'+varStr+'/'+varStr+year+'int.txt', varMYrN)


fig = figure(figsize=(4,2.5))
subplots_adjust(left = 0.13, right = 0.99, bottom=0.16, top = 0.96)

plot(time, varMYr, '--', linewidth = 0.25, color='r', alpha=0.5)
plot(timeN, varMYrN, '-', linewidth = 0.5, color='0.6', alpha=0.5)

ylabel(labelStr)
xlabel('Time (hours)')
savefig(figPath+'/'+varStr+year+'downscale.pdf', dpi=200)


