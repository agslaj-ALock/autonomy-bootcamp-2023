"""
BOOTCAMPERS TO COMPLETE.

Travel to designated waypoint.
"""

import math

from .. import commands
from .. import drone_report

# Disable for bootcamp use
# pylint: disable-next=unused-import
from .. import drone_status
from .. import location
from ..private.decision import base_decision


# Disable for bootcamp use
# No enable
# pylint: disable=duplicate-code,unused-argument


class DecisionSimpleWaypoint(base_decision.BaseDecision):
    """
    Travel to the designed waypoint.
    """

    def __init__(self, waypoint: location.Location, acceptance_radius: float) -> None:
        """
        Initialize all persistent variables here with self.
        """
        self.waypoint = waypoint
        print(f"Waypoint: {waypoint}")

        self.acceptance_radius = acceptance_radius

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

    def run(
        self, report: drone_report.DroneReport, landing_pad_locations: "list[location.Location]"
    ) -> commands.Command:
        """
        Make the drone fly to the waypoint.

        You are allowed to create as many helper methods as you want,
        as long as you do not change the __init__() and run() signatures.

        This method will be called in an infinite loop, something like this:

        ```py
        while True:
            report, landing_pad_locations = get_input()
            command = Decision.run(report, landing_pad_locations)
            put_output(command)
        ```
        """
        # Default command
        command = commands.Command.create_null_command()

        # ============
        # ↓ BOOTCAMPERS MODIFY BELOW THIS COMMENT ↓
        # ============

        status = report.status
        relative_x = self.waypoint.location_x - report.position.location_x
        relative_y = self.waypoint.location_y - report.position.location_y
        complete = self.flight_complete(relative_x, relative_y)

        if status == drone_status.DroneStatus.HALTED:
            if complete:
                command = commands.Command.create_land_command()
                print("Drone has landed")
            else:
                command = commands.Command.create_set_relative_destination_command(
                    relative_x, relative_y
                )
                print("Drone is heading to the destination")
        elif status == drone_status.DroneStatus.MOVING and complete:
            command = commands.Command.create_halt_command()

        # ============
        # ↑ BOOTCAMPERS MODIFY ABOVE THIS COMMENT ↑
        # ============

        return command

    def flight_complete(self, x: float, y: float):
        "Function printing if the drone is in the acceptance radius"
        distance = math.sqrt(pow(x, 2) + pow(y, 2))
        return distance < self.acceptance_radius
