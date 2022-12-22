import wpilib
import wpilib.drive
from rev import CANSparkMax, CANSparkMaxLowLevel


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.mt1 = CANSparkMax(1, CANSparkMaxLowLevel.MotorType.kBrushless)
        self.mt2 = CANSparkMax(2, CANSparkMaxLowLevel.MotorType.kBrushless)
        # self.robot_drive = wpilib.drive.DifferentialDrive(self.mt1, self.mt2)
        self.joy = wpilib.Joystick(0)  # fb

    def teleopPeriodic(self):
        damp = 0.1
        square = 0.3
        if self.joy.getZ() > square or self.joy.getZ() < -square:
            self.mt1.set(self.joy.getZ() * damp * -1)
            self.mt2.set(self.joy.getZ() * damp * -1)
        elif self.joy.getY() > square or self.joy.getY() < -square:
            self.mt1.set(self.joy.getY() * damp * -1)
            self.mt2.set(-self.joy.getY() * damp * -1)
        else:
            self.mt1.set(0)
            self.mt2.set(0)

        # self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)
