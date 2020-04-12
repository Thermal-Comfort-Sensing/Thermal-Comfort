import logging; logger = logging.getLogger("morse." + __name__)
import math

import morse.core
from morse.helpers.components import add_data, add_property


class ThermoSensor(morse.core.sensor.Sensor):
    _PROP_TEMP = "temperature"
    _PROP_BODY_PARTS = "body_parts"
    _DELIMS = ["|", ":", ","]
    _ALPHA = 0.15

    _name = "ThermoSensor"

    add_data("temperatures", [], "list", "Measured temperatures")

    def __init__(self, obj, parent=None):
        logger.info("Initializing %s", obj.name)
        morse.core.sensor.Sensor.__init__(self, obj, parent)
        logger.info("Initialized (Freq: %.2f Hz)", self.frequency)

    def default_action(self):
        temperatures = []
        for obj in morse.core.blenderapi.scene().objects:
            try:
                temperature = obj[ThermoSensor._PROP_TEMP]
                body_parts = obj[ThermoSensor._PROP_BODY_PARTS]
                temperatures.append({
                    "name": obj.name,
                    "temperatures": self._compute_body_temperatures(temperature, body_parts),
                })
            except KeyError as e:
                logger.debug("Exception: %s", e)
        self.local_data["temperatures"] = temperatures

    def _compute_body_temperatures(self, temperature, body_parts):
        temperatures = []
        for chunk in body_parts.split(ThermoSensor._DELIMS[0]):
            label, raw_coord = chunk.split(ThermoSensor._DELIMS[1])
            x, y, z = raw_coord.split(ThermoSensor._DELIMS[2])
            temperatures.append({
                "label": label,
                "value": temperature * math.exp(-ThermoSensor._ALPHA * self._dist(x, y, z))
            })
        return temperatures

    def _dist(self, x, y, z):
        return float(x) ** 2 + float(y) ** 2 + float(z) ** 2
