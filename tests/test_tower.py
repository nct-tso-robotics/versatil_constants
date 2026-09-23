"""Tests for TOWER wire protocol constants."""

from versatil_constants.tower import (
    TOWER_ACTION_KEYS,
    TOWER_STATE_KEYS,
    TowerCamera,
    TowerProprioKey,
)


def test_tower_camera_values_match_evaluator_protocol():
    assert tuple(camera.value for camera in TowerCamera) == (
        "left_back_camera",
        "right_front_camera",
        "left_wrist_camera",
        "back_wrist_camera",
    )


def test_tower_state_keys_preserve_evaluator_layout():
    assert TOWER_STATE_KEYS == (
        TowerProprioKey.LEFT_ARM_QPOS,
        TowerProprioKey.LEFT_GRIPPER_STATE,
        TowerProprioKey.BACK_ARM_QPOS,
        TowerProprioKey.BACK_GRIPPER_STATE,
        TowerProprioKey.LIFTER_POSITION_MM,
    )


def test_tower_action_keys_preserve_evaluator_layout():
    assert TOWER_ACTION_KEYS == (
        TowerProprioKey.LEFT_ARM_QPOS_ACTION,
        TowerProprioKey.LEFT_GRIPPER_ACTION,
        TowerProprioKey.BACK_ARM_QPOS_ACTION,
        TowerProprioKey.BACK_GRIPPER_ACTION,
        TowerProprioKey.LIFTER_ACTION_MM,
    )
