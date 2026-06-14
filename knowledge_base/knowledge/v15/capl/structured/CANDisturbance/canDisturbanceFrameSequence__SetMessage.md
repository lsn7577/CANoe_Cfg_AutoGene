# canDisturbanceFrameSequence::SetMessage

> Category: `CANDisturbance` | Type: `method`

## Syntax

```c
void canDisturbanceFrameSequence::SetMessage(dword deviceID, message msg); //form 1
void canDisturbanceFrameSequence::SetMessage(dword deviceID, message msg, word arbitrationTicks, word dataTicks); //form 2
```

## Description

Configures the output sequence based on the frame msg.

All CanDisturbanceBitSequence objects in all fields of this frame sequence are overridden by a sequence that corresponds to the bits the frame.

## Parameters

| Name | Description |
|---|---|
| deviceID | The device ID of the CAN Disturbance Interface. |
| msg | The frame data that should be used for the frame sequence. |
| Note If form 1 is used or set to 0, the arbitration ticks are calculated using the channel bit timings of the CAN Disturbance Interface. |  |
| NoteIf form 1 is used or set to 0, the arbitration ticks are calculated using the channel bit timings of the CAN Disturbance Interface. |  |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 10.0 SP3 recommended | — | — | — | 2.2 |
| Restricted To | — | CAN CAN Disturbance Interface | — | — | — | CAN CAN Disturbance Interface |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
