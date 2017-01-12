import matplotlib
matplotlib.use("AGG")
# Numpy import
from pylab import *
from netCDF4 import Dataset
from matplotlib import rc
# basemap import
from mpl_toolkits.basemap import Basemap
rcParams['xtick.labelsize']=10
rcParams['font.size']=10
rc('font',**{'family':'sans-serif','sans-serif':['Arial']})

m = Basemap(projection='spstere',boundinglat=-40.,lon_0=-45., lat_ts=0.0,resolution='l'  )

rawdatapath='../../../../DATA/'
figPath='../Figures/'
outPath='../Output/ERAI/'

var=5
if (var==0):
	varStr='t2m'
	labelStr='2 m air temperature (C)'
	scale_factor=1
elif (var==1):
	varStr='u10'
	labelStr='u10 winds (m/s)'
	scale_factor=1
elif (var==2):
	varStr='tp'
	labelStr='P (1e-5 kg/m2/s)'
	scale_factor=1e-5
elif (var==3):
	varStr='d2m'
	labelStr='2 m dp temperature (K)'
	scale_factor=1

elif (var==4):
	varStr='ssrd'
	labelStr='Shortwave radiation (W/m2)'
	scale_factor=1

elif (var==5):
	varStr='strd'
	labelStr='Downwelling radiation (W/m2)'
	scale_factor=1

varYrs=[]
for x in xrange(37):
	year=str(1979+x)
	varYrs.append(loadtxt(outPath+'/'+varStr+'/'+varStr+year+'.txt'))



fig = figure(figsize=(4,2.5))
subplots_adjust(left = 0.13, right = 0.99, bottom=0.16, top = 0.96)

for x in xrange(37):
#m.plot(windsuM[0:4*365], '-', linewidth = 1, color='r')
	plot(varYrs[x]/scale_factor, '-', linewidth = 0.25, color='0.6', alpha=0.5)
plot(varYrs[30], '-', linewidth = 0.5, color='r', alpha=0.8)
plot(varYrs[10], '-', linewidth = 0.5, color='g', alpha=0.8)

ylabel(labelStr)
xlabel('Time (hours)')
savefig(figPath+'/'+varStr+'.pdf', dpi=200)