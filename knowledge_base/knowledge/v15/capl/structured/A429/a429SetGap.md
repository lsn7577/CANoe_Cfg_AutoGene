# a429SetGap

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetGap( a429word myA429word, dword gapValue );
```

## Description

This function sets the selector gap of an ARINC word. The value is given in nanoseconds. You have to consider the bit rate on the corresponding channel. If the bit rate is high speed a value of 40000 (40 µs) specifies the standard gap of 4 bit times (as defined in /1/). For low speed at 12500 kBit/s a value of 320000 (320 µs) is needed.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Parameters

| Name | Description |
|---|---|
| myA429word | ARINC word |
| gapValue | gap in nanoseconds; value range [0; 1/8 bit time..1 second]; the value 0 forces the use of the channel default value |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
