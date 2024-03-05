from classes.connection import connection
from classes.missions import Missions
import time
import threading


class Abis:
    def __init__(self, server_ip, port):
        self.connection = connection(server_ip, port)
        self.connection.start_connection()

        self.current_mission = 0
        self.is_waiting_to_start = 0
        self.immediate_stop = 0

        self.data_gathering = threading.Thread(target=self.data_loop())
        self.data_gathering.start()

        self.missions = Missions()

    def data_loop(self):
        last_data = 0
        while True:
            self.current_mission = self.connection.get_current_mission_number()
            self.is_waiting_to_start = self.connection.get_current_start_status()
            self.immediate_stop = self.connection.get_current_stop_status()
            time.sleep(0.1)
            if last_data != self.current_mission:
                print(f"data from thread. ", self.current_mission)
                last_data = self.current_mission



    def get_data(self):
        if not self.connection.isConnected: return {};

        mission_number = self.connection.get_current_mission_number()
        starting = self.connection.get_current_start_status()
        stop = self.connection.get_current_stop_status()
        data = self.connection.get_current_data()

        return {"mission_number": mission_number, "starting": starting, "stop": stop, "data": data}