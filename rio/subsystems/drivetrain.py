import wpilib
import wpilib.drive

from rev import CANSparkMax, CANSparkMaxLowLevel

from constants.constants import getConstants


class Drivetrain(SubsystemBase):
    def __init__(self):
        super().__init__()

        self.drive_const = constants["drivetrain"]
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
