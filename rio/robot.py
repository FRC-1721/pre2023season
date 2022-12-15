import wpilib

from robotcontainer import RobotContainer


class KitKatToaster(wpilib.TimedRobot):
    def robotInit(self):
        self.container = RobotContainer()

    def teleopPeriodic(self):
        self.container.teleop()


if __name__ == "__main__":
    wpilib.run(KitKatToaster)
