from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
stations=build_station_list()
lat=52.2053
lon=0.1218
cambridge_coord = (lat, lon) # (lat, lon)

#10 nearest
stations=stations_by_distance(stations,cambridge_coord)
print(stations[:10])

#10 furtherst
print(stations[-10:])