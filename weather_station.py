import serial
import time
import datetime
import csv

# Connect to Arduino


def connection(port):
    try:
        print(f"Trying...")
        arduino = serial.Serial(port, 9600)  # Set COM port to connected
        print(f' Connected to: {arduino.name}')
        return arduino
    except NameError as err0:
        print(f"Failed to connect, check no other connections active")

# Write data to CSV and add date and time


def write_to_csv(data):
    now = datetime.datetime.now()
    with open('readings.csv', 'a', newline='') as file:
        writer = csv.writer(
            file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow([now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), data[0],
                         data[1], data[2], data[3]])
    return print(f'record written at {now.strftime("%Y-%m-%d")}')

# Write data to SQL database


def write_to_SQL(data):
    pass


# Main run code
if __name__ == "__main__":
    comm_port = 'COM6'
    connected_arduino = connection(comm_port)

    while True:
        try:
            data = connected_arduino.readline()
            clean_data = data.decode('UTF-8')
            pieces = str(clean_data).split(",")
            write_to_csv(pieces)
            time.sleep(300)
        except IndexError as err1:
            print('No data recieved (First connection has a delay)')
            print('Waiting for re-attempt')
            time.sleep(30)
