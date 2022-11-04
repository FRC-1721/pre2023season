#!/bin/python

import wpilib
from magicbot import MagicRobot

# Components
from components.component1 import Component1
from components.component2 import Component2


class Robot(MagicRobot):
    # Define components here.
    component1: Component1
    component2: Component2

    # Constants for components
    SOME_CONSTANT = 1

    def createObjects(self) -> None:
        """
        Initialize all wpilib motors & sensors
        """

        self.component1_motor = wpilib.Talon(1)
        self.some_motor = wpilib.Talon(2)

        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        """
        Iterated in teleop (so, things that the driver/operator need to interact with
        and not anything else)
        """

        try:
            if self.joystick.getTrigger():
                self.component2.do_something()
        except:
            self.onException()


if __name__ == "__main__":
    wpilib.run(Robot)
