
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

N=9
stations=build_station_list()


print(rivers_by_station_number(stations,N))