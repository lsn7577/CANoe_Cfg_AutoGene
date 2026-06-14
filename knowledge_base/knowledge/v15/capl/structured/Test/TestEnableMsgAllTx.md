# TestEnableMsgAllTx

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableMsgAllTx (char [] aNode);
```

## Description

Re-enables the sending of all tx messages of the node after having disabled it with TestDisableMsgAllTx.

This function influences a simulation node with an assigned CANoe Interaction Layer or CANopen simulation.

## Parameters

| Name | Description |
|---|---|
| aNode | Node, the tx messages should be enabled. |

## Example

```c
// send a message event for a message which is disabled by TestDisableMsgAllTx
// and re-enable the sending of all tx messages of node ‚NodeToManipulate’
TestDisableMsgAllTx(NodeToManipulate);
TestWaitForTimeout(5000);
TestSetMsgEvent(MsgToManipulate);
TestWaitForTimeout(5000);
TestEnableMsgAllTx(NodeToManipulate);
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
