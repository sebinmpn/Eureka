# import serial.tools.list_ports

# def list_serial_ports():
#     ports = serial.tools.list_ports.comports()
#     if len(ports) == 0:
#         print("No serial ports found.")
#     else:
#         print("Available serial ports:")
#         for port in ports:
#             print(f"  {port.device}")

# if __name__ == "__main__":
#     list_serial_ports()
import serial

# con_baud 921600
# baudrate=115200
def print_serial_data(port, baudrate=921600):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Listening to serial port {port} at {baudrate} baud...")

        while True:
            data = ser.readline().decode('utf-8').strip()
            print(f"Received data: {data}")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    serial_port = "/dev/ttyACM0"  # Change this to your specific serial port
    print_serial_data(serial_port)
