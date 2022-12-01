import wpilib
import wpilib.drive 
from rev import CANSparkMax, CANSparkMaxLowLevel 

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.mt1 = CANSparkMax(1,CANSparkMaxLowLevel.MotorType.kBrushless)
        self.mt2 = CANSparkMax(2,CANSparkMaxLowLevel.MotorType.kBrushless)
        #self.robot_drive = wpilib.drive.DifferentialDrive(self.mt1, self.mt2)
        self.fb = wpilib.Joystick(0) # fb
        self.sp = wpilib.Joystick(2) # sp


    def teleopPeriodic(self):
        if(self.fb):
            self.mt1.set(self.fb)
            self.mt2.set(self.fb)
        if(self.sp):
            self.mt1.set(self.sp)
            self.mt2.set(-self.sp)

        #self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getX())

if __name__ == '__main__':
    wpilib.run(MyRobot)