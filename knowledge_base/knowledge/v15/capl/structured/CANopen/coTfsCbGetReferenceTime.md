# coTfsCbGetReferenceTime

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCbGetReferenceTime( dword type, dword nodeId, dword refTime[1], dword minTime[1], dword minOccTime[1], dword maxTime[1], dword maxOccTime[1], dword averageTime[1] );
```

## Description

This function gets the maximum, minimum, and average value of an active monitor.

## Parameters

| Name | Description |
|---|---|
| type | 0 - Heartbeat message1 - Sync message2 - Sync PDO message3 - Guarding RTR message for request |
| nodeId | Monitored node-ID for request. |
| refTime[] | Reference time of the last executed callback [ms]. |
| minOccTime[] | Minimum time stamp of occurrence [ms]. |
| maxTime[] | Maximum time difference [ms]. |
| maxOccTime[] | Maximum time stamp of occurrence [ms]. |
| averageTime[] | Average time of all callbacks. |

## Return Values

Error code

## Example

```c
const kMonitorTypeHeartbeat   = 0;
const kMonitorTypeSyncMsg    = 1;
const kMonitorTypeSyncPdoMsg   = 2;
const kMonitorTypeGuardingRtrMsg = 3;
dword refTime[1];
dword minTime[1];
dword minOccTime[1];
dword maxTime[1];
dword maxOccTime[1];
dword averageTime[1];

/* assume the selected monitor is active */
/* get reference time of the active monitor */
if (coTfsCbGetReferenceTime(kMonitorTypeHeartbeat, 112, refTime, minTime, minOccTime, maxTime, maxOccTime, averageTime) != 1)
{
  ; /* failure, monitor not active?, incorrect nodeId? */
} /* if */
else
{
  write ("last message monitored = %d ms, average time = %d ms", refTime[0], averageTime[0]);
  write ("minimum time = %d ms, time stamp of that event = %d ms", minTime[0], minOccTime[0]);
  write ("maximum time = %d ms, time stamp of that event = %d ms", maxTime[0], maxOccTime[0]);
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
