# diagSetComplexParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetComplexParameter (diagResponse obj, char parameterName[], DWORD iteration, char subParameter[], double numValue)
long diagSetComplexParameter (diagRequest obj, char parameterName[], DWORD iteration, char subParameter[], double numValue)
long diagSetComplexParameter (diagResponse obj, char parameterName[], DWORD iteration, char subParameter[], char symbValue[])
long diagSetComplexParameter (diagRequest obj, char parameterName[], DWORD iteration, char subParameter[], char symbValue[])
long diagSetComplexParameter (diagResponse obj, long mode, char parameterName[], DWORD iteration, char subParameter[], char valueIn[])
long diagSetComplexParameter (diagRequest obj, long mode, char parameterName[], DWORD iteration, char subParameter[], char valueIn[])
```

## Description

Sets one of the sub-parameters within a complex parameter to the specified (numeric or symbolic) value.

For this first the complex parameter, that is, the name of the iteration, must be specified; then the number of repetitions of the sub-parameter list that is the goal, and then the sub-parameter in the iteration itself.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| parameterName | Complex parameter |
| iteration | Number of the iteration (beginning with 0) |
| subParameter | Sub parameter |
| numValue | New numeric value (only possible with numeric parameters) |
| symbValue | Symbolic value (possible with all parameters) |
| valueIn | Depending on the mode the value is numerical or symbolical. |
| mode | Access mode |

## Return Values

Error code.

## Example

See on diagRequest

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 5.0 7.0 SP3: methods | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
