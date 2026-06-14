# TestResetMsgDlc

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetMsgDlc (dbMsg aMessage);
long TestResetMsgDlc (dword aMessageId);
long TestResetMsgDlc (char aMessageName[]);
```

## Description

Resets the DLC to the DLC of the database.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message symbol. |
| aMessageId | Numeric ID of the message. |
| aMessageName | Name of the message symbol. Message name can optionally specified by additional qualifiers: MsgName BusName::MsgName TransmitterName::MsgName BusName::TransmitterName::MsgName |

## Example

```c
// reset the DLC of message ‘MsgToManipulate’
TestSetMsgDLC(MsgToManipulate, 4);
TestWaitForTimeout(2000);
TestResetMsgDLC(MsgToManipulate);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP4 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
