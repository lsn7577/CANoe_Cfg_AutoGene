# ChkCreate_MsgRelOccurrenceViolation, ChkStart_MsgRelOccurrenceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgRelOccurrenceViolation(Message observedMsg, double aMinRelCycleTime, double aMaxRelCycleTime, char[] aCallback);
dword ChkStart_MsgRelOccurrenceViolation(Message observedMsg, double aMin-RelCycleTime, double aMaxRelCycleTime, char[] aCallback);
dword ChkCreate_MsgRelOccurrenceViolation(dword aMessageId, double aMinRelCycleTime, double aMaxRelCycleTime, char[] aCallback)
dword ChkStart_MsgRelOccurrenceViolation(dword aMessageId, double aMinRelCycleTime , double aMaxRelCycleTime, char[] aCllback)
```

## Description

Checks for the occurrence of a periodic message.

The check condition is violated if the time between transmissions of the message is less than aMinRelCycleTime * GenMsgDelayTime or greater than aMaxRelCycleTime * Cycle Time.Cycle time is calculated from GenMsgCycleTime and GenSigCycleTime.Limits that should not be checked must be set to 0. At least one limit must be specified.Can only be started in the "on start" area of CAPL or during the measurement. However, the check may be set up as early as in the "pre start" area.

The numeric functions/constructors with the parameter 'aMessageId' cannot be used for FlexRay. Instead use the numeric constructors with the parameter 'slotID' (that can only be applied to a FlexRay bus).

## Parameters

| Name | Description |
|---|---|
| observedMessage | Must exist in the database. |
| aMinRelCycleTime | 0: Limit is not checked. 0 < x < 1: Limit is checked. |
| aMaxRelCycleTime | 0: Limit is not checked. 1 < x < ∞: Limit is checked. |
| aCallback | This parameter must be specified in simulation nodes; it is optional in test modules. |
| aMessageId | message ID to be observed. The corresponding message shall be defined in the database. |
| slotID | This number designates a specific FlexRay slot. Its value must be between 1 and 2047. |
| cycleOffs | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing" of a FlexRay frame. |
| cycleRep | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing" of a FlexRay frame. |
| channelMask | Identifies the FlexRay channel of the communication controller. A value of 1 will check the frame on channel A, 2 will check it on channel B and 3 on any channel (A/B). |

## Example

```c
// checks the periodic occurrence of the message
checkId = ChkStart_MsgRelOccurrenceViolation (MsgToObserve, 0.9, 1.1);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
