# ChkQuery_EventStatusToLog

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventStatusToLog (dword aCheckId);
check.QueryEventStatusToLog();
```

## Description

Uses the output of ChkQuery_EventStatus and writes the result to the logging file.

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventStatusToLog(checkId);
```

## Availability

| Since Version |
|---|
