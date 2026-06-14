# KLine_SetP3max

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP3max(dword P3max_us)
```

## Description

Sets the maximum time between the end of the server (ECU) response and start of a new client (tester) request. If no request is sent in this interval, the ECU can assume that the tester is no longer present.

## Parameters

| Name | Description |
|---|---|
| P3max_us | P3max in usValue range: 0 – 10000000 (10 s). |

## Example

```c
on start
{
   KLine_SetP3Max(3000000); // P3max == 3 s
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 | — | — | — | 2.0 SP2 |
| Restricted To | — | K-Line Real bus mode Online mode ECU simulation | — | — | — | K-Line Real bus mode Online mode ECU simualtion |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
