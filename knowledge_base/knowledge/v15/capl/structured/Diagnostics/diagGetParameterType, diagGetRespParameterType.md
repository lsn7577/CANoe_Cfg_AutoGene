# diagGetParameterType, diagGetRespParameterType

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterType(diagResponse object, char[] qualifier, char[] buffer, DWORD bufferSize)
long diagGetParameterType(diagRequest object, char[] qualifier, char[] buffer, DWORD bufferSize)
long diagGetRespParameterType(diagRequest object, char[] qualifier, char[] buffer, DWORD bufferSize)
```

## Description

Retrieve the qualifier of the parameter's type.

## Parameters

| Name | Description |
|---|---|
| object | Diagnostics object |
| qualifier | Parameter qualifier |
| buffer | Input/output buffer |
| bufferSize | Buffer size |

## Return Values

Length of qualifier written to buffer, may be truncated.
Error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 6.1 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
