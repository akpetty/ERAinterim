#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()

reanalysisDataPath = '/Volumes/PETTY_PASSPORT2/REANALYSES/'

def getERA(year):
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "expver": "1",
        "levtype": "sfc",
        #"number": "0",
        # for codes see http://apps.ecmwf.int/codes/grib/param-db
        # 228.128=tp, 144.128=sf
        "param": "165.128/166.128",
        # as we are getting total precip, we need to forecast how much precip comes down over 
        # the next 12 hours (hence the step)
        "step": "0",
        # in 0.5 degrees lat/lon
        "grid": "0.75/0.75",
        "stream": "oper",
        "date": ""+str(year)+"-01-01/to/"+str(year)+"-12-31",
        # see above comment. 
        "time": "00:00:00/06:00:00/12:00:00/18:00:00",
        "type": "an",
        "format" : "netcdf",
        # set an output file name
        "target": ""+reanalysisDataPath+"ERAI_winds_"+str(year)+".nc",

    })


for x in xrange(2012, 2012+1):
    getERA(x)

