# ChkStart_LINSynchDelTimingViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSynchDelTimingViolation (dword MinDelLen, dword MaxDelLen);
```

## Description

Checks the timing of the synchronization break field in LIN headers.

An event will be generated, if the measured length [in bit times] of break delimiter is outside of the specified range.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length of break delimiter shall not be checked |
| >0 | Minimum allowed length of break delimiter |

## Return Values

0: Check could not be created and must not be referenced

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(9); // switch to ns precision
// Create and start the check for LIN Synch Delimiter violation
checkId = ChkStart_LINSynchDelTimingViolation(1, 5, "LINSynchDelimiterCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSynchDelimiterCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
