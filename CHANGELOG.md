# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- TOWER camera, proprioceptive state, and absolute-action keys, including the
  canonical state/action concatenation order.

## [0.3.0] - Unreleased

### Removed
- **Breaking:** Removed the invalid TSO proprio keys
  `ROBOT_FRAME_CARTESIAN_TIP_ORI` and `CAMERA_FRAME_CARTESIAN_TIP_ORI`.
  Use `RELATIVE_PIVOT_ROLL` for the controlled scalar pivot roll.

## [0.2.2] - 2026-08-28

### Added
- TSO proprio key `RELATIVE_PIVOT_ROLL` for relative pivot-roll actions.

## [0.2.1] - 2026-05-05

### Added
- PushT wire protocol constants: `PushTCamera`, `PushTProprioKey`.
- Franka Kitchen wire protocol constants: `KitchenCamera`, `KitchenProprioKey`.
- BlockPush wire protocol constants: `BlockPushProprioKey`.
- UR3 block-pushing wire protocol constants: `UR3ProprioKey`.
- Multimodal Ant wire protocol constants: `MultimodalAntProprioKey`.

## [0.2.0] - 2026-04-12

### Added
- TSO observation keys: `TSOObsKey` with `PHASE_LABEL`.

### Changed
- **Breaking:** Moved `PHASE_LABEL` from `ObsKey` (shared) to `TSOObsKey` (tso). `ObsKey` now only contains `LANGUAGE`.

## [0.1.1] - 2026-03-16

### Added
- Shared wire protocol constants: `ActionComponent`, `ActionMetadataField`.
- TSO camera keys: `DISPARITY_MAP`, `POINT_CLOUD`.

## [0.1.0] - 2026-03-15

### Added
- Shared wire protocol constants: `ObsKey`, `GripperType`, `BinaryGripperRange`, `ActionComputationMethod`, `CoordinateSystem`, `OrientationRepresentation`.
- TSO world constants: `TSOCamera`, `TSOProprioKey`.
- Libero world constants: `LiberoCamera`, `LiberoProprioKey`.
- MetaWorld world constants: `MetaWorldCamera`, `MetaWorldProprioKey`.

[Unreleased]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.2.2...v0.3.0
[0.2.2]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/nct-tso-robotics/versatil_constants/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/nct-tso-robotics/versatil_constants/releases/tag/v0.1.0
