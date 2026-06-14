# KLine_SetP2max

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetP2max(dword P2max_us)
```

## Description

Sets the maximum time between the client (tester) request and the server (ECU) response, or between 2 server (ECU) responses.

## Parameters

| Name | Description |
|---|---|
| P2max_us | P2max in usValue range: 0 – 100000000 (100 s). |

## Example

```c
on start
{
   KLine_SetP2Max(10000000); // P2max == 10 s
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
