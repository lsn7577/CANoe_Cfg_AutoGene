# coTfsCbGetSettings

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCbGetSettings( dword type, dword nodeId, dword cycleTime[1], dword tolerance[1] );
```

## Description

This function gets the set parameter of an active monitor.

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
