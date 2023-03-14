from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

stations = build_station_list()

Inconsistent_stations = inconsistent_typical_range_stations(stations)
Inconsistent_stations = inconsistent_typical_range_stations(stations)
Inconsistent_stations_sorted = sorted(Inconsistent_stations)

print(Inconsistent_stations_sorted)


    