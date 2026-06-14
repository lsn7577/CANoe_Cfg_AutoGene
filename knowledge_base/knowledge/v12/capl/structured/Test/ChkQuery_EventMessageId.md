# ChkQuery_EventMessageId

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventMessageId (dword aCheckId);
check.QueryEventMessageId();
```

## Description

Returns the ID of the message that has forced the event

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventMessageId(checkId);
Write("result = %d", result);
```

## Availability

| Since Version |
|---|
