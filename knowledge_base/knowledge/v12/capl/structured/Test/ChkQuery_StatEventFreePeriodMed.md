# ChkQuery_StatEventFreePeriodMed

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_StatEventFreePeriodMed (dword aCheckId);
check.QueryStatEventFreePeriodMed();
```

## Description

Returns the average timely distance between events and check starts/stops.

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
result = ChkQuery_StatEventFreePeriodMed(checkId);
```

## Availability

| Since Version |
|---|
