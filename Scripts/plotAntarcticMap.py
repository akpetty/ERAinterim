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

def get_box_xy(m, lonlat):
    lats = np.zeros((40))
    lats[0:10] = np.linspace(lonlat[3], lonlat[2], 10)
    lats[10:20] = np.linspace(lonlat[2], lonlat[2], 10)
    lats[20:30] = np.linspace(lonlat[2], lonlat[3], 10)
    lats[30:40] = np.linspace(lonlat[3], lonlat[3], 10)
    lons = np.zeros((40))
    lons[0:10] = np.linspace(lonlat[1], lonlat[1], 10)
    lons[10:20] = np.linspace(lonlat[1], lonlat[0], 10)
    lons[20:30] = np.linspace(lonlat[0], lonlat[0], 10)
    lons[30:40] = np.linspace(lonlat[0], lonlat[1], 10)
    xpts, ypts = m(lons, lats)

    return xpts, ypts

m = Basemap(projection='spstere',boundinglat=-55.,lon_0=180, lat_ts=0.0,resolution='l'  )

rawdatapath='../../../DATA/'
figPath='../Figures/'
lonlat = [240., 255., -73.5, -71.]
xptsB, yptsB = get_box_xy(m, lonlat)

fig = figure(figsize=(4,4))
subplots_adjust(left = 0.01, right = 0.99, bottom=0.01, top = 0.99)

m.fillcontinents(color='w',lake_color='grey', zorder=3)
m.drawcoastlines(linewidth=0.25, zorder=5)
m.drawparallels(np.arange(90,-90,-5), linewidth = 0.25, zorder=10)
m.drawmeridians(np.arange(-180.,180.,30.), latmax=85, linewidth = 0.25, zorder=10)
m.plot(xptsB, yptsB, '--', linewidth = 1, color='k', zorder=12)


#savefig(out_path+'/Ridges_6years'+ftype+out_var+'.pdf', dpi=200)
savefig(figPath+'/Antarctica.png', dpi=200)