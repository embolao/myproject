import unittest
from mylibreria.camera import Controller, Sensor, Recorder
"""
Objetivo:
Software para una cámara de vigilancia.
Partes:
    Sensor de movimiento.
        - Algo ha empezado a moverse.  TRUE
        - Cuando llevamos X segundos en que nada se mueve. FALSE
    Grabador.
        - Empezar la grabación.  Función: start_recording
        - Detener la grabación.  Función: stop_recording
    Controlador (software)
        - Nuestro objetivo es programar esta pieza.
"""


class CameraTestsUsingMonkeyPatchingForMocks(unittest.TestCase):
    """docstring for CameraTestsUsingMonkeyPatchingForMocks"""
    def test_asks_the_recorder_to_stop_recording_when_no_information_received_from_sensor(self):
        """docstring for test_xxx"""
        sensor = Sensor()
        recorder = Recorder()

        # SIMULACION monkey patching
        self.called = False

        def save_call():
            """docstring for save_call"""
            self.called = True

        sensor.is_detecting_movement = lambda: False
        recorder.stop_recording = save_call
        # FIN SIMULACION

        controller = Controller(sensor, recorder)
        controller.record_movement()  # Usa ya las dependencias simuladas
        self.assertTrue(self.called)

    def test_asks_the_recorder_to_start_recording_when_sensor_detects_movement(self):
        """docstring for test_xxx"""
        sensor = Sensor()
        recorder = Recorder()

        # SIMULACION monkey patching
        self.called = False

        def save_call():
            """docstring for save_call"""
            self.called = True

        sensor.is_detecting_movement = lambda: True
        recorder.start_recording = save_call
        # FIN SIMULACION

        controller = Controller(sensor, recorder)
        controller.record_movement()  # Usa ya las dependencias simuladas
        self.assertTrue(self.called)


















class CameraTestsUsingInheritanceMocks(unittest.TestCase):
    """docstring for CameraTestsUsingInheritanceMocks"""
    def test_xxx(self):
        """docstring for test_xxx"""
        pass
