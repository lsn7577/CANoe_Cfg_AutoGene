# ChkStart_LINMasterInitTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINMasterInitTimeViolation (duration MinTime, duration MaxTime);
```

## Description

Checks an initialization time of LIN Master. The initialization state is entered on switching on and on waking up.

An event will be generated, if the initialization time is out of the specified range.

This function verifies the initialization time on waking up only, i.e. a time between getting Wakeup signal and the first header transmitted by the Master.

For a LIN 2.0 compliance the initialization time has to be in the range [100 .. 150] ms.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum time shall not be checked |
| >0 | Minimum allowed initialization time |

## Example

```c
...
dword checkId;
// Create and start the check for LIN Master initialization time violation
checkId = ChkStart_LINMasterInitTimeViolation(100, 150, "LINMasterInitTimeCallback"); 
...
// CAPL callback for violation notification
void LINMasterInitTimeViolation (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
