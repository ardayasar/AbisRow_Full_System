import time
import socket
import socketio


class connection:
    def __init__(self, server_ip, tcp_port):
        self.server_ip = server_ip
        self.tcp_port = tcp_port
        self.socket = socketio.Client()
        self.isConnected = False

        self.mission_number = 0
        self.starting = 0
        self.stop = 0
        self.data = {"0": "0"}

        # Mission Numbers
        #-----------------
        # 1 - Line Tracking
        # 2 - Torpedo Shot
        # 3 - Passing Door with Color Flag
        #-----------------

        # Starting
        # ----------------
        # Only set 1 if mission is starting
        # ----------------

        # Stop
        # ----------------
        # Use to stop the vehicle or code
        # ----------------

        # Data
        # ----------------
        # Other data sent from server or user
        # ----------------

        @self.socket.event
        def connect():
            print(f"Connection success to {self.server_ip}:{self.tcp_port}")
            self.isConnected = True

        @self.socket.event
        def disconnect():
            print(f"Connection dropped from {self.server_ip}:{self.tcp_port}")
            self.isConnected = False
            self.socket.disconnect()
            self.socket = socketio.Client()
            self.start_connection()

        @self.socket.event
        def mission_status(data):
            self.mission_number = int(data)

        @self.socket.event
        def set_starting(data):
            self.starting = int(data)

        @self.socket.event
        def set_stop(data):
            self.stop = int(data)

    def start_connection(self):
        connection_try_count = 0
        while not self.isConnected:

            if connection_try_count == 3:
                self.find_server()
                connection_try_count = 0

            try:
                self.socket.connect(f"{self.server_ip}:{self.tcp_port}")
                self.isConnected = True
                connection_try_count = 0
            except Exception as e:
                self.socket.disconnect()
                connection_try_count += 1
                print(f"Connection to {self.server_ip}:{self.tcp_port} couldn't established. Trying again in 3 seconds. Try count: {connection_try_count}")
                time.sleep(2.6)

    def drop_connection(self):
        self.socket.disconnect()

    def find_server(self):
        print(f"Searching ip address by port {self.tcp_port}")
        did_find = self.finder()
        if did_find:
            print(f"Found server ip address: {self.server_ip}")
        else:
            print(f"Not found any server. Starting back")

    def finder(self):
        test_socket = socketio.Client()
        for t_block in range(255):
            for f_block in range(255):
                testing_ip_address = f"192.168.{t_block}.{f_block}"
                try:
                    test_socket.connect(testing_ip_address + self.tcp_port)
                except:
                    continue

                self.server_ip = testing_ip_address
                test_socket.disconnect()
                return True

        test_socket.disconnect()
        return False

    def get_current_mission_number(self):
        return self.mission_number

    def get_current_start_status(self):
        return self.starting

    def get_current_stop_status(self):
        return self.stop

    def get_current_data(self):
        return self.data
