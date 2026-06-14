# coTfsatoxD

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsatoxD( char inValueBuf[], dword valueBufSize );
```

## Description

The function converts a string in a dword value.

The string contains either a decimal value, e.g. "1234" and "-1234" or a hexadecimal value, e.g. "0x4321". The prefix 0x is automatically detected and the function converts the string.

## Parameters

| Name | Description |
|---|---|
| inValueBuf[] | Buffer containing the string. |
| valueBufSize | Buffer size in byte of inValueBuf. |

## Return Values

Converted string as dword value.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
