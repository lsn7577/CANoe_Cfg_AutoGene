# diagGetComplexParameterRaw, diagSetComplexParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetComplexParameterRaw (diagResponse obj, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword buffersize)
long diagGetComplexParameterRaw (diagRequest obj, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword buffersize)
long diagSetComplexParameterRaw (diagResponse obj, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword buffersize)
long diagSetComplexParameterRaw (diagRequest obj, char parameterName[], dword iteration, char subParameter[], byte buffer[], dword buffersize)
```

## Description

Reads/sets the complex parameter to the specified raw value.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| parameterName | Parameter qualifier |
| iteration | Iteration (beginning with 0) |
| subParameter | Sub parameter qualifier |
| buffer | Output buffer |
| buffersize | Buffer size |

## Return Values

Number of bytes copied into the buffer or error code.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 5.0 | — | — | — | 1.0 |
| Restricted To | Online mode Not for basic diagnostics | Online mode Not for basic diagnostics | — | — | — | Online mode Not for basic diagnostics |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
