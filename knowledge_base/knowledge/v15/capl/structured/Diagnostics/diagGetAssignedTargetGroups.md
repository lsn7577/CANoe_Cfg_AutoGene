# diagGetAssignedTargetGroups

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetAssignedTargetGroups(DiagRequest request, dword& targetGroupFlagsOut);
long DiagGetAssignedTargetGroups(DiagResponse response, dword& targetGroupFlagsOut);
```

## Description

Returns a bit mask where each bit represents a target group. The diagnostic description defines in which target group the object may be sent, and the bit for this group is set to 1 in the mask returned.

The position of the bit in the mask (0 for least significant bit) can be used to query the qualifier and name of the target group using DiagGetTargetGroupQualifier and DiagGetTargetGroupName.

## Parameters

| Name | Description |
|---|---|
| request | Diagnostic request. |
| response | Diagnostic response. |
| targetGroupFlagsOut | Receives the bit mask for the target groups. |

## Return Values

Error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP4 | 9.0 SP4 | — | — | — | 2.1 SP4 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
