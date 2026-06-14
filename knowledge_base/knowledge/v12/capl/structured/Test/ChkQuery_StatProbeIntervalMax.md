# ChkQuery_StatProbeIntervalMax

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_StatProbeIntervalMax (dword aCheckId);
check.QueryStatProbeIntervalMax();
```

## Description

Returns the maximum timely distance between 2 consumed message events.

Among other things with this function this function the maximum occurred cycle time of a cyclic message can be queried.

## Return Values

< 0: Refers the query error codes
Note
There is a meaningful value available and a positive return value is supplied even if the check has not generated any event.

## Example

```c
double result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_StatProbeIntervalMax(checkId);
```

## Availability

| Since Version |
|---|
