# ChkStart_LINSyncDelTimingViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSyncDelTimingViolation (float MinDelLen, float MaxDelLen);
```

## Description

Checks the timing of the synchronization break field in LIN headers.

An event will be generated, if the measured length [in bit times] of break delimiter is outside of the specified range.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length of break delimiter shall not be checked |
| >0 | Minimum allowed length of break delimiter |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(9); // switch to ns precision
// Create and start the check for LIN Synch Delimiter violation
checkId = ChkStart_LINSyncDelTimingViolation(1, 5, "LINSyncDelimiterCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSyncDelimiterCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
