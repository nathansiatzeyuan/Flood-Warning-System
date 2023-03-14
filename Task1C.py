from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

centre_coord = (52.2053, 0.1218)
stations_within10km = stations_within_radius(stations, centre_coord , 10) #distance is in km

print(stations_within10km)
