import time

def mission(number):
    missions = {
        0: mission_1(),
        1: mission_2()
    }

    return missions[number]


class mission_1:
    def __init__(self):
        self.example = 0

    def start(self):
        self.main()

    def main(self):
        # Buradaki fonksiyonunuz ana fonksiyonunuz olmasi gerekmektedir. Sadece dışarıdan çağırıldığı zaman çalışmalı.
        print("Starting mission")


class mission_2:
    def __init__(self):
        self.example = 0

    def start(self):
        self.main()

    def main(self):
        # Buradaki fonksiyonunuz ana fonksiyonunuz olmasi gerekmektedir. Sadece dışarıdan çağırıldığı zaman çalışmalı.
        print("Starting mission")

# ---------------- DİKKAT ----------------
# Bu alandan sonrası Missions.py dir.
# Bu alanın yukarısında bulunanlar sizlerin yapması gereken örnek görev classıdır
# ---------------- DİKKAT ----------------


class Missions:
    def __init__(self):
        self.current_mission = 0
        self.is_in_water = 0
        self.waiting_to_start = 0
        self.mission_end = 0
        self.mission_paused = 0
        self.mission_access = None

    def mission_controller(self):
        last_call = 0
        while True:
            if self.current_mission != last_call:
                last_call = self.current_mission
                self.waiting_to_start = 0
                self.mission_end = 0
                self.mission_paused = 0
                self.mission_access = mission(self.current_mission)

    def change_mission(self, mission_number):
        self.current_mission = mission_number

    def stop_mission(self):
        self.mission_paused = 1

    def destroy_mission(self):
        self.mission_end = 1

    def start_mission(self):
        # Buraya su algılama durumunu entegre ediniz
        self.waiting_to_start = 1
        in_water_waiting_counter = 0
        while True:
            if self.is_in_water:
                in_water_waiting_counter += 1
                time.sleep(1)
            else:
                in_water_waiting_counter = 0
                time.sleep(1)

            if in_water_waiting_counter == 5:
                self.mission_access.start()