from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

stations=build_station_list()   # pick out 1 station then sub it into line 9
update_water_levels(stations)

list_of_highest_rel_level = stations_highest_rel_level(stations, 5)

for station in list_of_highest_rel_level:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=10))
    plot_water_levels(station[0], dates, levels)


