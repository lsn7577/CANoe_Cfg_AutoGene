# ChkCreate_MsgOccurrenceCount, ChkStart_MsgOccurrenceCount

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MsgOccurrenceCount(dbMsg aMessage, long aMaxCount);
dword ChkStart_MsgOccurrenceCount(dbMsg aMessage, long aMaxCount);
dword ChkCreate_MsgOccurrenceCount(dword aMessageId, long aMaxCount);
dword ChkStart_MsgOccurrenceCount(dword aMessageId, long aMaxCount);
dword ChkCreate_MsgOccurrenceCount(dword aSourceAdr, dword aDestAdr, char[] aSymbolicMsg, dword aInstanceId, long aMaxCount)
dword ChkStart_MsgOccurrenceCount(dword aSourceAdr, dword aDestAdr, char[] aSymbolicMsg, dword aInstanceId, long aMaxCount)
```

## Description

Checks the absence of the specified message on the bus. An event is created if more than aMaxCount of the specified message were sent.

The numeric functions/constructors with the parameter 'aMessageId/aSourceAdr' cannot be used for FlexRay. Instead use the numeric constructors with the parameter 'slotID' (that can only be applied to a FlexRay bus).

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| aMessage | The message whose occurrence is to be monitored in symbolic form, e.g.: "EngineData". |
| aMessageId | The ID of the message whose occurrence is to be monitored. |
| aMaxCount | The maximum number of message that may be sent without the check to fail. |
| aSourceAdr | The source address of the message whose occurrence is to be monitored. |
| aDestAdr | The destination address of the message whose occurrence is to be monitored. |
| aSymbolicMsg | Symbolic message definition of the message which has to be monitored in the format "FBlock.Function.OpType". Widcards can also be used (e.g. "AudioDiskPlayer.*.Status"). |
| aInstanceId | The instance ID of the message whose occurrence is to be monitored. |
| slotID | This number designates a specific FlexRay slot. Its value must be between 1 and 2047. |
| cycleOffs | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing" of a FlexRay frame. |
| cycleRep | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing" of a FlexRay frame. |
| channelMask | Identifies the FlexRay channel of the communication controller. A value of 1 will check the frame on channel A, 2 will check it on channel B and 3 on any channel (A/B). |
| aNode | The node from the DB whose Tx messages should be observed. |
| aCaplCallbackFunction | This parameter must be specified in simulation nodes; it is optional in test modules. |

## Example

```c
// checks that the message is sent less than 3 times
checkId = ChkStart_MsgOccurrenceCount (MsgToObserve, 2);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN MOST FlexRay ARINC429 (since 10.0 SP3) | CAN MOST FlexRay ARINC429 | — | CAN MOST FlexRay ARINC429 | CAN MOST FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
