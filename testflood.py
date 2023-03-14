from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
#Test 2B
def test_stations_level_over_threshold():
    stations = build_station_list()
    over_threshold = stations_level_over_threshold(stations, 0.8)
    assert isinstance(over_threshold, list)


#Task 2C
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    highest_rel_level = stations_highest_rel_level(stations, N)
    assert isinstance(highest_rel_level, list)
    assert len(highest_rel_level) == N

