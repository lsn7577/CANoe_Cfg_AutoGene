# TestSetMsgEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSetMsgEvent (dbMsg aMessage);
long TestSetMsgEvent (dword aMessageId);
long TestSetMsgEvent (char aMessageName[]);
```

## Description

Sends the transferred message directly to the bus if the network is active.

The send model is ignored.

This function influences a simulation node with an assigned CANoe Interaction Layer or CANopen simulation.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be sent. |
| aMessageId | Numeric ID of the message that should be sent. |
| aMessageName | Name of the message that should be sent. Message name can optionally specified by additional qualifiers: MsgName BusName::MsgName TransmitterName::MsgName BusName::TransmitterName::MsgName |

## Example

```c
// send a message event for the disabled message ‘MsgToManipulate’
TestDisableMsg(MsgToManipulate);
TestWaitForTimeout(5000);
TestSetMsgEvent(MsgToManipulate);
TestWaitForTimeout(5000);
TestEnableMsg(MsgToManipulate);
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
