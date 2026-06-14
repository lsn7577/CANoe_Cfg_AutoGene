# coTfsCbGetSettings

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCbGetSettings( dword type, dword nodeId, dword cycleTime[1], dword tolerance[1] );
```

## Description

This function gets the set parameter of an active monitor.

## Parameters

| Name | Description |
|---|---|
| type | 0 - Heartbeat message1 - Sync message2 - Sync PDO message3 - Guarding RTR message for request |
| nodeId | Monitored node-ID for request. |
| cycleTime[] | Set cycle time. |
| tolerance[] | Set tolerance. |

## Return Values

Error code

## Example

```c
const kMonitorTypeHeartbeat   = 0;
const kMonitorTypeSyncMsg    = 1;
const kMonitorTypeSyncPdoMsg   = 2;
const kMonitorTypeGuardingRtrMsg = 3;
dword cycleTime[1];
dword tolerance[1];

/* assume the selected monitor is active */
/* get settings of the active monitor */
if (coTfsCbGetSettings(kMonitorTypeHeartbeat, 112, cycleTime, tolerance) != 1)
{
  ; /* failure, monitor not active?, incorrect nodeId? */
} /* if */
else
{
  write ("tolerance = %d ms, cycleTime = %d ms", tolerance[0], cycleTime[0]);
} /* else */
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
