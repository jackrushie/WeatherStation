import serial
import time
import datetime
import csv


try:
    print(f"Trying...")
    arduino = serial.Serial('COM6', 9600)
    print(arduino.name)
except:
    print(f"Failed to connect")

while True:
    try:
        data = arduino.readline()
        clean_data = data.decode('UTF-8')
        pieces = str(clean_data).split(",")
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        light_level = pieces[0]
        air_quality = pieces[1]
        humidity = pieces[2]
        temp = pieces[3]
        with open('readings.csv', 'a', newline='') as file:
            writer = csv.writer(
                file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            writer.writerow([date, time, light_level,
                             air_quality, humidity, temp])
        print('record written')

    except IndexError as err1:
        print('no data')
