# ChkQuery_StatNumProbes

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_StatNumProbes (dword aCheckId);
check.QueryStatNumProbes();
```

## Description

Returns the number of samples (probes) that have been considered by the check. In general this is the count of messages that have been analyzed by the check. In almost all signal/envvar/sysvar orientated checks, it is the number of changes in value of the specific signal or variable.

Deviating from the default following checks return the number of value updates:

## Return Values

< 0: Refers the query error codes

## Example

```c
long result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_StatNumProbes(checkId);
```

## Availability

| Since Version |
|---|
