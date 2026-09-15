"""Constants for the TSO Robot Testbed world."""

from enum import Enum


class TSOCamera(str, Enum):
    """Camera identifiers for the TSO testbed."""

    LEFT = "left"
    RIGHT = "right"
    DEPTH = "depth"
    DISPARITY_MAP = "disparity_map"
    POINT_CLOUD = "point_cloud"


class TSOObsKey(str, Enum):
    """Non-proprioceptive observation keys for TSO surgical robotics tasks."""

    PHASE_LABEL = "phase_label"


class TSOProprioKey(str, Enum):
    """Proprioceptive observation and action keys for the TSO testbed."""

    ROBOT_FRAME_CARTESIAN_TIP_POS = "proprio_robot_frame"
    CAMERA_FRAME_CARTESIAN_TIP_POS = "proprio_camera_frame"
    RELATIVE_PIVOT_ROLL = "relative_pivot_roll"
    GRIPPER_STATE = "gripper_state_obs"
    GRIPPER_STATE_ACTION = "gripper_state_action"
