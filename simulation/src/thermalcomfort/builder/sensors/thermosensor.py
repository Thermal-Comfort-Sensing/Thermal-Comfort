from morse.builder.creator import SensorCreator
from morse.builder.blenderobjects import Cylinder


class ThermoSensor(SensorCreator):
    _classpath = "thermalcomfort.sensors.thermosensor.ThermoSensor"

    def __init__(self, name=None):
        SensorCreator.__init__(self, name)
        mesh = Cylinder("ThermometerCylinder")  # Reuse objects of Thermometer.
        mesh.scale = (.02, .02, .04)
        mesh.color(0, .6, .5)
        self.append(mesh)
