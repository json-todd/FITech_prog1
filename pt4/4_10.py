"""
COMP.CS.100 4.10 Triangle's angle
Creator: Tri Phung
Student ID: tuni.fi:K441912
"""

def calculate_angle(angle_1, angle_2=90):
    """Calculate the angle of the triangle, knowing the other twos

    Args:
        angle_1 (int): the angle of the triangle
        angle_2 (int, optional): the other angle. Defaults to 90.

    Returns:
        [int]: the last angle of the triangle
    """
    return 180 - angle_1 - angle_2
