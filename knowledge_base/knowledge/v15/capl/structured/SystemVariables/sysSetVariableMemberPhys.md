# sysSetVariableMemberPhys

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableMemberPhys(char namespace[], char variableAndMemberName[], double value); // form 1
long sysSetVariableMemberPhys(SysVarMemberName, double value); // form 2
```

## Description

Sets the physical value of a specific element of a variable of type struct or generic array.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variableAndMemberName | Name of the variable and the element of the struct/array. |
| SysVarName | Name of the fully qualified name of the system variable element, including all name spaces, separated by "::". The name must be preceded by "sysVarMember::". |
| value | Sets the new physical value of the element. |

## Example

```c
sysSetVariableMemberPhys(sysvarMember::XCP::ECU_2::KL2.Curve2[0], 1.2);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 SP4 | 8.0 SP4 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
