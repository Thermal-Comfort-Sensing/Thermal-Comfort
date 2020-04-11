#!/usr/bin/env morseexec
# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name

import morse.builder as mb
import thermalcomfort.builder as tb

# Human.
human = mb.Human()
human.translate(-0.50, 3.00, 0.00)
human.rotate(0.00, 0.00, 3.14)

# Set human's temperature to be detected by robot's thermometer.
human.properties(temperature="head,100.00")

# Robot.
robot = mb.Morsy()
robot.translate(-3.50, 3.00, 0.00)
robot.rotate(0.00, 0.00, 0.00)
robot.add_default_interface("socket")

# Keyboard controller to move the robot with arrow keys.
keyboard = mb.Keyboard()
keyboard.properties(ControlType="Position")
robot.append(keyboard)

# Robot's camera.
camera = mb.VideoCamera()
camera.translate(0.00, 0.00, 0.85)
camera.rotate(0.00, 0.00, 0.00)
camera.properties(cam_width=512, cam_height=512)
robot.append(camera)

# Robot's thermometer.
thermosensor = tb.ThermoSensor()
thermosensor.translate(0.00, 0.00, 0.00)
thermosensor.rotate(0.00, 0.00, 0.00)
robot.append(thermosensor)

# Environment.
env = mb.Environment("sandbox", fastmode=False)
env.set_camera_location([-18.00, -6.70, 10.80])
env.set_camera_rotation([1.09, 0.00, -1.14])
