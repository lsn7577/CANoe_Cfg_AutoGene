# KLine_SetP1ECU

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP1ECU(dword P1_us)
```

## Description

Sets the interbyte time of a response.

## Parameters

| Name | Description |
|---|---|
| P1_us | P1 in usValue range: 0 – 650000. |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on start
{
   KLine_SetP1ECU(10000); // P1 == 10 ms
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simualtion |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
