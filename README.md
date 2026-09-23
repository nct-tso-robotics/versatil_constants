# versatil_constants

[![Tests](https://github.com/nct-tso-robotics/versatil_constants/actions/workflows/test.yml/badge.svg)](https://github.com/nct-tso-robotics/versatil_constants/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/versatil-constants)](https://pypi.org/project/versatil-constants/)
[![Python](https://img.shields.io/pypi/pyversions/versatil-constants)](https://pypi.org/project/versatil-constants/)

Shared domain constants for the VersatIL imitation learning ecosystem. Zero dependencies.

Each "world" (TSO robot testbed, Libero simulation, MetaWorld simulation, PushT, Kitchen, BlockPush, UR3 block-pushing, Multimodal Ant, etc.) has its own module defining observation and action keys that cross the wire between inference clients and environment servers. Shared constants (language keys, gripper types, coordinate systems) live in `shared`.

## Installation

```bash
pip install versatil-constants
```

## Usage

```python
# Shared across all worlds
from versatil_constants.shared import ObsKey, GripperType, BinaryGripperRange

# TSO Robot Testbed
from versatil_constants.tso import TSOCamera, TSOProprioKey

# Libero simulation
from versatil_constants.libero import LiberoCamera, LiberoProprioKey

# MetaWorld simulation
from versatil_constants.metaworld import MetaWorldCamera, MetaWorldProprioKey

# PushT simulation
from versatil_constants.pusht import PushTCamera, PushTProprioKey

# Franka Kitchen simulation
from versatil_constants.kitchen import KitchenCamera, KitchenProprioKey

# BlockPush simulation
from versatil_constants.blockpush import BlockPushProprioKey

# UR3 block-pushing simulation
from versatil_constants.ur3 import UR3ProprioKey

# Multimodal Ant simulation
from versatil_constants.multimodal_ant import MultimodalAntProprioKey

# TOWER simulation
from versatil_constants.tower import TowerCamera, TowerProprioKey
```

## Modules

| Module | Contents |
|--------|----------|
| `shared` | `ObsKey`, `GripperType`, `BinaryGripperRange`, `ActionComputationMethod`, `CoordinateSystem`, `OrientationRepresentation`, `ActionComponent`, `ActionMetadataField` |
| `tso` | `TSOCamera`, `TSOProprioKey` |
| `libero` | `LiberoCamera`, `LiberoProprioKey` |
| `metaworld` | `MetaWorldCamera`, `MetaWorldProprioKey` |
| `pusht` | `PushTCamera`, `PushTProprioKey` |
| `kitchen` | `KitchenCamera`, `KitchenProprioKey` |
| `blockpush` | `BlockPushProprioKey` |
| `ur3` | `UR3ProprioKey` |
| `multimodal_ant` | `MultimodalAntProprioKey` |
| `tower` | `TowerCamera`, `TowerProprioKey`, `TOWER_STATE_KEYS`, `TOWER_ACTION_KEYS` |
