# diagGetParameterPath, diagGetRespParameterPath

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterPath( diagResponse object, dword paramNo, char[] buffer, dword bufferSize)
long diagGetParameterPath( diagRequest object, dword paramNo, char[] buffer, dword bufferSize)
long diagGetRespParameterPath( diagRequest object, dword paramNo, char[] buffer, dword bufferSize)
```

## Description

Returns the full qualifier path of the parameter at the given position in the primitive. Only leaf parameters that have a simple value are counted, i.e. structural parameters like container lists are NOT returned.

## Parameters

| Name | Description |
|---|---|
| object | Diagnostics object |
| paramNo | Which leaf parameter in the object, beginning with 0. Structural parameters are NOT counted. |
| buffer | Input/output buffer |
| bufferSize | Buffer size |

## Return Values

Length of path written to buffer, may be truncated.
Error code

## Example

see diagGetObjectPath

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.0 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
