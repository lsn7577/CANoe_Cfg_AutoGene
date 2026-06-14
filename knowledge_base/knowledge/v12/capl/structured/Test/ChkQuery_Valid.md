# ChkQuery_Valid

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_Valid (dword aCheckId);
check.QueryValid();
```

## Description

Examines whether a check with particular Id is valid.

## Return Values

= 0: Refer the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_Valid(checkId);
```

## Availability

| Since Version |
|---|
