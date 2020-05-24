import serial
import time
import datetime
import csv
import mysql.connector


def connection(port):  # Connect to Arduino
    try:
        print(f"Trying...")
        arduino = serial.Serial(port, 9600)  # Set COM port to connected
        print(f' Connected to: {arduino.name}')
        return arduino
    except NameError as err0:
        print(f"Failed to connect, check no other connections active")


def write_to_csv(data):  # Write data to CSV
    now = datetime.datetime.now()
    with open('readings.csv', 'a', newline='') as file:
        writer = csv.writer(
            file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow([now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), data[0],
                         data[1], data[2], data[3]])
    return print(f'record written at {now.strftime("%Y-%m-%d")}')


def write_to_SQL(data):  # Write data to SQL database
    now = datetime.datetime.now()
    mySQLdb = mysql.connector.connect(
        host="localhost",
        user="sqluser",
        passwd="IyySGieRucpIc2ogtB8X",
        database="weather_station",
        auth_plugin='mysql_native_password'
    )
    mycursor = mySQLdb.cursor()

    sql = "INSERT INTO arduino (date, time, LightLevel, AirQuality, Humidity, Temperature) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"),
           data[0], data[1], data[2], data[3])
    mycursor.execute(sql, val)
    mySQLdb.commit()
    print(mycursor.rowcount, "record inserted.")
    mySQLdb.close()


# Main run code
if __name__ == "__main__":
    comm_port = 'COM6'  # NEEDS TO BE SET BEFORE RUNNING
    connected_arduino = connection(comm_port)

    while True:
        try:
            data = connected_arduino.readline()
            clean_data = data.decode('UTF-8')
            pieces = str(clean_data).split(",")
            # write_to_csv(pieces)
            write_to_SQL(pieces)
            time.sleep(300)
        except IndexError as err1:
            print('No data recieved (First connection has a delay)')
            print('Waiting for re-attempt')
            time.sleep(30)
