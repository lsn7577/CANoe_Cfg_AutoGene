# ChkQuery_EventInterval

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventInterval (dword checkId);
check.QueryEventInterval();
```

## Description

Returns the last time-interval that has led to the event.

## Return Values

-101: The interval for the last event has been started but not yet terminated.

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventInterval(checkId);
Write("result = %d", result);
```

## Availability

| Since Version |
|---|
