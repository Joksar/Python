import time

class TrafficLight:
    __color = None

    def running(self):
        while True:
            __color = "Red"
            print(__color)
            time.sleep(3)
            __color = "Yellow"
            print(__color)
            time.sleep(2)
            __color = "Green"
            print(__color)
            time.sleep(2)

light = TrafficLight()
light.running()
