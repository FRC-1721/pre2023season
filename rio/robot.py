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
        # TODO
        # after other two motors work

        # self.fp_motor = CANSparkMax(
        #     3,
        #     CANSparkMaxLowLevel.MotorType.kBrushless,
        # )
        # self.fs_motor = CANSparkMax(
        #     4,
        #     CANSparkMaxLowLevel.MotorType.kBrushless,
        # )
        # self.port_motors = wpilib.SpeedControllerGroup(self.fp_motor, self.ap_motor)
        # self.starboard_motors = wpilib.SpeedControllerGroup(
        #     self.fs_motor, self.as_motor
        # )

        # setting drive type
        # TODO
        # add with above
        # self.robot_drive = wpilib.drive.DifferentialDrive(
        #     self.port_motors, self.starboard_motors
        # )
        self.robot_drive = wpilib.drive.DifferentialDrive(self.ap_motor, self.as_motor)

        # controls
        # stick
        self.stick = wpilib.Joystick(0)

        # RE drive
        self.controler = wpilib.Joystick(1)

    def teleopPeriodic(self):
        # # do when we have control
        # # for joystick
        self.robot_drive.arcadeDrive(
            self.stick.getZ() * -1 / 2.5, self.stick.getY() / 2.5
        )  # for kids 2.5 = z 2.5 = Y for us 2 = x 2 = y

        # for RE drive
        # self.ap_motor.set(self.controler.getRawAxis(1) / 6)
        # self.as_motor.set(self.controler.getRawAxis(5) * -1 / 6)


if __name__ == "__main__":
    wpilib.run(KitKatToaster)
