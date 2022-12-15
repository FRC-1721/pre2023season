# Subsystems
from subsystems.drivetrain import Drivetrain

# Constants
from constants.constants import getConstants


class RobotContainer:
    def __init__(self):

        constants = getConstants("robot_controls")
        self.control_const = constants["driver"]

        self.drivetrain = Drivetrain.robot_drive
        # controls
        # stick
        self.stick = wpilib.Joystick(self.control_const[controller_port])

        # RE drive
        # self.controler = wpilib.Joystick(1)

    def teleopPeriodic(self):
        # do when we have control
        # for joystick
        self.robot_drive.arcadeDrive(
            self.stick.getZ() * -1 / 2, self.stick.getY() * -1 / 2
        )

        # for RE drive
        # self.as_motor.set(self.controler.getRawAxis(1) / 6)
        # self.ap_motor.set(self.controler.getRawAxis(5) * -1 / 6)


if __name__ == "__main__":
    wpilib.run(KitKatToaster)
