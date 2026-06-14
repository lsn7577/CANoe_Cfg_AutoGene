# diagSetPrimitiveByte

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetPrimitiveByte( diagRequest request, DWORD bytePos, DWORD newValue);
long diagSetPrimitiveByte( diagResponse response, DWORD bytePos, DWORD newValue);
```

## Description

Writes one byte of a diagnostic object.

## Parameters

| Name | Description |
|---|---|
| request | Request |
| response | Response |
| bytePos | Position of the byte in the object |
| newValue | New value of the accessed byte |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 6.0 7.0 SP3: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
