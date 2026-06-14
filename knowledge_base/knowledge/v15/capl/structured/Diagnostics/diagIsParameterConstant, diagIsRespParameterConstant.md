# diagIsParameterConstant, diagIsRespParameterConstant

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsParameterConstant(diagResponse object, char[] qualifier)
long diagIsParameterConstant(diagRequest object, char[] qualifier)
long diagIsRespParameterConstant(diagRequest object, char[] qualifier)
```

## Description

Returns 1 if the parameter is declared constant in the diagnostic description.

## Parameters

| Name | Description |
|---|---|
| object | Diagnostics object |
| qualifier | Parameter qualifier |

## Return Values

1 for true or error code.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
