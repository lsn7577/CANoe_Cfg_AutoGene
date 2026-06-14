# diagGetParameterName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterName (diagResponse obj, dword paramNo, char buffer[], dword buffersize)
long diagGetParameterName (diagRequest obj, dword paramNo, char buffer[], dword buffersize)
```

## Description

Writes the qualifier (without parent path) of the diagnostic parameter into the given field. Structural parameters are counted too.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| paramNo | Index of the parameter in the object, beginning with 0. Structural parameter that cannot have a simple value (e.g. a container for a list) are also counted and reported. |
| buffer | Output buffer |
| buffersize | Buffer size |

## Return Values

Number of chars written to buffer or error code.

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
