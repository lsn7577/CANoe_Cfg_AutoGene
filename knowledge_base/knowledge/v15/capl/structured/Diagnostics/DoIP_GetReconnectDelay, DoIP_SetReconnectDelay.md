# DoIP_GetReconnectDelay, DoIP_SetReconnectDelay

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetReconnectDelay(dword reconnectDelay_ms);
dword DoIP_GetReconnectDelay();
```

## Description

Sets or returns the delay started by the tester when the ECU closes the TCP connection. After the configured time the tester attempts at first to re-open the TCP connection and afterwards to re-establish the routing activation.

## Parameters

| Name | Description |
|---|---|
| reconnectDelay_ms | Delay in milliseconds between TCP connection close and attempt to reactivate it. A value of 0 will deactivate this feature, i.e. the tester does not try to reactivate the route. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2 | — | — | — | 1.1 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
