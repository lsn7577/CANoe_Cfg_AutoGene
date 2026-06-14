# ChkStart_LINMasterBaudrateViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINMasterBaudrateViolation (float ClockTolerance);
```

## Description

Checks the LIN Master baud rate, by analyzing frame headers.

An event will be generated, if the measured baud rate is outside of the specified range. The expected baud rate is taken from DB.

For a LIN 2.0 compliance the Master clock tolerance has to be in the range:

[-0.5 .. 0.5] %.

The actual baud rate is done in Synch Field with the sample rate of 1 second.

This check works only when LIN hardware is not in Master mode, i.e. when an external Master is used.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN Master baud rate violation
checkId = ChkStart_LINMasterBaudrateViolation(0.5, "LINMasterBaudrateCallback"); 
...
// CAPL callback for violation notification
void LINMasterBaudrateCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
