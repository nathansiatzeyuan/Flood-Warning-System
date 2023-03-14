from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_highest_rel_level


stations = build_station_list()
update_water_levels(stations)
N=10
list_of_tuples=stations_highest_rel_level(stations, N)
for t in list_of_tuples:
        print(t[0].name, t[1])

