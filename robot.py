import wpilib
import wpilib.drive
from rev import CANSparkMax, CANSparkMaxLowLevel
from robot_damp import UrMomsToaster_damp


class UrMomsToaster(wpilib):
    def robotInit(self):
        self.as_motor = CANSparkMax(2, CANSparkMaxLowLevel.MotorType.kBrushless)
        self.ap_motor = CANSparkMax(1, CANSparkMaxLowLevel.MotorType.kBrushless)
        self.robot_drive = wpilib.drive.DifferentialDrive(self.as_motor, self.ap_motor)
        self.stick = wpilib.Joystick(1)
        self.damp = UrMomsToaster()

    def teleop(self):
        self.robot_drive.arcadeDrive(
            self.damp(self.stick.getZ()), self.damp(self.stick.getY())
        )


if __name__ == "__main__":
    wpilib.run(UrMomsToaster)
