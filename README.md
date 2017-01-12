#ERA-Interim information

https://software.ecmwf.int/wiki/pages/viewpage.action?pageId=56658233

6-hourly data of 2 m air temp, 2 m dew point temp, surface pressure, 10 m winds (all instantaneous)
12 hourly incoming longwave/shortwave and precipitation (summed over 12 hours)


Temperature:

2 m air temp, (4 per day, 6 hourly) C (converted from kelvin)

Specific humidity:

We need to calulate from dew point and surface pressure (4 per day, 6 hourly)

Winds:

10 m winds, (4 per day, 6 hourly)

Can calucalte wind speed cubed from the 6-hourly data. Need to do this before any climatology is calculated (to avoid smoothing out this signal). Similar smoothing issues with other datasets too though.


Radiation:

strd, surface thermal radiation downwards (downward longwave radiation),  (2 per day, 12 hourly)

ssrd, Surface solar radiation downwards (downward solar radiation),  (2 per day, 12 hourly)


Precipitation: 

Total downward precipitation (2 per day, 12 hourly)

Note that ERA-I gives the integral of precipitation over some time period (I took it to be twelve hours to be consistent with the 12 hurly time steps, so both together give the total precipitation in a day). To express as kg/m2/s i multiplied by 1000 (density of water) and divided by 12 hours (in seconds).

In Petty we use total precipitation and I think assumes this all falls into the ocean? In new appraoch we might want to say set to snow (if temp less than zero?) and have some fraction contributing to snow accumulation, and the rest os freshwater input through leads/open water.








