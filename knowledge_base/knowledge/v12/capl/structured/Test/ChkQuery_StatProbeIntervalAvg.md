# ChkQuery_StatProbeIntervalAvg

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_StatProbeIntervalAvg (dword aCheckId)
check.QueryStatProbeIntervalAvg()
```

## Description

Returns the average timely distance between 2 consumed message events.

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
result = ChkQuery_StatProbeIntervalAvg(checkId);
```

## Availability

| Since Version |
|---|
