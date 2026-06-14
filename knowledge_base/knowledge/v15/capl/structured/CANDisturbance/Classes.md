# Classes

> Category: `CANDisturbance` | Type: `notes`

## Description

With this class it is possible to define a user-defined sequence within a frame sequence. A typical use case is to insert a glitch within a bit near the sample point or to lengthen or shorten a bit. 8 transitions of levels are possible within a bit. The segment with the array index 0 is sent first on the bus.

Classes in CAPL

| Classes | Short Description |
|---|---|
| CanDisturbanceFrameTrigger | A configurable frame trigger for a CAN/CAN FD frame.Every field of a CAN/CAN FD frame is configurable. The position of the frame trigger is configurable. |
| CanDisturbanceCombinedFrameTrigger | Combination of up to 32 frame triggers.The position of the trigger can be configured once for all frame triggers. |
| CanDisturbanceExternalTrigger | Configuration options for external trigger inputs. |
| CanDisturbanceErrorFrameTrigger | A configurable trigger condition for CAN/CAN FD error frames. |

| Classes | Short Description |
|---|---|
| CanDisturbanceSequence | A user-defined sequence is sent directly on the bus or can be used in combination with a trigger. |
| CanDisturbanceBitSequence | A sequence describes a bit sequence within a CanDisturbanceFrameSequenceField. With this class it is possible to define a user-defined sequence within a frame sequence. A typical use case is to insert a glitch within a bit near the sample point or to lengthen or shorten a bit. 8 transitions of levels are possible within a bit. The segment with the array index 0 is sent first on the bus. |
| CanDisturbanceFrameSequenceField | Contains the bits for a field of a CAN/CAN FD frame. A field can contain one or several bits. |
| CanDisturbanceFrameSequence | Represents a CAN/CAN FD frame as sequence. Contains all fields of a CAN/CAN FD frame. |

| Classes | Short Description |
|---|---|
| CanDisturbanceTriggerRepetitions | Can be used to configure repetitions and cycles for a frame trigger in combination with a sequence or only a sequence. |

| Version 15© Vector Informatik GmbH |
|---|
