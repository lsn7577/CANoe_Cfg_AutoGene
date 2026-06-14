# diagGetParameterCoded, diagSetParameterCoded

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetParameterCoded(diagResponse obj, char parameterName[], byte* buffer, dword bufferSize)
long diagGetParameterCoded(diagRequest obj, char parameterName[], byte* buffer, dword bufferSize)
long diagSetParameterCoded(diagResponse obj, char parameterName[], byte* buffer, dword bufferSize)
long diagSetParameterCoded(diagRequest obj, char parameterName[], byte* buffer, dword bufferSize)
```

## Description

Sets or specifies the value of a parameter directly via coded data bytes.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |
| parameterName | Parameter qualifier (NOT the language-dependent name of the parameter!) |
| buffer | Input buffer |
| bufferSize | Buffer size |

## Return Values

0 if bytes were copied, otherwise <0 for an error code.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP4 | 8.2 SP4 | — | — | — | 2.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
