# SCC_SetMessageDelay

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetMessageDelay ( dword Delay ) // form 1
void SCC_SetMessageDelay ( dword Delay, float JitterPercent ) // form 2
```

## Description

Specifies the delay time before an SCC message is sent. This allows you to slow down the protocol sequence. The delay applies to all active connections of the module.

## Parameters

| Name | Description |
|---|---|
| Delay | Desired delay value in milliseconds. |
| JitterPercent | Desired jitter (max. random variation) in % of Delay. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1, 2 | — | — | — | 3.0 SP3: form 1, 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
