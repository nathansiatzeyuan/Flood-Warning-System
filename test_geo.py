from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
def test_station_coord():            #Task 1B
    stations=build_station_list()
    list=stations_by_distance(stations,(1,1))
    assert isinstance (list[0][0],str)
    assert isinstance (list[0][1],str)
    assert isinstance (list[0][2],float)
    for station in stations:
        assert station.coord is not None
        assert isinstance (station.coord,tuple)
        assert isinstance (station.coord[0],float)
        assert isinstance (station.coord[1],float)

test_station_coord()
def test_stations_within_radius():         #Task 1C
    stations=build_station_list()
    list=stations_within_radius(stations,(0,0), 5)
    for i in list:
        assert type(i) == str
test_stations_within_radius()    
    
def test_stations_by_distance():         #Task 1B
    stations=build_station_list()
    list=stations_by_distance(stations, (52.2063, 0.1202))
    for i in list:
        assert type(i) == tuple
test_stations_by_distance()
def test_river():                     #Task 1D.1
    stations=build_station_list()
    for station in stations:
        assert(station.river,str)
    assert (rivers_with_station(stations),set)
test_river()
def test_dictionary_combine():       #Task 1D.2
    dict={"R1":"S1","R2":"S1"}
    dict2={"R1":"S2","R2":"S2"}
    for key,value in dict2.items():
            if key in dict:
                if isinstance(dict[key], list):
                    dict[key].append(value)
                else:
                    temp_list = [dict[key]]
                    temp_list.append(value)
                    dict[key] = temp_list
            else:
                dict[key] = value
    
    assert dict=={"R1":["S1","S2"],"R2":["S1","S2"]}    
test_dictionary_combine()  

def test_taskE():                                         #Task 1E
    dict={"R1":["S1","S2"],"R2":["S1","S2"],"R3":["S1"]}  
    list1=[]
    for key,value in dict.items():
        if isinstance(value, list):
            a=(key,len(value))
        else:
            a=(key,1)

        list1.append(a)

    list1=sorted_by_key(list1,1,True)
    N=1
    while list1[N-1][1]==list1[N][1]:
        N+=1
    assert list1[:N]==[("R1",2),("R2",2)]
    
test_taskE()

    
def test_rivers_by_station_number():
    stations = build_station_list()
    rivers_by_station_number_testlist = rivers_by_station_number(stations,100)
    assert type(rivers_by_station_number_testlist) == list
    for i in rivers_by_station_number_testlist:
        assert type(i[0]) == str
        assert type(i[1]) == int

test_rivers_by_station_number()

    
