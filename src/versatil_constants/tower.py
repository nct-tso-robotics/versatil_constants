"""Wire protocol keys for the TOWER simulation world."""

from enum import Enum


class TowerCamera(str, Enum):
    """RGB camera observation keys provided by the TOWER evaluator."""

    LEFT_BACK = "left_back_camera"
    RIGHT_FRONT = "right_front_camera"
    LEFT_WRIST = "left_wrist_camera"
    BACK_WRIST = "back_wrist_camera"


class TowerProprioKey(str, Enum):
    """Proprioceptive observation and action keys for TOWER."""

    LEFT_ARM_QPOS = "left_arm_qpos"
    LEFT_GRIPPER_STATE = "left_gripper_state"
    BACK_ARM_QPOS = "back_arm_qpos"
    BACK_GRIPPER_STATE = "back_gripper_state"
    LIFTER_POSITION_MM = "lifter_position_mm"
    LEFT_EEF_POSITION = "left_eef_position"
    LEFT_EEF_ORIENTATION = "left_eef_orientation"
    BACK_EEF_POSITION = "back_eef_position"
    BACK_EEF_ORIENTATION = "back_eef_orientation"
    LEFT_GRIPPER_STATUS = "left_gripper_status"
    BACK_GRIPPER_STATUS = "back_gripper_status"
    LIFTER_PHYSICAL_HEIGHT_MM = "lifter_physical_height_mm"
    LIFTER_IS_MOVING = "lifter_is_moving"
    LIFTER_SAMPLE_AGE_MS = "lifter_sample_age_ms"
    LIFTER_VALID = "lifter_valid"

    LEFT_ARM_QPOS_ACTION = "left_arm_qpos_action"
    LEFT_GRIPPER_ACTION = "left_gripper_action"
    BACK_ARM_QPOS_ACTION = "back_arm_qpos_action"
    BACK_GRIPPER_ACTION = "back_gripper_action"
    LIFTER_ACTION_MM = "lifter_action_mm"


TOWER_STATE_KEYS = (
    TowerProprioKey.LEFT_ARM_QPOS,
    TowerProprioKey.LEFT_GRIPPER_STATE,
    TowerProprioKey.BACK_ARM_QPOS,
    TowerProprioKey.BACK_GRIPPER_STATE,
    TowerProprioKey.LIFTER_POSITION_MM,
)

TOWER_ACTION_KEYS = (
    TowerProprioKey.LEFT_ARM_QPOS_ACTION,
    TowerProprioKey.LEFT_GRIPPER_ACTION,
    TowerProprioKey.BACK_ARM_QPOS_ACTION,
    TowerProprioKey.BACK_GRIPPER_ACTION,
    TowerProprioKey.LIFTER_ACTION_MM,
)
