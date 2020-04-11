import logging; logger = logging.getLogger("morse." + __name__)
import math

import morse.core
from morse.helpers.components import add_data, add_property


class ThermoSensor(morse.core.sensor.Sensor):
    _name = "ThermoSensor"

    add_property("_tag", "temperatures", "TemperaturesTag", "string", "")
    add_property("_tag_delim_outer", "|", "TagOuterDelimiter", "string", "")
    add_property("_tag_delim_inner", ",", "TagInnerDelimiter", "string", "")
    add_property("_alpha", 0.2, "Alpha", "float", "")

    add_data("temperatures", [], "list", "Measured temperatures")

    def __init__(self, obj, parent=None):
        logger.info("Initializing %s", obj.name)
        morse.core.sensor.Sensor.__init__(self, obj, parent)
        logger.info("Initialized (Freq: %.2f Hz)", self.frequency)

    def default_action(self):
        temperatures = []
        for obj in morse.core.blenderapi.scene().objects:
            try:
                raw_temp = obj[self._tag]
                dist, _, _ = self.bge_object.getVectTo(obj)
                temperatures += self._build_temperatures(raw_temp, dist)
            except KeyError:
                pass
        self.local_data["temperatures"] = temperatures

    def _build_temperatures(self, raw_temp, dist):
        temperatures = []
        for chunk in raw_temp.split(self._tag_delim_outer):
            label, val = chunk.split(self._tag_delim_inner)
            temperatures.append({
                "label": label,
                "value": float(val) * math.exp(-self._alpha * dist)
            })
        return temperatures
