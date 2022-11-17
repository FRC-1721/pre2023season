import wpilib
import wpilib.drive

from rev import CANSparkMax, CANSparkMaxLowLevel


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

        # setting drive type
        self.robot_drive = wpilib.drive.DifferentialDrive(self.ap_motor, self.as_motor)

        # controls
        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        # do when we have control
        self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(KitKatToaster)
