# ChkCreate_MsgDistViolation, ChkStart_MsgDistViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgDistViolation (Message aReferenceMessage, Message aObservedMessage, duration aMinDistance, duration aMaxDistance, Callback aCallback);
dword ChkStart_MsgDistViolation (Message aReferenceMessage, Message aObservedMessage, duration aMinDistance, duration aMaxDistance, Callback aCallback);
dword ChkCreate_MsgDistViolation (Message aReferenceMessage, char aReferenceBus[], Message aObservedMessage, char aObservedBus[], duration aMinDistance, duration aMaxDistance, Callback aCallback);
dword ChkStart_MsgDistViolation (Message aReferenceMessage, char aReferenceBus[], Message aObservedMessage, char aObservedBus[], duration aMinDistance, duration aMaxDistance, Callback aCallback);
```

## Description

Event is generated if the time interval that starts on receipt of the reference message and ends with the receipt of the observed message is smaller than aMinDistance or is larger than aMaxDistance.

The numeric constructors with the parameter 'slotID1/2' can only be applied to a FlexRay bus.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aReferenceMessage | Must exist in DB |
| aObservedMessage | Must exist in DB |
| aMinDistance | Default unit [ms], if not changed with ChkConfig_SetPrecision.aMinDistance < aMaxDistance |
| aMaxDistance | Default unit [ms], if not changed with ChkConfig_SetPrecision.aMinDistance < aMaxDistance |
| aCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional |
| aReferenceBus | Name of the bus on that should be received the reference message |
| aObservedBus | Name of the bus that should receive the observed message |
| slotID1/2 | This number designates a specific FlexRay slot. Its value must be between 1 and 2047. |
| cycleOffs1/2 | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing" of a FlexRay frame. |
| cycleRep1/2 | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing" of a FlexRay frame. |
| channelMask1/2 | Identifies the FlexRay channel of the communication controller. A value of 1 will check the frame on channel A, 2 will check it on channel B and 3 on any channel (A/B). |

## Example

```c
// checks the distance between two messages
checkId = ChkStart_MsgDistViolation (ReferenceMsg, MsgToObserve, 90, 110);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
