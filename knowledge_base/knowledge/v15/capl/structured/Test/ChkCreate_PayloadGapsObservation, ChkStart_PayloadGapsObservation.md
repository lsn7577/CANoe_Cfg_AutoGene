# ChkCreate_PayloadGapsObservation, ChkStart_PayloadGapsObservation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_PayloadGapsObservation(Message aMessage, long defaultBitValue, char [] aCallback);
dword ChkStart_PayloadGapsObservation(Message aMessage, long defaultBitValue, char [] aCallback);
dword ChkCreate_PayloadGapsObservation(dword aMessageId, long defaultBitValue, char [] aCallback);
dword ChkStart_PayloadGapsObservation(dword aMessageId, long defaultBitValue, char [] aCallback);
dword ChkCreate_PayloadGapsObservation(dword slotID, dword cycleOffs, dword cycleRep, dword channelMask, long defaultBitValue, char [] aCallback);
dword ChkStart_PayloadGapsObservation(dword slotID, dword cycleOffs, dword cycleRep, dword channelMask, long defaultBitValue, char [] aCallback);
```

## Description

Checks the payload gaps and the DLC of a message.

The check condition is violated if the payload gaps do not match the specified default bit value or the DLC does not match the specified DLC of the database.

The numeric functions/constructors with the parameter aMessageId cannot be used for FlexRay. Instead use the numeric constructors with the parameter slotID (that can only be applied to a FlexRay bus).

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous Frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aMessage | Must exist in the database. |
| defaultBitValue | Default bit value the payload gaps must have. |
| aCallback | This parameter must be specified in simulation nodes; it is optional in test modules. |
| aMessageId | Message ID to be observed. The corresponding message shall be defined in the database. |
| slotID | This number designates a specific FlexRay slot. Its value must be between 1 and 2047. |
| cycleOffs | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing" of a FlexRay frame. |
| cycleRep | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing" of a FlexRay frame. |
| channelMask | Identifies the FlexRay channel of the communication controller. A value of 1 will check the frame on channel A, 2 will check it on channel B and 3 on any channel (A/B). |

## Example

```c
// checks the payload gaps of the message
checkId = ChkStart_PayloadGapsObservation(MsgToObserve, 0);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | 14 | 2.1 |
| Restricted To | — | CAN LIN FlexRay | CAN LIN FlexRay | — | CAN LIN FlexRay | CAN LIN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
