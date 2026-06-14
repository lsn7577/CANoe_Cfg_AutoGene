# CAN Disturbance Interface CAPL Functions

> Category: `CANDisturbance` | Type: `notes`

## Description

To configure the CAN Disturbance Interface the following functions and methods are available.

Classes

| CAN Only available with CAN Disturbance Interface. To configure the CAN Disturbance Interface the following functions and methods are available. |
|---|

| Functions | Trigger | Output | Short Description |
|---|---|---|---|
| canDisturbanceTriggerEnable | FrameTrigger | Sequence | Configures and enables a frame trigger for the CAN Disturbance Interface and outputs a user-defined sequence. |
| canDisturbanceTriggerEnable | FrameTrigger | FrameSequence | Configures and enables a frame trigger for the CAN Disturbance Interface and outputs a frame as sequence. |
| canDisturbanceTriggerEnable | MultiFrameTrigger | Sequence | Configures and enables up to 32 frame triggers for the CAN Disturbance Interface and outputs a user-defined sequence. |
| canDisturbanceTriggerEnable | MultiFrameTrigger | FrameSequence | Configures and enables up to 32 frame triggers for the CAN Disturbance Interface and outputs a frame as sequence. |
| canDisturbanceTriggerEnable | ExternalTrigger | Sequence | Configures and enables an external trigger for the CAN Disturbance Interface and outputs a user-defined sequence. |
| canDisturbanceTriggerEnable | ExternalTrigger | FrameSequence | Configures and enables an external trigger for the CAN Disturbance Interface and outputs a frame as sequence. |
| canDisturbanceTriggerEnable | ErrorFrame | Sequence | Configures and enables an error frame trigger for the CAN Disturbance Interface and outputs a user-defined sequence. |
| canDisturbanceTriggerEnable | ErrorFrame | FrameSequence | Configures and enables an error frame trigger for the CAN Disturbance Interface and outputs a frame as sequence. |
| canDisturbanceTriggerNow | Configures and outputs a sequence directly on the CAN bus. |  |  |
| canDisturbanceTriggerDisable | Disables a configured trigger. |  |  |

| Methods | Short Description |
|---|---|
| canDisturbanceCombinedFrameTrigger::AddFrameTrigger | Adds a frame trigger to the combined frame trigger. |
| canDisturbanceCombinedFrameTrigger::Clear | Deletes all configured frame triggers. |
| canDisturbanceFrameSequence::RecalculateCRC | Recalculates the CRC value based on the configured sequence. |
| canDisturbanceFrameSequence::SetMessage | Configures the output sequence based on the frame. |
| canDisturbanceFrameTrigger::RecalculateCRC | Recalculates the CRC value if fields of the trigger have been changed. |
| canDisturbanceFrameTrigger::SetMessage | Sets the frame for the trigger condition. |
| canDisturbanceSequence::AppendToSequence | Adds a segment to a sequence. |
| canDisturbanceSequence::Clear | Clears the current sequence. |
| canDisturbanceSequence::ToString | Represents the sequence as FPGA tick based string. |

| Version 15© Vector Informatik GmbH |
|---|
