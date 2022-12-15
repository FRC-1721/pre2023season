import wpilib
import wpilib.drive

from rev import CANSparkMax, CANSparkMaxLowLevel

from constants.constants import getConstants


class Drivetrain(SubsystemBase):
    def __init__(self):
        super().__init__()

        constants = getConstants("robot_hardware")
        self.drive_const = constants["drivetrain"]

        # motor declaration
        self.ap_motor = CANSparkMax(
            self.drive_const[ap_motor],
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.as_motor = CANSparkMax(
            self.drive_const[as_motor],
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.robot_drive = wpilib.drive.DifferentialDrive(self.ap_motor, self.as_motor)
