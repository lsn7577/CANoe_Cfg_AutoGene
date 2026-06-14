# diagGetTargetGroupQualifier

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetTargetGroupQualifier(char ecuQualifier[], dword bitPos, char groupQualOut[]);
long DiagGetTargetGroupQualifier(dword bitPos, char groupQualOut[]);
```

## Description

Returns the qualifier of the diagnostic target group for which the bit at the given position is used by diagGetAssignedTargetGroups. If the target ECU is not specified explicitly, the target selected with diagSetTarget is used.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Use this diagnostic target, not that selected with DiagSetTarget. |
| bitPos | Position of the bit in the bit mask returned by DiagGetAssignedTargetGroups. |
| groupQualOut | The qualifier of the target group is written to this field, ASCII characters only. |

## Example

See diagGetAssignedTargetGroups

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
