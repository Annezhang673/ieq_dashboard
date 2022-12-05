import utility as util
from datetime import datetime, timedelta
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import time


# df = pd.read_csv('book_with_grids.csv')

while True:
    # set time
    current_local = datetime.now()
    current_gmt = current_local + timedelta(days=0, hours=5)
    start = current_gmt - timedelta(days=0, hours=0, minutes=5)
    end = current_gmt
    current_local_display = current_local.strftime('%m/%d/%Y - %H:%M:%S')

    # set target sensor
    sensor_list = pd.read_csv('sensor.csv')
    n = len(list(sensor_list['room']))
    room_list = list(sensor_list['room'])

    co2_sensor = []
    for item in list(sensor_list['co2']):
        co2_sensor.append(item.split(','))

    temp_sensor = []
    for item in list(sensor_list['temp']):
        temp_sensor.append(item.split(','))

    illum_sensor = []
    for item in list(sensor_list['illumination']):
        illum_sensor.append(item.split(','))

    ## create result container
    result = pd.DataFrame()
    result['room'] = room_list
    result['co2'] = ['',] * n
    result['temp'] = ['',] * n
    result['illumination'] = ['',] * n
    result['label'] = ['',] * n
    result['time'] = ['',] * n

    header = ["time", "location_specific", "value"]

    # create function to attach label to the IEQ value
    def get_co2(val):
        if val <= 493.68:
            return 'c1'
        elif val > 493.68 and val <= 604.53:
            return 'c2'
        elif val > 604.53 and val <= 715.38:
            return 'c3'
        return 'c4'


    def get_temp(val):
        if val <= 22.6:
            return 't1'
        elif val > 22.6 and val <= 24.1:
            return 't2'
        elif val > 24.1 and val <= 25.7:
            return 't3'
        return 't4'


    def get_illu(val):
        if val <= 541.02:
            return 'i1'
        elif val > 541.02 and val <= 2406.53:
            return 'i2'
        elif val > 2406.53 and val <= 4272.04:
            return 'i3'
        return 'i4'

    for i in range(n):
        # CO2
        label = ''

        try:
            readings_co2 = util.get_lfdf(
                "co2_ppm", start, end, co2_sensor[i])
            val = round(readings_co2['value'].mean(), 2)
            label += get_co2(val)
            result.at[i, 'co2'] = str(val) + ' ppm'
        except:
            print('----------- pass -----------')
            label += 'xx'
            result.at[i, 'co2'] = 'unavailable now'
            pass
        # temperature
        try:
            readings_temp = util.get_lfdf(
                "Temperature_°C", start, end, temp_sensor[i])
            val = round(readings_temp['value'].mean(), 1)
            label += get_temp(val)
            result.at[i, 'temp'] = str(val) + ' °C'
        except:
            print('----------- pass -----------')
            label += 'xx'
            result.at[i, 'temp'] = 'unavailable now'
            pass
        # illumination
        try:
            readings_ill = util.get_lfdf(
                "Illumination_lx", start, end, illum_sensor[i])
            val = round(readings_ill['value'].mean(), 2)
            label += get_illu(val)
            result.at[i, 'illumination'] = str(val) + ' lx'
        except:
            print('----------- pass -----------')
            label += 'xx'
            result.at[i, 'illumination'] = 'unavailable now'
            pass
        
        result.at[i, 'label'] = label
        result.at[i, 'time'] = current_local_display

    # result.to_csv('real_time_IEQ.csv')
    result.to_json('../public/real_time_IEQ.json', orient='records')

    print('done')

    print('----------- waiting for next update -----------')
    time.sleep(300)
    