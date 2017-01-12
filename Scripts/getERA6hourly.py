
# Read in 6-hourly ERA-Interim data, average (within given lat/lon bounds) and output yearly data.
# This script works for 6 hourly data of 2 m temp (t2m), 2 m dew point, surface pressure (sp) and u/v winds (u10/v10)
# By Alek Petty
# 12/01/2017

import matplotlib
matplotlib.use("AGG")
# Numpy import
from pylab import *
from netCDF4 import Dataset
# basemap import
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='spstere',boundinglat=-40.,lon_0=-45., lat_ts=0.0,resolution='l'  )

rawdatapath='../../../../DATA/'
figPath='../Figures/'
outPath='../Output/ERAI/'
lonlat = [240., 255., -73.5, -71.]

varStr='sp'

f1 = Dataset(rawdatapath+'ERAI/'+varStr+'.nc', 'r')
var = f1.variables[varStr][:].astype(float32)

if (varStr=='t2m'):
	var=var-273.15

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
	varMYr = varM[x*(4*numdays):(x+1)*(4*numdays)]
	savetxt(outPath+'/'+varStr+'/'+varStr+year+'.txt', varMYr)

