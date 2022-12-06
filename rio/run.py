import wpilib
import wpilib.drive 
from rev import CANSparkMax, CANSparkMaxLowLevel 

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.mt1 = CANSparkMax(1,CANSparkMaxLowLevel.MotorType.kBrushless)
        self.mt2 = CANSparkMax(2,CANSparkMaxLowLevel.MotorType.kBrushless)
        #self.robot_drive = wpilib.drive.DifferentialDrive(self.mt1, self.mt2)
        self.joy = wpilib.Joystick(0) # fb


    def teleopPeriodic(self):
        if(self.joy.getX()):
            self.mt1.set(self.fb.getX())
            self.mt2.set(self.fb.getX())
        if(self.joy.getZ()):
            self.mt1.set(self.joy.getZ())
            self.mt2.set(-self.joy.getZ())

        #self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getX())

if __name__ == '__main__':
    wpilib.run(MyRobot)