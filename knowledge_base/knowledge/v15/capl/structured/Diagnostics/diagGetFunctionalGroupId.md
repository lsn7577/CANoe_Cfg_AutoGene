# diagGetFunctionalGroupId

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
dword diagGetFunctionalGroupId ()
dword diagGetFunctionalGroupId (char groupQualifier)
```

## Description

Determines the CAN ID on which functional requests are sent by the diagnostic tester.

If the functional group is not specified, the destination set with diagSetTarget is used.

## Parameters

| Name | Description |
|---|---|
| groupQualifier | Functional group's qualifier. |

## Return Values

CAN ID of the requests, or 0xFFFFFFFF if no functional group has been set.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
