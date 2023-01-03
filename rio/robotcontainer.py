import wpilib

# Subsystems
from subsystems.drivetrain import Drivetrain

# Commands
from commands.dampen import Dampen

# Constants
from constants.constants import getConstants


class RobotContainer:
    def __init__(self):

        constants = getConstants("robot_controls")
        self.control_const = constants["driver"]
        self.dampen = Dampen()

        self.drivetrain = Drivetrain()

        # controls
        self.controler = wpilib.Joystick(self.control_const["controller_port"])

    def teleop(self):
        # changing dampening
        if self.controler.getRawAxis(self.control_const["clutch"]) >= 0.1:
            self.dampen.change()

        # reverse
        if self.controler.getRawAxis(self.control_const["brake"]) >= 0.1:

            # right turn
            if self.controler.getRawAxis(self.control_const["steer"]) >= 0.1:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=self.controler.getRawAxis(self.control_const["steer"]),
                    )
                    * -1
                )

            # left turn
            elif self.controler.getRawAxis(self.control_const["steer"]) <= -0.1:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=self.controler.getRawAxis(self.control_const["steer"]),
                    )
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                    * -1
                )

            # no turn
            else:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                    * -1
                )

        # forward
        elif self.controler.getRawAxis(self.control_const["accelerate"]) >= 0.1:
            # right turn
            if self.controler.getRawAxis(self.control_const["steer"]) >= 0.1:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                    * -1
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=self.controler.getRawAxis(self.control_const["steer"]),
                    )
                )

            # left turn
            elif self.controler.getRawAxis(self.control_const["steer"]) <= -0.1:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=self.controler.getRawAxis(self.control_const["steer"]),
                    )
                    * -1
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                )

            # no turn
            else:
                self.drivetrain.ap_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                    * -1
                )
                self.drivetrain.as_motor.set(
                    self.dampen.damp(
                        self.controler.getRawAxis(self.control_const["brake"]),
                        decrease=0,
                    )
                )


if __name__ == "__main__":
    wpilib.run(KitKatToaster)
