# frSetSendFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetSendFrame( <frame name>, dword flags ); // form 1
void frSetSendFrame( int slotId, int channelMask, int len, int cycleStart, int cycleRepetition, dword flags, int channel ); // form 2
void frSetSendFrame( <frame object> ); // form 3
```

## Description

Configures the hardware for sending the specified message.

The call must take place in the On preStart routine in the Simulation Setup / transmission branch.

## Parameters

| Name | Description |
|---|---|
| <frame name> | String that corresponds to a frame name of the database.The necessary parameters slotId, channelMask, len, cycleStart and cycleRepetition are taken from the corresponding frame definition of the database. |
| slotId | Identifier of the time slot in which the message should be sent. |
| 1 | Channel A |
| 2 | Channel B |
| 3 | Channel A+B |
| len | Number of databytes (maximum 254 bytes). |
| cycleStart | This number designates the base cycle. This value must be smaller than the repetition factor and lie in the range between 0 and 63.This value together with the repetition factor determines the "Cycle Multiplexing" of the frame. The slot ID and the cycle multiplexing (and the cluster allocation of the FlexRay bus) uniquely identify the message in a FIBEX database. |
| cycleRepetition | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64).This value, together with the base cycle, determines the "Cycle Multiplexing" of the frame. The slot ID and the cycle multiplexing (and the cluster allocation of the FlexRay bus) uniquely identify the message in a FIBEX database. |
| Bit Mask | Meaning |
| Caution! This flag is deprecated (for CANoe ≥ 7.2)! Use instead function FRSetKeySlot. |  |
| Caution! This flag is deprecated (for CANoe ≥ 7.2)! Use instead function FRSetKeySlot. |  |
| 0x10 | Sets the send mode to event-triggered. If not set, the frame will be transmitted in time-triggered mode. |
| 0x20 | Sets the payload preamble bit. With static frames, the initial data bytes then contain the local NM vector; with dynamic frames, the first two bytes then designate the expanded message ID. |
| Caution! This flag is deprecated (for CANoe ≥ 7.2)! Use instead function FRSetKeySlot. |  |
| channel | Channel number (or cluster number) |

## Return Values

—

## Example

For an example see functions frUpdateStatFrame and frSendFrame.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
