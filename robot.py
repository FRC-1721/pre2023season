import wpilib.drive 
import wpilib
from rev import CANSparkMax, CANSparkMaxLowLevel 

class KitkatBot(wpilib.TimedRobot):
    def robotInit(self):
        self.motorleft = CANSparkMax(1,CANSparkMaxLowLevel.MotorType.kBrushless)
        self.motorright = CANSparkMax(2,CANSparkMaxLowLevel.MotorType.kBrushless)
        self.robotdrive = wpilib.drive.DifferentialDrive (self.motorright, self.motorleft)
        self.stick = wpilib.joystick(0)
    def teleoPeriodic(self):
        self.arcadeDrive(self.stick.getY(), self.stick.getX())
if __name__ == "__main__":
    wpilib.run(KitkatBot)



