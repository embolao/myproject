class Sensor:
    """Simulado"""

    def is_detecting_movement(self) -> bool:
        """Mucho código"""
        pass


class Recorder:
    """Simulado"""

    def start_recording(self):
        """Mucho código"""
        pass

    def stop_recording(self):
        """Mucho código"""
        pass


###########################################################


class Controller:
    """description"""

    def __init__(self, sensor: Sensor, recorder: Recorder):
        self.__sensor = sensor
        self.__recorder = recorder

    def record_movement(self):
        """docstring for record_movement"""
        if self.__sensor.is_detecting_movement():
            self.__recorder.start_recording()
        else:
            self.__recorder.stop_recording()
