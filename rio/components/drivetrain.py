import wpilib.drive

from rev import CANSparkMax as CSM


class Drivetrain:
    """
    This is a low level component for the drivetrain.
    """

    # Motor controllers
    fp_motor: CSM
    fs_motor: CSM

    # Vector targets
    thro = 0
    rot = 0

    def on_enable(self):
        # Kinematics
        self.kmatic = wpilib.drive.DifferentialDrive(self.fp_motor, self.fs_motor)

    def vectorDrive(self, thro, rot):
        """
        Takes a manual throttle and manual rotation
        (a drawn vector)
        """

        self.thro = thro
        self.rot = rot

    def execute(self):
        """
        Runs every iteration.
        """

        self.kmatic.arcadeDrive(self.thro, self.rot)
