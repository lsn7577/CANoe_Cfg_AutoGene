# diagSetParameterRaw, diagGetParameterRaw

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetParameterRaw (diagResponse obj, char parameter[], byte* buffer, DWORD buffersize); // form 1
long diagSetParameterRaw (diagRequest obj, char parameterName[], byte* buffer, DWORD buffersize); // form 2
long diagGetParameterRaw (diagResponse obj, char parameterName[], byte* buffer, DWORD buffersize); // form 3
long diagGetParameterRaw (diagRequest obj, char parameterName[], byte* buffer, DWORD buffersize); // form 4
```

## Description

Sets or specifies the value of a (complex) parameter directly via uncoded data bytes.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| parameterName | Parameter qualifier |
| buffer | Input/output buffer |
| buffersize | Buffer size |

## Example

See diagGenerateKeyFromSeed

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2: form 1, 2 9.0: form 3, 4 | 5.0: form 1, 2 7.0 SP5: methods form 1, 2 9.0: form 3, 4 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
