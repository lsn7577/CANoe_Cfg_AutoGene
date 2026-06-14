# coTfsActivateHeartbeatMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsActivateHeartbeatMonitor( dword nodeID, dword producerTime, dword tolerance );
```

## Description

This function checks whether the DUT Device Under Test as heartbeat producer makes the heartbeat message available within the defined times.

For each correct occurrence, the callback void coTfsOnHeartbeatMsg (dword nodeId) is called. If the time is not adhered to, then the callback void coTfsOnHeartbeatFail(dword nodeId, dword cause) is called. After an error has occurred, the callback system is automatically disabled. The reason for the error is specified in the parameter cause:1 = Message distance too small2 = Message distance too large or message is missing

Only one DUT can be monitored at a time. This check can be switched off again with coTfsDeactivateHeartbeatMonitor.

## Parameters

| Name | Description |
|---|---|
| nodeID | Node-ID of the DUT. |
| producerTime | Heartbeat time in us. |
| tolerance | Permitted time deviation of the target device in us. It is recommended that you use an even value. The tolerated time frame within which a message is still accepted is: x - (delta/2) <= x <= x + (delta/2) |

## Return Values

Error code

## Example

Demonstration of the mode of operation of coTfsActivateHeartbeatMonitor and the corresponding callback functions

```c
coTfsActivateHeartbeatMonitor (0x1, 100, 20);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
