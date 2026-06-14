# ChkQuery_EventStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventStatus (dword aCheckId, char aBuffer[], dword aBufferLength);
check.QueryEventStatus (char aBuffer[], dword aBufferLength);
```

## Description

Converts the status into a string that can be printed. Returns the number of characters written (<= length).

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
char eventStatus[256];
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventStatus(checkId, eventStatus, 256);
Write("result = %d", result);
Write("Event Status = %s", eventStatus);
```

## Availability

| Since Version |
|---|
