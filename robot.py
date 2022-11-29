import wpilib # the lib
import wpilib.drive

from rev import CANSparkMax,
from rev import CANSparkMaxLowLevel

class myCringlance():
    
    def robotInit(self):
        self.motorL = CANSparkMax(0, CANSparkMaxLowLevel.MotorType.kBrushless) # left motor, use kBrushless from CANSparkMax
        self.motorR = CANSparkMax(1, CANSparkMaxLowLevel.MotorType.kBrushless) # right motor, same as left

        self.drive = wpilib.drive.DifferentialDrive(self.motorL, self.motorR) # "drive different" - jeve stobs
        self.stick = wpilib.Joystick(0) # wiggly cringlance
    
    def teleopPeriodic(self):
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX()) # make the wiggly cringlance work

if __name == "__main__":
    wpilib.run(myCringlance)
