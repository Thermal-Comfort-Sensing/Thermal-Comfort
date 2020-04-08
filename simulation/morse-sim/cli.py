#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name

import sys
import base64

import pymorse
from PIL import Image


def main():
    with pymorse.Morse() as simu:
        camera = simu.robot.camera
        thermometer = simu.robot.thermometer

        print_help()
        while True:
            print("> ", end="", flush=True)

            try:
                cmd = input()
            except KeyboardInterrupt:
                cmd = "exit"
                print("")

            if cmd == "help":
                print_help()
            elif cmd == "exit":
                sys.exit(0)
            elif cmd == "cam":
                camera_handler(camera.get())
            elif cmd == "therm":
                thermometer_handler(thermometer.get())


def thermometer_handler(data):
    print("Thermometer: {}".format(data))


def camera_handler(data):
    print("Picture taken. (Size: {}x{})".format(data["height"], data["width"]))
    raw = base64.b64decode(data["image"])
    img = Image.frombytes("RGBA", (data["width"], data["height"]), raw).convert("RGB")
    img.show()


def print_help():
    print(
        "\nCommands:\n\n"
        "  help\t show this help message\n"
        "  exit\t exit the program\n"
        "  cam\t take a picture using robot's camera\n"
        "  therm\t read robot's thermometer value\n"
    )


if __name__ == "__main__":
    main()
