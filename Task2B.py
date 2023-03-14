from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

station = build_station_list()
update_water_levels(station)

list_of_tuples = stations_level_over_threshold(station, 0.8)
for t in list_of_tuples:
        print(t[0].name, t[1])
    
