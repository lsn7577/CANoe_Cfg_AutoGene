# ChkQuery_EventSignalValue (for signals with positive values)

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_EventSignalValue (dword checkId);
check.QueryEventSignalValue();
```

## Description

This function enables access to the signal value which was last reported by a check as invalid.

This function enables access only to positive signal values.

## Return Values

< 0: Refers the query error codes in this chapter

## Example

```c
double result;
dword checkId;
checkId = ChkStart_MsgSignalValueInvalid(Velocity, 80, 100);
// ... execute test sequence
result = ChkQuery_EventSignalValue(checkId);
```

## Availability

| Since Version |
|---|
