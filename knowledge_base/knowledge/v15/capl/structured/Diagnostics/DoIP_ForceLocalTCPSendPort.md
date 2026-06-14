# DoIP_ForceLocalTCPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_ForceLocalTCPSendPort(dword forcedPort);
```

## Description

Forces local TCP send port to a specific value. According to ISO13400, the local send port for outgoing TCP connections should be dynamically selected. This function allows forcing the local TCP send port to a specific value, typically to 13400 to indicate DoIP. Note that specifying a well-known or system port (1..1023) might not work on most systems.

## Parameters

| Name | Description |
|---|---|
| forcedPort | 0: use a dynamically assigned value (default)1..65535: send from this local TCP portother: reserved |

## Example

```c
On preStart
{
  // Make sure that tester starts TCP connection from the standard port
  DoIP_ForceLocalTCPSendPort(13400);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
