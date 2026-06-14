# a429CalcBitLength

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429CalcBitLength( long channel, dword BitTimes );
```

## Description

For every channel there is a relation between a bit time and the length of a bit time. This relation is determined by the channel bit rate. In order to make it easier to provide the gap length a429SetGap in bit times this function converts these values for a given channel.

## Parameters

| Name | Description |
|---|---|
| channel | valid Tx channel |
| BitTimes | 1..1048576 (0x1..0x10000; 0,125..131072 bit times; in steps of 1/8 bit) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
