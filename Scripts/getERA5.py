#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "ea",
    "dataset": "era5",
    "expver": "1",
    "levtype": "sfc",
    #"number": "0",
    # for codes see http://apps.ecmwf.int/codes/grib/param-db
    # 228.128=tp, 144.128=sf
    "param": "144.128",
    # as we are getting total precip, we need to forecast how much precip comes down over 
    # the next 12 hours (hence the step)
    # but I think ERA-5 just gives the mean hourly accumulation
    "step": "1/to/12/by/1",
    #"step": "12",
    # in 0.5 degrees lat/lon
    "grid": "0.5/0.5",
    "stream": "oper",
    "date": "2016-01-01/to/2016-12-31",
    # see above comment. This should actually be 0 and 12 to give the total through the day, 
    # so offset by 6 hours currently. Hopefully they update this soon

    "time": "06:00:00/18:00:00",
    "type": "fc",
    "format" : "netcdf",
    # set an output file name
    "target": "ERA5_sf_2016yrOperTest.nc",

})