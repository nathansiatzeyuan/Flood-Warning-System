
import numpy as np
from datetime import timedelta

from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def test_polyfit():   #Test 2F
 
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
    p_coeff = polyfit(dates, levels, 3)
    assert isinstance(p_coeff, np.ndarray)
    assert len(p_coeff) == 4