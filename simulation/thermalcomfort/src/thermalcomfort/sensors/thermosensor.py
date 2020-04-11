# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name,missing-class-docstring

import logging; logger = logging.getLogger("morse." + __name__)
import math

import morse.core
from morse.helpers.components import add_data


class ThermoSensor(morse.core.sensor.Sensor):
    _name = "ThermoSensor"
    _attr_temperature = "temperature"
    _attr_temperature_sep = ","
    _alpha = 0.2

    add_data("temperatures", None, "list", "Measured temperatures")

    def __init__(self, obj, parent=None):
        logger.info("Initializing %s", obj.name)
        morse.core.sensor.Sensor.__init__(self, obj, parent)
        logger.info("Initialized (Freq: %.2f Hz)", self.frequency)

    def default_action(self):
        temperatures = []

        for obj in morse.core.blenderapi.scene().objects:
            try:
                raw_temp = obj[ThermoSensor._attr_temperature]
                name, val = raw_temp.split(ThermoSensor._attr_temperature_sep)
                dist, _, _ = self.bge_object.getVectTo(obj)
                temperatures.append({
                    "name": name,
                    "value": float(val) * math.exp(-self._alpha * dist)
                })
            except KeyError:
                pass

        self.local_data["temperatures"] = temperatures
