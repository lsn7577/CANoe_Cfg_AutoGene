# TestEnableCRCCalculation

> Category: `Test` | Type: `function`

## Syntax

```c
long TestEnableCRCCalculation (dbMsg aMessage);
long TestEnableCRCCalculation (dword aMessageId);
long TestEnableCRCCalculation (char aMessageName[]);
```

## Description

Re-enables the calculation of the CRC, after it has been disabled with TestDisableCRCCalculation.

This function influences a simulation node with an assigned CANoe Interaction Layer.

## Parameters

| Name | Description |
|---|---|
| aMessage | Message that should be reset to default behavior. |
| aMessageId | Numeric ID of the message that should be reset to default behavior. |
| aMessageName | Name of the message that should be reset to default behavior. Message name can optionally specified by additional qualifiers: MsgName BusName::MsgName TransmitterName::MsgName BusName::TransmitterName::MsgName |

## Example

```c
// resets the CRC calculation of message ‚MsgToManipulate’ to default behaviour after a break of 2000 ms
TestDisableCRCCalculation(MsgToManipulate);
TestWaitForTimeout(2000);
TestEnableCRCCalculation(MsgToManipulate);
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
