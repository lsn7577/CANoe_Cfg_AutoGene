# ChkCreate_MsgAbsCycleTimeViolation, ChkStart_MsgAbsCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgAbsCycleTimeViolation (Message aObservedMessage, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkStart_MsgAbsCycleTimeViolation (Message aObservedMessage, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkCreate_MsgAbsCycleTimeViolation (Message aObservedMessage, dword aSourceAddress, dword aDestinationAddress, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkStart_MsgAbsCycleTimeViolation (Message aObservedMessage, dword aSourceAddress, dword aDestinationAddress, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkCreate_MsgAbsCycleTimeViolation (Message aObservedMessage, Node aSendNode, Node aReceiveNode, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkStart_MsgAbsCycleTimeViolation (Message aObservedMessage, Node aSendNode, Node aReceiveNode, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkCreate_MsgAbsCycleTimeViolation (Message aObservedMessage, Node aSendNode, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkStart_MsgAbsCycleTimeViolation (Message aObservedMessage, Node aSendNode, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkCreate_MsgAbsCycleTimeViolation (long MessageId, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
dword ChkStart_MsgAbsCycleTimeViolation (long MessageId, duration aMinCycleTime, duration aMaxCycleTime, char[] aCallback);
```

## Description

Checks the occurrences of cyclic messages.

Event is generated if the time between sends of the message is smaller than aMinCycleTime or larger than aMaxCycleTime.

Not to be checked limits are set to 0; there must be at least on limit specified.

Can be started only in the 'on start' section of CAPL or during measurement.

The numeric constructors with the parameter 'slotID' can only be applied to a FlexRay bus.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aObservedMessage | Must exist in DB |
| aMinCycleTime | 0: Limit is not checked0 < x < aMaxCycleTime: Limit is checked Default unit [ms], if not changed with ChkConfig_SetPrecision. |
| aMaxCycleTime | 0: Limit is not checkedaMinCycleTime < x < ∞: Limit is checked Default unit [ms], if not changed with ChkConfig_SetPrecision. |
| aCallback | In simulation nodes this parameter has to be set. In test modules this parameter is optional. |
| slotID | This number designates a specific FlexRay slot. Its value must be between 1 and 2047. |
| cycleOffs | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing" of a FlexRay frame. |
| cycleRep | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing" of a FlexRay frame. |
| channelMask | Identifies the FlexRay channel of the communication controller. A value of 1 will check the frame on channel A, 2 will check it on channel B and 3 on any channel (A/B). |
| aSourceAddress | Source address of a J1939 parameter group. Possible values: 0 – 253, 255: Observe parameter groups sent from this address.254: Observe parameter groups sent from any address.-1 (or 0xFFFFFFFF): Observe parameter groups sent from the source address which is specified by the parameter group in the database. |
| aDestinationAddress | Destination address of a J1939 parameter group. Possible values: 0 – 253, 255: Observe parameter groups sent to this address254: Observe parameter groups sent to any address-1 (or 0xFFFFFFFF): Observe parameter groups sent to the destination address which is specified by the parameter group in the database. |
| aSendNode | Send node of a J1939 parameter group. |
| aReceiveNode | Receive node of a J1939 parameter group. This parameter is only used for destination specific parameter groups (PDU1 format). |
| MessageId | Message-ID of an A429 Label |

## Example

```c
// checks the cycle time of the message
checkId = ChkStart_MsgAbsCycleTimeViolation (MsgToObserve, 90, 110);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method | 13.0 | — | 14 | 1.0: form 1 1.1 SP2: form 1 |
| Restricted To | — | CAN FlexRay J1939 (since 8.2 SP3) A429 (since 8.5 SP4) | CAN FlexRay J1939 A429 | — | CAN FlexRay | CAN FlexRay J1939 (since 1.1 SP2) |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
