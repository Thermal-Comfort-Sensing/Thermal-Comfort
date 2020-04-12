#!/usr/bin/env python3

import sys
import base64
import pprint

import pymorse
from PIL import Image


def main():
    with pymorse.Morse() as sim:
        camera = sim.robot.camera
        thermosensor = sim.robot.thermosensor

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
            elif cmd == "pic":
                picture_handler(camera)
            elif cmd == "temp":
                temperature_handler(thermosensor)
            elif cmd != "":
                print("Command \"{}\" not supported.".format(cmd))


def picture_handler(camera):
    data = camera.get()
    print("Picture taken. (Size: {}x{})".format(data["height"], data["width"]))
    raw = base64.b64decode(data["image"])
    img = Image.frombytes("RGBA", (data["width"], data["height"]), raw).convert("RGB")
    img.show()


def temperature_handler(thermosensor):
    pprint.PrettyPrinter(indent=2).pprint(thermosensor.get())


def print_help():
    print(
        "\nCommands:\n\n"
        "  help\t show this help message\n"
        "  exit\t exit the program\n"
        "  pic\t take a picture using robot's camera\n"
        "  temp\t get human's temperature data\n"
    )


if __name__ == "__main__":
    main()
