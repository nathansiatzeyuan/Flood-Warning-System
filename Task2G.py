import datetime
import numpy as np
from floodsystem.datafetcher import fetch, fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation, relative_level
from floodsystem.flood import stations_level_over_threshold


stations = build_station_list()
update_water_levels(stations)
list_of_stations_levels = stations_level_over_threshold(stations, 1)  # List of stations which is prone to flood (threshold>1)

dt=3 # 3 days data
time=dt*86400 #time in seconds for number of days
hour=1 # predicted 1 hour later relative water level
t=time+3600*hour  
s_tol = 10 #severe flood tolerance
h_tol = 5 #high risk flood tolerance
m_tol = 1 #moderate risk flood tolerance
#<1 low risk
severe_warnings = [[],[],[]]
for station in list_of_stations_levels:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=dt)) #3 days data
    coeffs = polyfit(dates, levels, 3)
    poly = np.poly1d(coeffs)
    rel_level = relative_level(poly(t), station[0])
    if rel_level > s_tol:
        # risk = "Severe"
        severe_warnings[0].append((station[0].town,rel_level))
    elif rel_level > h_tol:
        # risk = "High"
        severe_warnings[1].append((station[0].town,rel_level))
    elif rel_level > m_tol:
        # risk = "Moderate"
        severe_warnings[2].append((station[0].town,rel_level))
print("WARNING: These stations have a SEVERE risk of flooding:\n"+str(severe_warnings[0]))
print("\n\n")
print("WARNING: These stations have a HIGH risk of flooding:\n"+str(severe_warnings[1]))
print("\n\n")
print("WARNING: These stations have a MODERATE risk of flooding:\n"+str(severe_warnings[2]))
