from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        x = 0
        while x != 3:
            print(TrafficLight.__color[x])
            if x == 0:
                sleep(7)
            elif x == 1:
                sleep(2)
            elif x == 3:
                sleep(8)
            x += 1


light = TrafficLight()
light.running()