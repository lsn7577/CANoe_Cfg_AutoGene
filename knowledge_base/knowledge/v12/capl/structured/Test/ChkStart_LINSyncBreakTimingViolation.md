# ChkStart_LINSyncBreakTimingViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSyncBreakTimingViolation (float MinBreakLen, float MaxBreakLen);
```

## Description

Checks the timing of the synchronization break field in LIN headers.

An event will be generated, if the measured length [in bit times] of break low phase is outside of the specified range.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length of break low phase shall not be checked |
| >0 | Minimum allowed length of break low phase |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(9); // switch to ns precision
// Create and start the check for LIN break low phase violation
checkId = ChkStart_LINSyncBreakTimingViolation(13, 20, "LINSyncBreakCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSyncBreakCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
