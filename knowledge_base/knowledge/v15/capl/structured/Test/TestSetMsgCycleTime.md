# TestSetMsgCycleTime

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSetMsgCycleTime(dbMsg aMessage, float aNewCycleTime);
long TestSetMsgCycleTime(dword aMessageId, float aNewCycleTime);
long TestSetMsgCycleTime(char aMessageName[]);
```

## Description

Assigns a new cycle time to the message.

This function influences a simulation node with an assigned CANoe Interaction Layer or CANopen simulation.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should get a new cycle time. |
| aMessageId | Numeric ID of the message that should get a new cycle time. |
| aNewCycleTime | The new cycle time (in milliseconds) that should be assigned to the message. |
| aMessageName | Name of the message that should get a new cycle time. Message name can optionally specified by additional qualifiers: MsgName BusName::MsgName TransmitterName::MsgName BusName::TransmitterName::MsgName |

## Example

```c
// set the cycle time of message ‘MsgToManipulate’ to a specified value for 2000 ms
TestSetMsgCycleTime(MsgToManipulate, 200);
TestWaitForTimeout(2000);
TestResetMsgCycleTime(MsgToManipulate);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
