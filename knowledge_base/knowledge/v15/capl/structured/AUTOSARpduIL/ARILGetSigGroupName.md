# ARILGetSigGroupName

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILGetSigGroupName (char aMsgName[], dword index, char sigGroupName[], long maxSigGroupNameLen);
```

## Description

Retrieves the name of the nth signal group of the PDU.

## Parameters

| Name | Description |
|---|---|
| aMsgName | The symbolic name of a PDU in the database. |
| index | Number of the signal group (starting from 0). |
| sigGroupName | Returns the full name of the designated signal group. |
| maxSigGroupNameSize | Size of the buffer for the name of the signal group. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet FlexRay | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
