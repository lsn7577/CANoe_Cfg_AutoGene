# a429SetParity

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetParity( a429word myA429word, int parity_value );
```

## Description

This function sets the selector parity of an ARINC word. So you may change the mode of parity generation for every single ARINC word.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Parameters

| Name | Description |
|---|---|
| myA429word | ARINC word |
| parity_value | hardware parity support 0: use channel configuration (default) 1: disable hardware parity support 2: generate odd parity 3: generate even parity |

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
