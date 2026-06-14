# coTfsMonitorGetStatistics

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsMonitorGetStatistics( dword nodeId, dword requestType, dword minValue[1], dword maxValue[1], dword averageValue[1], dword passedCounter[1] , dword failedCounter[1]);
```

## Description

This function returns the statistics information that are monitored between coTfsMonitorActivate and coTfsMonitorDeactivate.

## Return Values

Error code
