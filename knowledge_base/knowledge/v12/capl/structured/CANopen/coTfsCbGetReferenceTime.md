# coTfsCbGetReferenceTime

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCbGetReferenceTime( dword type, dword nodeId, dword refTime[1], dword minTime[1], dword minOccTime[1], dword maxTime[1], dword maxOccTime[1], dword averageTime[1] );
```

## Description

This function gets the maximum, minimum, and average value of an active monitor.

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
