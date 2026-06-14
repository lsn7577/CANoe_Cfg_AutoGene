# ChkQuery_EventStatusToWrite

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventStatusToWrite (dword aCheckId);
check.QueryEventStatusToWrite();
```

## Description

Uses the output of ChkQuery_EventStatus and writes the result to the Write Window.

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventStatusToWrite(checkId);
```

## Availability

| Since Version |
|---|
