from magicbot import AutonomousStateMachine, tunable, timed_state

from components.drivetrain import Drivetrain


class TwoSteps(AutonomousStateMachine):

    MODE_NAME = "Two Steps"
    DEFAULT = True

    drivetrain: Drivetrain

    drive_speed = tunable(0.2)

    @timed_state(duration=2, next_state="do_something", first=True)
    def dont_do_something(self):
        """This happens first"""
        pass

    @timed_state(duration=5)
    def do_something(self):
        """This happens second"""
        self.drivetrain.vectorDrive(self.drive_speed, 0)
