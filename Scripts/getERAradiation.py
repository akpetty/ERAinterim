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
lonlat = [240., 255., -73.5, -71.]

varStr='ssrd'
#varStr='strd'

f1 = Dataset(rawdatapath+'ERAI/lwsw.nc', 'r')
var = f1.variables[varStr][:]

# Units given in J over a 12 hour period. 
# So to convert to W/m2 we dividee by the number of seconds in 12 hours..
var=var/(60.*60.*12.)

lon = f1.variables['longitude'][:]
lat = f1.variables['latitude'][:]

lonS, latS=np.meshgrid(*(lon, lat))
Amundsen= where((lonS>lonlat[0])&(lonS<lonlat[1])&(latS>lonlat[2])&(latS<lonlat[3]))

varM=mean(var[:, Amundsen[0], Amundsen[1]], axis=1)
#windsuM=mean(windsu[:, Amundsen[0], Amundsen[1]], axis=1)


leapYrs=[1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
#need to update with leap years
for x in xrange(37):
	numdays=365
	if (x+1979) in leapYrs:
		print x+1979
		numdays=366
	year=str(1979+x)
	varMYr = varM[x*(2*numdays):(x+1)*(2*numdays)]
	savetxt(outPath+'/'+varStr+'/'+varStr+year+'.txt', varMYr)

