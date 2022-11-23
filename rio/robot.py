#!/bin/python
import wpilib
from magicbot import MagicRobot

# Vendor Libs
from rev import CANSparkMax as CSM
from rev import CANSparkMaxLowLevel as CSMLL

# Components
from components.drivetrain import Drivetrain


class Robot(MagicRobot):
    # Define components here.
    drivetrain: Drivetrain

    # Constants for components
    SOME_CONSTANT = 1

    def createObjects(self) -> None:
        """
        Initialize all wpilib motors & sensors
        """

        self.fp_motor = CSM(0, CSMLL.MotorType.kBrushless)
        self.fs_motor = CSM(1, CSMLL.MotorType.kBrushless)

        self.driverStick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        """
        Iterated in teleop (so, things that the driver/operator need to interact with
        and not anything else)
        """

        try:
            self.drivetrain.vectorDrive(
                self.driverStick.getX(),
                self.driverStick.getZ(),
            )
        except:
            self.onException()


if __name__ == "__main__":
    wpilib.run(Robot)
