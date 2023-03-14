from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

stations=build_station_list()
rivers_with_station = list(rivers_with_station(stations))
no_of_stations_with_rivers=len(rivers_with_station)

#Number of rivers with a station(s)
print(no_of_stations_with_rivers)

#First 10 rivers
rivers_with_station.sort()
print(rivers_with_station[:10])

#Stations of the river
stations_by_river(stations,"River Aire")
stations_by_river(stations,"River Cam")
stations_by_river(stations,"River Thames")
