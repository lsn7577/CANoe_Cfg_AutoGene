# coTfsDeactivateHeartbeatMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateHeartbeatMonitor( dword nodeId );
```

## Description

This function switches off the calling of the heartbeat callbacks if these are switched on.

The callbacks can be switched on with coTfsActivateHeartbeatMonitor.

## Parameters

| Name | Description |
|---|---|
| nodeId | Identifier of the node for which the heartbeat callbacks are to deactivate. |

## Return Values

Error code

## Example

```c
coTfsActivateHeartbeatMonitor(0x1,100.20);
TestWaitForTimeout(2000);
coTfsDeactivateHeartbeatMonitor(0x1);
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
