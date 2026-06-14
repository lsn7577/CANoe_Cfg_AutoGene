# AfdxGetSignalString

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetSignalString( long packet, char signalName[], long bufSize, char buffer[] ); // form 1
long AfdxGetSignalString( long packet, long offset, long bufSize, char buffer[] ); // form 2
```

## Description

This function copies up to bufSize characters of an AFDX string to the specified buffer. The AFDX string structure consists of a 16-bit length code n and a sequence of n ASCII characters.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message. |
| signalName | Name of the signal. Note: The signal and the message need to be defined in the assigned DBC file. |
| offset | The offset value points to the starting byte of the AFDX string. |
| bufSize | Size of available buffer area. |
| buffer | Buffer containing the read string value. |

## Return Values

number of copied data bytes.
If this value is > bufSize an error occurred.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP3 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
