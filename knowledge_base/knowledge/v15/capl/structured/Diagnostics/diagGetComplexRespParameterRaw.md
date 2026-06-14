# diagGetComplexRespParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexRespParameterRaw (diagRequest req, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword bufferLen);
```

## Description

Reads/sets the complex parameter to the specified raw value.

This function offers access to parameters contained in a received response object, whereby the function is addressed directly by the request. This eliminates the need to generate a separate response object. If no response is available yet for the request, an error is reported.

## Parameters

| Name | Description |
|---|---|
| req | Request |
| parameterName | Parameter qualifier |
| iteration | Iteration (beginning with 0) |
| subParameter | Sub parameter qualifier |
| buffer | Output buffer |
| bufferLen | Buffer size |

## Return Values

Error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 5.1 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
