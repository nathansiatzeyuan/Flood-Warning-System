from datetime import datetime, timedelta
import numpy as np

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

N = 5
TIME_PERIOD = 2  # days
POLYNOMIAL_DEGREE = 4

stations = build_station_list()
update_water_levels(stations)
list_of_highest_rel_level = stations_highest_rel_level(stations, N)

for station in list_of_highest_rel_level:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=TIME_PERIOD))
    plot_water_level_with_fit(station[0], dates, levels, POLYNOMIAL_DEGREE)

