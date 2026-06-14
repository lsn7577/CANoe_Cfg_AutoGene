# ChkQuery_EventMessageName

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_EventMessageName (dword aCheckId, char buffer[], dword bufferlen);
check.QueryEventMessageName (char buffer[], dword bufferlen);
```

## Description

Stores the name of the message, that has led to the event, in the buffer and returns the length of the name, or 0 if specified for a range.

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
char messageName[100];
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_EventMessageName(checkId, messageName, 100);
Write("result = %d", result);
```

## Availability

| Since Version |
|---|
