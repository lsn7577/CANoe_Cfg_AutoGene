# ChkStart_LINSchedTableViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINSchedTableViolation (dword TableIndex, duration Jitter);
```

## Description

Checks a certain LIN schedule table for correspondence with the database definition.

An event will be generated, if

The check has to be started only when the specified schedule table is already running. That is to allow run-time synchronization, which may take maximum one schedule cycle time.

This is not an appropriate function to check diagnostic schedule tables because dependent on the application silent slots can occur.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(6); // switch to µs precision
// Create and start the check for LIN schedule table with index 0
checkId = ChkStart_LINSchedTableViolation(0, "LINSchedTableCallback"); 
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINSchedTableCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
