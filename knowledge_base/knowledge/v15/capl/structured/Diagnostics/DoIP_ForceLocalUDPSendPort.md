# DoIP_ForceLocalUDPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_ForceLocalUDPSendPort(dword forcedPort);
```

## Description

According to ISO 13400, the local send port for UDP messages should be dynamically selected. This function allows forcing the local UDP send port to a specific value, typically to 13400 to indicate DoIP.

Note that specifying a "well-known" or system port (1..1023) might not work on most systems.

## Parameters

| Name | Description |
|---|---|
| forcedPort | 0: use a dynamically assigned value (default) 1..65535: bind to this local UDP port other: reserved. |

## Return Values

Error code

## Example

```c
On preStart
{
  // Make sure that in an ECU simulation all UDP packets are sent from the standard port
  DoIP_ForceLocalUDPSendPort(13400);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP3 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
