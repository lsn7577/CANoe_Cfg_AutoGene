# TestResetAllFaultInjections

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetAllFaultInjections (dbNode aNode);
```

## Description

Reset all fault injections setting of a node.

## Parameters

| Name | Description |
|---|---|
| aNode | Node which fault injection settings should be reset. |

## Example

```c
// set some FaultInjections and reset them all
TestDisableMsg(MsgToManipulate1);
TestSetMsgCycleTime(MsgToManipulate2, 200);

TestWaitForTimeout(2000)

TestResetAllFaultInjections(NodeToManipulate);
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
