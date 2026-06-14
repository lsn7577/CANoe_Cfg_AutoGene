# ChkQuery_EventTimeStamp

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventTimestamp (dword CheckId);
check.QueryEventTimestamp();
```

## Description

Retrieves time stamp of last fired event.

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventTimeStamp(checkId);
```

## Availability

| Since Version |
|---|
