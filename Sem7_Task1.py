import time


class Traffic_light:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        while True:
            if self.__color == 'red':
                print('Red light')
                time.sleep(4)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print('Yellow light')
                time.sleep(2)
                self.__color = 'green'
            elif self.__color == 'green':
                print('Green light')
                time.sleep(4)
                self.__color = 'red'


traffic_light = Traffic_light()
traffic_light.running()
