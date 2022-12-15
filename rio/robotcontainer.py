# Subsystens
from subsystems.drivetrain import Drivetrain


class KitKatToaster(wpilib.TimedRobot):
    def robotInit(self):
        # motor declaration
        self.ap_motor = CANSparkMax(
            1,
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.as_motor = CANSparkMax(
            2,
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.robot_drive = wpilib.drive.DifferentialDrive(self.ap_motor, self.as_motor)

        # controls
        # stick
        self.stick = wpilib.Joystick(0)

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
