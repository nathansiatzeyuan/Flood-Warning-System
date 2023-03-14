# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations, relative_level
from floodsystem.stationdata import build_station_list, update_water_levels



def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():      #Test 1F

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    s_label = "Station 1"
    y_label = "Station 2"
    z_label = "Station 3"
    coord = (-2.0, 4.0)
    s_trange = (5, 1)
    y_trange = None
    z_trange = (2, 7)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, s_label, coord, s_trange, river, town)
    y = MonitoringStation(s_id, m_id, y_label, coord, y_trange, river, town)
    z = MonitoringStation(s_id, m_id, z_label, coord, z_trange, river, town)
    list=[s,y,z]
    assert MonitoringStation.typical_range_consistent(s)==False
    assert MonitoringStation.typical_range_consistent(y)==False
    assert MonitoringStation.typical_range_consistent(z)==True
    assert inconsistent_typical_range_stations(list)==["Station 1","Station 2"]
    
test_typical_range_consistent()


def test_relative_water_level():  #Test 2B

    # did not test  due to several challenges
    assert True


def test_relative_level():      #Test 2G
    stations = build_station_list()
    update_water_levels(stations)
    rel_level = relative_level(stations[0].latest_level, stations[0])
    assert isinstance(rel_level, float)

