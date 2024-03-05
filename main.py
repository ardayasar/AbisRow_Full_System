import time
from classes.abis import Abis

vehicle = Abis("http://localhost", "3000")

while True:
    # print(vehicle.get_data())
    time.sleep(1)

