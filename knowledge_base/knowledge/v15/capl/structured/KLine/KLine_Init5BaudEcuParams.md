# KLine_Init5BaudEcuParams

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_Init5BaudEcuParams(dword 5BaudAddress, dword rate_10thBd, dword W1_us, dword W2_us, dword W3_us, dword W4_us, dword W4Min_us, dword W4Max_us, dword addressNot);
```

## Description

Initialize K-Line channel for reception of the 5 baud pattern.

## Parameters

| Name | Description |
|---|---|
| 5BaudAddress | The 5 Baud address to accept on the active channel. |
| rate_10thBd | Rate of the address in 1/10 of baud, i.e. a value of 50 should be used here. |
| W1_us W2_us W3_us W4_us W4Min_us W4Max_us | Timing parameters in milliseconds used for the initialization pattern. A detailed description of the parameters is available on the Vector K-Line Protocol Reference Chart e.g. available at vector.com. |
| addressNot | The inverted address to be sent by the ECU simulation. A value of 0 will use the default, i.e. the inverted 5 baud address. |

## Return Values

On success 0, otherwise a value less than 0.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
